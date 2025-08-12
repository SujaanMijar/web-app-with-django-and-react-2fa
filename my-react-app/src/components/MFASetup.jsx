import { useEffect, useState } from "react";
import API from "../api";

export default function MFASetup({ setStep, userData }) {
  const [qr, setQr] = useState("");

  useEffect(() => {
    API.get("/mfa/setup", { params: { user_id: userData.user_id } }).then(res => {
      setQr(res.data.qr_code);
    });
  }, [userData.user_id]);

  return (
    <div className="flex flex-col gap-4">
      <img src={`data:image/png;base64,${qr}`} alt="MFA QR Code" />
      <p>Scan with Google Authenticator</p>
    </div>
  );
}
