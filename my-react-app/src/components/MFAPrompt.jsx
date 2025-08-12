import { useState } from "react";
import API from "../api";

export default function MFAPrompt({ setStep, userData }) {
  const [code, setCode] = useState("");

  const verify = async (e) => {
    e.preventDefault();
    await API.post("/mfa/verify", { code, user_id: userData.user_id });
    setStep("dashboard");
  };

  return (
    <form onSubmit={verify} className="flex flex-col gap-2">
      <input placeholder="Enter MFA Code" onChange={(e) => setCode(e.target.value)} />
      <button type="submit">Verify</button>
    </form>
  );
}
