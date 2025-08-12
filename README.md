# Associate Full Stack Developer Assessment: Django + React MFA Web App

## Introduction
Welcome to the Associate Full Stack Developer take-home assessment.  
This project demonstrates a secure web application built with Django (backend) and React (frontend), featuring user registration, login, and two-factor authentication (2FA) using Time-Based One-Time Passwords (TOTP) and QR codes.

---

## Table of Contents
- [Technologies](#technologies)  
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Setup and Installation](#setup-and-installation)  
- [MFA Flow Explanation](#mfa-flow-explanation)  
- [API Endpoints](#api-endpoints)  
- [Extra Credit Features](#extra-credit-features)  
- [Usage](#usage)  
- [Demo](#demo)  
- [Contact](#contact)

---

## Technologies
- **Backend:** Django, Django REST Framework, pyotp, qrcode  
- **Frontend:** React (or Next.js)  
- **Authentication:** JWT tokens, TOTP 2FA  
- **Others:** Axios or Fetch API for frontend-backend communication

---

## Project Overview
This app provides:
- User registration and login  
- Two-factor authentication using TOTP (compatible with apps like Google Authenticator)  
- QR code provisioning for easy MFA setup  
- Secure session management

---

## Features

### Backend (Django)
- User Registration & Authentication  
- MFA check after login  
- TOTP secret generation & QR code provisioning  
- Verification of TOTP codes during login  
- REST API endpoints for all user actions

### Frontend (React)
- User-friendly registration and login forms  
- Prompt for MFA code input when required  
- Display QR code for MFA setup if not enabled  
- Conditional rendering based on authentication and MFA state

---

## Setup and Installation

### Backend
1. Clone the repo and navigate to backend folder:
   ```bash
   cd backend
