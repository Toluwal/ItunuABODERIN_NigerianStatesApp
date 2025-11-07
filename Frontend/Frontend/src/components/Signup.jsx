import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import emailIcon from "../assets/email_icon.png";
import passwordIcon from "../assets/password_icon.png";
import nameIcon from "../assets/name_icon.png";

const Signup = () => {
  const [name, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const isValidEmail = (email) => {
    return /\S+@\S+\.\S+/.test(email);
  };

  const handleSignup = async () => {
    if (name.length < 3) {
      alert("Name must be at least 3 characters long.");
      return;
    }
    if (!isValidEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }
    if (password.length < 6) {
      alert("Password must be at least 6 characters.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });

      const result = await response.json();

      if (response.ok) {
        alert(result.message);
      } else {
        alert(result.detail);
      }
    } catch (error) {
      console.error("Signup failed:", error);
      alert("An error occurred during signup.");
    }

    setFullName("");
    setEmail("");
    setPassword("");
  };

  return (
    <div className='container'>
      <div className="header">
        <div className="text">Sign Up</div>
        <div className="underline"></div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={nameIcon} alt="name icon" />
          <input 
            type="text" 
            placeholder='Enter your full name' 
            value={name}
            onChange={(e) => setName(e.target.value)} 
          />
        </div>
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
        <div className="submit" onClick={handleSignup}>Sign Up</div>
      </div>

      <div className="Registered">
        <p>Already have an account?</p>
        <NavLink to="/login" className="submit">
          Login
        </NavLink>
      </div>
    </div>
  );
};

export default Signup;
