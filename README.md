Itunu Bisayo ABODERIN

Publica Academy Logo
Publica Academy
Examination Platform

Itunu Aboderin
learner
Logout
Taking Exam: AI Developers Course - General
AI Developers Course - General
Exam Window: 12:00 PM - 4:00 PM

Active
MCQ Section
Started: 12:02:01 PM WAT
Theory Section
Started: 12:12:05 PM WAT
213:53
Theory Section
Started: 12:12:05 PM WAT
Until exam ends
Theory Time Window: You can work until the exam ends at 2025-11-07T16:00:00 WAT.
Theory/Hands-on Section
Instructions:
Nigerian States Explorer Application
Module: Full-Stack Web Development with React, FastAPI & MySQL

Scenario
You have been hired to develop a Nigerian States Explorer web application. The system should allow users to create an account, login securely, and view information about all 36 Nigerian states plus the FCT.

What You Will Build
A full-stack web application with:

Frontend: React application with multiple pages
Backend: FastAPI server with MySQL database using SQLAlchemy ORM
Features: User authentication and Nigerian states information display
Core Features
1. User Authentication
Signup Page:

Collect: Full Name, Email, Password
Validate email format and password strength (minimum 6 characters)
Store user data securely in MySQL database
Show success/error messages
Login Page:

Collect: Email and Password
Verify credentials against database
Redirect to dashboard on successful login
Show error message for invalid credentials
2. States Dashboard (Main Page - After Login)
Display all Nigerian states in a grid or card layout
Each state card should show:
State Name
Capital
Region (North-East, North-West, North-Central, South-East, South-South, South-West)
Slogan
Population
Landmarks
3. Logout Functionality
Logout button on dashboard
Redirects user back to login page
Technology Stack
Frontend
React (using Vite)
React Router for navigation
fetch for API calls
CSS for styling
Backend
FastAPI framework
Pydantic for request/response validation
SQLAlchemy for database operations
MySQL database
Bcrypt for password hashing
python-dotenv for environment variables
Folder Structure
nigerian-states-app/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Signup.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── StateCard.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   └── package.json
│
└── backend/
    ├── main.py
    ├── database.py
    ├── .env
    └── requirements.txt
Database Schema
Environment Variables (.env file)
dbuser=your_mysql_username
dbpassword=your_mysql_password
dbhost=localhost
dbport=3306
dbname=nigerian_states_db
Database Tables (Created via SQLAlchemy)
Table 1: users

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Table 2: states

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capital VARCHAR(50) NOT NULL,
    region VARCHAR(20) NOT NULL,
    slogan VARCHAR(200),
    population INT,
    landmarks TEXT
);
API Endpoints (FastAPI)
Authentication
POST /api/signup - Register new user

Request body (Pydantic model): {full_name: str, email: str, password: str}
Response: {message: "User created successfully", user_id: 1}
POST /api/login - Login user

Request body (Pydantic model): {email: str, password: str}
Response: {message: "Login successful", user: {id, full_name, email}}
States
GET /api/states - Get all Nigerian states
Response: Array of all states with their details
Steps to Complete
Part A: Backend Setup (FastAPI + SQLAlchemy + MySQL)
Environment Setup:

Install dependencies: fastapi, uvicorn, sqlalchemy, pymysql, bcrypt, python-dotenv, pydantic
Create .env file with database credentials:
dbuser=root
dbpassword=your_password
dbhost=localhost
dbport=3306
dbname=nigerian_states_db
Database Configuration (database.py):

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pymysql.constants import CLIENT
import os

load_dotenv()

db_url = f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"

engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)

session = sessionmaker(bind=engine)
db = session()

