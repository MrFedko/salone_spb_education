import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Education app"
    DB_NAME = "knowledge.db"
    PROJECT_DESCRIPTION = "Education app for restaurant staff"

    BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
    EMAIL_CONTROLLER = str(os.getenv("EMAIL_CONTROLLER"))
    SHEET_ID = str(os.getenv("SHEET_ID"))
    CREDS_PATH = os.getenv("CREDS_PATH")

    admins = [
        os.getenv("ADMIN_ID"),
    ]

    worksheet_ids = {
    }

    PROJECT_PATH = "/Users/mac/Desktop/my_projects/saloneSpbEducation/saloneSpbEducation/"
    # PROJECT_PATH = "/home/educationBot/"
    DB_PATH = PROJECT_PATH + DB_NAME
    SERVER_IP = "localhost"
    SERVER_PORT = 8000
    SERVER_LINK = f"http://{SERVER_IP}:{SERVER_PORT}"
    # GOOGLE_DRIVE_FOLDER_ID = "1v7he5jjYeT-sXtbySeMvLA2R_ls-wRzW"

settings = Settings()
