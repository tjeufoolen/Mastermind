from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DATABASE_FILE = os.getenv("DATABASE_FILE")
SECRET_KEY = os.getenv("SECRET_KEY")
