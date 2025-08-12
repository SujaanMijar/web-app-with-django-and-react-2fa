import { useState } from "react";
import Register from "./components/Register";
import Login from "./components/Login";
import MFAPrompt from "./components/MFAPrompt";
import MFASetup from "./components/MFASetup";

function App() {
  const [step, setStep] = useState("login");
  const [userData, setUserData] = useState({});

  return (
    <div className="container">
      {step === "register" && <Register setStep={setStep} />}
      {step === "login" && <Login setStep={setStep} setUserData={setUserData} />}
      {step === "mfa-prompt" && <MFAPrompt setStep={setStep} userData={userData} />}
      {step === "mfa-setup" && <MFASetup setStep={setStep} userData={userData} />}
    </div>
  );
}

export default App;
