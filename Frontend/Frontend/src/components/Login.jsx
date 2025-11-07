import React, { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import emailIcon from "../assets/email_icon.png";
import passwordIcon from "../assets/password_icon.png";

const Login = () => {
 const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");  

  const isValidEmail = (email) => {
    return /\S+@\S+\.\S+/.test(email);
  };

  const handleLogin = async () => {
    if (!isValidEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }
    if (password.length < 6) {
      alert("Password must be at least 6 characters.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const result = await response.json();

      if (response.ok) {
        alert(result.message); 
        navigate("/dashboard");

      } else {
        alert(result.detail);  
      }
    } catch (error) {
      console.error("Login failed:", error);
      alert("An error occurred during login.");
    }
    setEmail("")
    setPassword("")
  };

  return (
    <div className='container'>
      <div className="header">
        <div className="text">Login</div>
        <div className="underline"></div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={emailIcon} alt="email icon" />
          <input 
            type="email" 
            placeholder='Enter email'
            value={email}
            onChange={(e) => setEmail(e.target.value)} 
          />
        </div>
        <div className="input">
          <img src={passwordIcon} alt="password icon" />
          <input 
            type="password" 
            placeholder='Enter password'
            value={password}
            onChange={(e) => setPassword(e.target.value)} 
          />
        </div>
      </div>

      <div className="submit-container">
        <div className="submit" onClick={handleLogin}>Login</div>
      </div>

      <div className="Registered">
        <p>Don't have an account?</p>
        <NavLink to="/" className="submit">Sign Up</NavLink>
      </div>
      <div className="dashboard">
        <p>This is my Dashboard</p>
        <NavLink to="/" className="submit">Dashboard</NavLink>
      </div>
    </div>
  );
};

export default Login;
