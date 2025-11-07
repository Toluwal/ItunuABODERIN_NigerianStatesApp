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

# insert_product = text ("""
# INSERT INTO states (name, capital, region, slogan, population, landmarks)
# VALUES
#     ("Abia", "Umuahia", "South-East", "God's Own State", 3700000, "National War Museum, Arochukwu Caves"),
#     ("Adamawa", "Yola", "North-East", "Land of Beauty", 4200000, "Sukur Kingdom, Mandara Mountains"),
#     ("Akwa Ibom", "Uyo", "South-South", "Land of Promise", 5500000, "Ibeno Beach, Amalgamation House"),
#     ("Anambra", "Awka", "South-East", "Light of the Nation", 5500000, "Ogbunike Caves, Onitsha Market"),
#     ("Bauchi", "Bauchi", "North-East", "Pearl of Tourism", 6500000, "Yankari National Park, Sumu Wildlife Park"),
#     ("Bayelsa", "Yenagoa", "South-South", "Glory of All Lands", 2300000, "Ox-Bow Lake, Isaac Boro Park"),
#     ("Benue", "Makurdi", "North-Central", "Food Basket of the Nation", 6000000, "Ikwe Holiday Resort, River Benue"),
#     ("Borno", "Maiduguri", "North-East", "Home of Peace", 5900000, "Shehu's Palace, Lake Chad"),
#     ("Cross River", "Calabar", "South-South", "The People's Paradise", 3900000, "Obudu Cattle Ranch, Calabar Carnival"),
#     ("Delta", "Asaba", "South-South", "The Big Heart", 5700000, "River Niger Bridge, Abraka Turf & Country Club"),
#     ("Ebonyi", "Abakaliki", "South-East", "Salt of the Nation", 2900000, "Abakaliki Rice Mill, Unwana Beach"),
#     ("Edo", "Benin City", "South-South", "Heartbeat of the Nation", 4200000, "Benin Moat, Oba Palace"),
#     ("Ekiti", "Ado-Ekiti", "South-West", "Fountain of Knowledge", 3300000, "Ikogosi Warm Springs, Erin-Ijesa Waterfalls"),
#     ("Enugu", "Enugu", "South-East", "Coal City State", 4500000, "Awhum Waterfall, Nike Lake Resort"),
#     ("Gombe", "Gombe", "North-East", "Jewel in the Savannah", 3300000, "Tangale Peak, Dukku Lake"),
#     ("Imo", "Owerri", "South-East", "Eastern Heartland", 5400000, "Oguta Lake, Mbari Cultural Centre"),
#     ("Jigawa", "Dutse", "North-West", "New World", 5800000, "Dutse Rock, Hadejia-Nguru Wetlands"),
#     ("Kaduna", "Kaduna", "North-West", "Centre of Learning", 8000000, "Kajuru Castle, Matsirga Waterfalls"),
#     ("Kano", "Kano", "North-West", "Centre of Commerce", 13000000, "Kurmi Market, Gidan Makama Museum"),
#     ("Katsina", "Katsina", "North-West", "Home of Hospitality", 7800000, "Gobarau Minaret, Kusugu Well"),
#     ("Kebbi", "Birnin Kebbi", "North-West", "Land of Equity", 4400000, "Argungu Fishing Festival, Kanta Museum"),
#     ("Kogi", "Lokoja", "North-Central", "Confluence State", 4500000, "Confluence of Rivers Niger and Benue, Lord Lugard House"),
#     ("Kwara", "Ilorin", "North-Central", "State of Harmony", 3200000, "Owu Waterfalls, Esie Museum"),
#     ("Lagos", "Ikeja", "South-West", "Centre of Excellence", 14000000, "Lekki Beach, National Museum Lagos"),
#     ("Nasarawa", "Lafia", "North-Central", "Home of Solid Minerals", 2500000, "Farin Ruwa Falls, Eggon Hills"),
#     ("Niger", "Minna", "North-Central", "Power State", 5600000, "Gurara Falls, Zuma Rock"),
#     ("Ogun", "Abeokuta", "South-West", "Gateway State", 5200000, "Olumo Rock, Oke-Mosan Palace"),
#     ("Ondo", "Akure", "South-West", "Sunshine State", 4700000, "Idanre Hills, Owo Museum"),
#     ("Osun", "Osogbo", "South-West", "State of the Living Spring", 4200000, "Osun-Osogbo Sacred Grove, Erin-Ijesha Waterfalls"),
#     ("Oyo", "Ibadan", "South-West", "Pace Setter State", 7500000, "Cocoa House, University of Ibadan"),
#     ("Plateau", "Jos", "North-Central", "Home of Peace and Tourism", 4200000, "Jos Wildlife Park, Shere Hills"),
#     ("Rivers", "Port Harcourt", "South-South", "Treasure Base of the Nation", 7000000, "Port Harcourt Pleasure Park, Isaac Boro Park"),
#     ("Sokoto", "Sokoto", "North-West", "Seat of the Caliphate", 4900000, "Sultan's Palace, Sokoto Museum"),
#     ("Taraba", "Jalingo", "North-East", "Nature's Gift to the Nation", 3100000, "Mambilla Plateau, Gashaka-Gumti National Park"),
#     ("Yobe", "Damaturu", "North-East", "Pride of the Sahel", 3200000, "Dagona Bird Sanctuary, Bade Emirate"),
#     ("Zamfara", "Gusau", "North-West", "Farming is our Pride", 4500000, "Jata Rock Shelter, Kuyambana Game Reserve"),
#     ("FCT", "Abuja", "North-Central", "Centre of Unity", 3500000, "Aso Rock, National Mosque, Zuma Rock")
# """)
# db.execute(insert_product)
# db.commit()
# print("Products successfully added!")