# Create tables
create_table_query = text("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capital VARCHAR(50) NOT NULL,
    region VARCHAR(20) NOT NULL,
    slogan VARCHAR(200),
    population INT,
    landmarks TEXT
);
""")

db.execute(create_table_query)
db.commit()
print("Tables created successfully!")
Pydantic Models (in main.py):

Define request/response models using Pydantic BaseModel
Example:
from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
FastAPI Application (main.py):

Import FastAPI, database, bcrypt, Pydantic models
Create FastAPI app instance
Implement all API endpoints using Pydantic for validation
API Endpoints Implementation:

Signup endpoint (POST /api/signup):

Use Pydantic model to validate request body (SignupRequest)
Check if email already exists using SQL query
Hash password using bcrypt: bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
Insert new user into database using text() and SQL INSERT
Return success message with user_id
Login endpoint (POST /api/login):

Use Pydantic model to validate request body (LoginRequest)
Query database for user by email using text() and SQL SELECT
Verify password hash using bcrypt: bcrypt.checkpw(password.encode('utf-8'), stored_hash)
Return user data (id, full_name, email) on success
Return error message if credentials invalid
Get all states (GET /api/states):

Query all states from database using text() and SQL SELECT
Convert results to list of dictionaries
Return list of all states with complete information
Populate States Data:

Use text() with INSERT statements or loop through the states data
Use the complete data provided below
Part B: Frontend Setup (React)
React Setup:

Create React app using Vite: npm create vite@latest frontend -- --template react
Install dependencies: react-router-dom
Set up routing for different pages (Signup, Login, Dashboard)
Build Components:

Signup Component:

Form with fields: Full Name, Email, Password
Validate email format (contains @)
Validate password length (minimum 6 characters)
Submit form data to backend /api/signup
Show success message and redirect to login
Show error message if signup fails
Login Component:

Form with fields: Email, Password
Submit credentials to backend /api/login
Store user data in component state or localStorage
Redirect to dashboard on success
Show error message for invalid credentials
Dashboard Component:

Fetch all states from /api/states when component loads
Display states in a responsive grid (3-4 cards per row)
Each card shows: State name, capital, region, slogan, population, landmarks
Include logout button at top
StateCard Component:

Reusable component to display state information
Props: state data (name, capital, region, slogan, population, landmarks)
Styling (CSS):

Create professional and clean design
Use CSS Grid or Flexbox for layouts
Style forms with proper spacing and labels
Style state cards with borders, shadows, and hover effects
Make the application responsive for mobile devices
Use consistent colors and fonts throughout
Navigation:

Use React Router for page navigation
Route setup:
/ - Signup page
/login - Login page
/dashboard - States dashboard
Complete Nigerian States Data (37 States Including FCT)
Use this data format to populate your database:

states_data = [
    ("Abia", "Umuahia", "South-East", "God's Own State", 3700000, "National War Museum, Arochukwu Caves"),
    ("Adamawa", "Yola", "North-East", "Land of Beauty", 4200000, "Sukur Kingdom, Mandara Mountains"),
    ("Akwa Ibom", "Uyo", "South-South", "Land of Promise", 5500000, "Ibeno Beach, Amalgamation House"),
    ("Anambra", "Awka", "South-East", "Light of the Nation", 5500000, "Ogbunike Caves, Onitsha Market"),
    ("Bauchi", "Bauchi", "North-East", "Pearl of Tourism", 6500000, "Yankari National Park, Sumu Wildlife Park"),
    ("Bayelsa", "Yenagoa", "South-South", "Glory of All Lands", 2300000, "Ox-Bow Lake, Isaac Boro Park"),
    ("Benue", "Makurdi", "North-Central", "Food Basket of the Nation", 6000000, "Ikwe Holiday Resort, River Benue"),
    ("Borno", "Maiduguri", "North-East", "Home of Peace", 5900000, "Shehu's Palace, Lake Chad"),
    ("Cross River", "Calabar", "South-South", "The People's Paradise", 3900000, "Obudu Cattle Ranch, Calabar Carnival"),
    ("Delta", "Asaba", "South-South", "The Big Heart", 5700000, "River Niger Bridge, Abraka Turf & Country Club"),
    ("Ebonyi", "Abakaliki", "South-East", "Salt of the Nation", 2900000, "Abakaliki Rice Mill, Unwana Beach"),
    ("Edo", "Benin City", "South-South", "Heartbeat of the Nation", 4200000, "Benin Moat, Oba Palace"),
    ("Ekiti", "Ado-Ekiti", "South-West", "Fountain of Knowledge", 3300000, "Ikogosi Warm Springs, Erin-Ijesa Waterfalls"),
    ("Enugu", "Enugu", "South-East", "Coal City State", 4500000, "Awhum Waterfall, Nike Lake Resort"),
    ("Gombe", "Gombe", "North-East", "Jewel in the Savannah", 3300000, "Tangale Peak, Dukku Lake"),
    ("Imo", "Owerri", "South-East", "Eastern Heartland", 5400000, "Oguta Lake, Mbari Cultural Centre"),
    ("Jigawa", "Dutse", "North-West", "New World", 5800000, "Dutse Rock, Hadejia-Nguru Wetlands"),
    ("Kaduna", "Kaduna", "North-West", "Centre of Learning", 8000000, "Kajuru Castle, Matsirga Waterfalls"),
    ("Kano", "Kano", "North-West", "Centre of Commerce", 13000000, "Kurmi Market, Gidan Makama Museum"),
    ("Katsina", "Katsina", "North-West", "Home of Hospitality", 7800000, "Gobarau Minaret, Kusugu Well"),
    ("Kebbi", "Birnin Kebbi", "North-West", "Land of Equity", 4400000, "Argungu Fishing Festival, Kanta Museum"),
    ("Kogi", "Lokoja", "North-Central", "Confluence State", 4500000, "Confluence of Rivers Niger and Benue, Lord Lugard House"),
    ("Kwara", "Ilorin", "North-Central", "State of Harmony", 3200000, "Owu Waterfalls, Esie Museum"),
    ("Lagos", "Ikeja", "South-West", "Centre of Excellence", 14000000, "Lekki Beach, National Museum Lagos"),
    ("Nasarawa", "Lafia", "North-Central", "Home of Solid Minerals", 2500000, "Farin Ruwa Falls, Eggon Hills"),
    ("Niger", "Minna", "North-Central", "Power State", 5600000, "Gurara Falls, Zuma Rock"),
    ("Ogun", "Abeokuta", "South-West", "Gateway State", 5200000, "Olumo Rock, Oke-Mosan Palace"),
    ("Ondo", "Akure", "South-West", "Sunshine State", 4700000, "Idanre Hills, Owo Museum"),
    ("Osun", "Osogbo", "South-West", "State of the Living Spring", 4200000, "Osun-Osogbo Sacred Grove, Erin-Ijesha Waterfalls"),
    ("Oyo", "Ibadan", "South-West", "Pace Setter State", 7500000, "Cocoa House, University of Ibadan"),
    ("Plateau", "Jos", "North-Central", "Home of Peace and Tourism", 4200000, "Jos Wildlife Park, Shere Hills"),
    ("Rivers", "Port Harcourt", "South-South", "Treasure Base of the Nation", 7000000, "Port Harcourt Pleasure Park, Isaac Boro Park"),
    ("Sokoto", "Sokoto", "North-West", "Seat of the Caliphate", 4900000, "Sultan's Palace, Sokoto Museum"),
    ("Taraba", "Jalingo", "North-East", "Nature's Gift to the Nation", 3100000, "Mambilla Plateau, Gashaka-Gumti National Park"),
    ("Yobe", "Damaturu", "North-East", "Pride of the Sahel", 3200000, "Dagona Bird Sanctuary, Bade Emirate"),
    ("Zamfara", "Gusau", "North-West", "Farming is our Pride", 4500000, "Jata Rock Shelter, Kuyambana Game Reserve"),
    ("FCT", "Abuja", "North-Central", "Centre of Unity", 3500000, "Aso Rock, National Mosque, Zuma Rock")
]
Important Notes
Use Pydantic models for request/response validation in FastAPI
Use SQLAlchemy with text() for database queries (follow the pattern taught in class)
Use bcrypt for password hashing
Use python-dotenv to load database credentials from .env file
Do NOT use Tailwind CSS - Use regular CSS only
Do NOT add CORS middleware - Not required for this exam
Hash passwords before storing (never store plain text passwords)
Make sure both frontend and backend run without errors
Use meaningful variable and function names
Comment your code where necessary
Ensure all 37 states are in your database
📝 Submission Requirements
Submit a ZIP file named: YourName_NigerianStatesApp.zip

The ZIP file must contain:

backend/ folder with:

All Python files (main.py, database.py)
requirements.txt
frontend/ folder with:

All React files and folders (src/, public/, etc.)
package.json
database_export.sql - Export of your MySQL database with all states data

README.md - Include:

Your full name
Any additional notes
Good luck! 🚀



python
pandas
fastapi
sqlalchemy
pydantic
pyjwt
python-dotenv
pymysql
bcrypt
uvicorn
pymysql
fastapi-cors
dotenv

