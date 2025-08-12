import io, base64
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import UserMFA
from .serializers import RegisterSerializer
import pyotp, qrcode
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    ser = RegisterSerializer(data=request.data)
    if ser.is_valid():
        user = ser.save()
        UserMFA.objects.create(user=user)
        return Response({'msg':'user created'}, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'detail':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    # check mfa
    mfa, _ = UserMFA.objects.get_or_create(user=user)
    if mfa.mfa_enabled:
        # Do not issue final tokens yet — request MFA code next.
        # Return short message: MFA required plus a temporary token (not JWT). For simplicity, we return user_id.
        return Response({'mfa_required': True, 'user_id': user.id})
    # No MFA -> issue JWT tokens
    refresh = RefreshToken.for_user(user)
    return Response({'mfa_required': False, 'access': str(refresh.access_token), 'refresh': str(refresh)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mfa_setup(request):
    user = request.user
    mfa, _ = UserMFA.objects.get_or_create(user=user)
    if not mfa.totp_secret:
        secret = pyotp.random_base32()
        mfa.totp_secret = secret
        mfa.save()
    else:
        secret = mfa.totp_secret
    issuer = "MyApp"
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user.username, issuer_name=issuer)
    img = qrcode.make(uri)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    data_uri = 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode()
    return Response({'qr': data_uri})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mfa_verify(request):
    code = request.data.get('code')
    user = request.user
    mfa, _ = UserMFA.objects.get_or_create(user=user)
    if not mfa.totp_secret:
        return Response({'detail':'No TOTP secret'}, status=status.HTTP_400_BAD_REQUEST)
    totp = pyotp.TOTP(mfa.totp_secret)
    if totp.verify(code):
        mfa.mfa_enabled = True
        mfa.save()
        return Response({'verified': True})
    return Response({'verified': False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def mfa_login_verify(request):
    # This endpoint is used to finish login when MFA is enabled.
    user_id = request.data.get('user_id')
    code = request.data.get('code')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail':'no user'}, status=status.HTTP_400_BAD_REQUEST)
    mfa, _ = UserMFA.objects.get_or_create(user=user)
    if not mfa.totp_secret:
        return Response({'detail':'no secret'}, status=status.HTTP_400_BAD_REQUEST)
    totp = pyotp.TOTP(mfa.totp_secret)
    if totp.verify(code):
        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token), 'refresh': str(refresh)})
    return Response({'detail':'invalid code'}, status=status.HTTP_400_BAD_REQUEST)