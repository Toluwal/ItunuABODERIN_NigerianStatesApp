from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr, Field
from dotenv import load_dotenv
from sqlalchemy import text
from database import db
from fastapi.middleware.cors import CORSMiddleware
import bcrypt
import uvicorn
import os
load_dotenv()
app = FastAPI(title="Test API", version="1.0.0")
origin = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get("/")
def home():
    return "Welcom to my API"
class SignupRequest(BaseModel):
    name: str = Field(..., example="Bisayo Ololade")
    email: EmailStr = Field(..., example="bisayo@example.com")
    password: str = Field(..., example="bisayo123")
@app.post('/signup')
def sign_up(input:SignupRequest):
    try:
        duplicate_query= text("""
            SELECT * FROM user_info
            WHERE email = :email
        """)
        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
            print("Email already exists!")
        query = text("""
            INSERT INTO user_info (name, email, password)
            VALUES (:name, :email, :password)
        """)
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword})
        db.commit()
        return {"message": "User Created Successfully",
                "data": {"name": input.name, "email":input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="bisayo@gmail.com")
    password: str = Field(..., example="bisayo123")
@app.post("/login")
def login(input: LoginRequest):
    try:
        query = text("""
            SELECT * FROM user_info
            WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).fetchone()
        if not result:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))
        if not verified_password:
            raise HTTPException(status_code=401, detail="Inavlid email or password")
        return {
            "message": "Login Successful"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/states")
def states():
    try:
        get_states = text("""
            SELECT * from states;
        """)
        result = db.execute(get_states).mappings().all()
        if not result:
            return "No states yet. Try again later!"
        return {"states": result}
    except Exception as e:
        return {"details": str(e)}