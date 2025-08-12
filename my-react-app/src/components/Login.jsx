import { useState } from "react";
import API from "../api";

export default function Login({ setStep, setUserData }) {
  const [form, setForm] = useState({ username: "", password: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await API.post("/login", form);
    setUserData(res.data);
    if (res.data.mfa_required) setStep("mfa-prompt");
    else if (res.data.mfa_setup) setStep("mfa-setup");
    else setStep("dashboard");
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <h2>Login</h2>
        <input
          type="text"
          placeholder="Username"
          value={form.username}
          onChange={(e) => setForm({ ...form, username: e.target.value })}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) => setForm({ ...form, password: e.target.value })}
          required
        />
        <button type="submit">Login</button>
        <p className="text-center">
          Don't have an account?
          <button
            type="button"
            className="link-button"
            onClick={() => setStep("register")}
          >
            Register here
          </button>
        </p>
      </form>
    </div>
  );
}
