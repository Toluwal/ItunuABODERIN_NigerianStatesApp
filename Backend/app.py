from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os
from sqlalchemy import text
from database import db
from fastapi.middleware.cors import CORSMiddleware
import bcrypt
load_dotenv()
app = FastAPI(title="Test API", version="1.0.0")
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get("/")
def home():
    return "Welcome to my API"
class User(BaseModel):
    name: str = Field(..., example="sam")
    email: str = Field(..., example="sam@gmail.com")
    password: str = Field(..., example="sam123")
@app.post('/signup')
def sign_up(input: User):
    try:
        duplicate_query = text("""
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
        return {"message": "User created successfully",
                "data": {
                    "name": input.name,
                    "email": input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
class userLogin(BaseModel):
    email: str = Field(..., example="sam@gmail.com")
    password: str = Field(..., example="sam123")
@app.post("/login")
def login(input: userLogin):
    try:
        query =text("""
            SELECT * FROM user_info
            WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).fetchone()
        if not result:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))
        if not verified_password:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return {
            "message": "Login Successful!"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class UpdateUser(BaseModel):
    name: str = Field(..., example="sam")
    email: str = Field(..., example="sam@gmail.com")
    password: str = Field(..., example="sam123")

@app.put("/update/{email}")
def update_user(email: str, input: UpdateUser):
    try:
        query = text("""
            SELECT * FROM user_info WHERE email = :email
        """)
        existing = db.execute(query, {"email": email}).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="User not found")
        update_query = text("""
            UPDATE user_info
            SET name = :name, password = :password
            WHERE email = :email
        """)
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), bcrypt.gensalt()) if input.password else existing.password
        db.execute(update_query, {"name": input.name or existing.name, "password": hashedPassword, "email": email})
        db.commit()
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/update-name/{email}")
def patch_name(email: str, input: UpdateUser):
    try:
        query = text("""
            UPDATE user_info SET name = :name WHERE email = :email
        """)
        db.execute(query, {"name": input.name, "email": email})
        db.commit()
        return {"message": "User name updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{email}")
def delete_user(email: str):
    try:
        query = text("""
            DELETE FROM user_info WHERE email = :email
        """)
        db.execute(query, {"email": email})
        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))








