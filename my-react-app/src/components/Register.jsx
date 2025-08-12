import { useState } from "react";
import API from "../api";

export default function Register({ setStep }) {
  const [form, setForm] = useState({ username: "", password: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/register", form);
    setStep("login");
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <h2>Register</h2>
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
        <button type="submit">Register</button>
        <p className="text-center">
          Already have an account?
          <button
            type="button"
            className="link-button"
            onClick={() => setStep("login")}
          >
            Login here
          </button>
        </p>
      </form>
    </div>
  );
}
