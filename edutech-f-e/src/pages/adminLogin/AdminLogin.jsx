import React, { useState } from "react";
import { useNavigate } from 'react-router-dom'
import './AdminLogin.css';

import { adminLogin } from "../../api";
const AdminLogin = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await adminLogin({email, password});
    if (response.token) {
      localStorage.setItem("token", response.token);
      navigate('/');
    }
    else {
      setErrorMessage("Invalid username or password");
    }
  };

  return (
    <div className="login-form">
      <h1>Admin Login</h1>
      <input
        type="text"
        placeholder="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit" onClick={handleSubmit}>
        Login
      </button>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
    </div>
  );
};

export default AdminLogin;