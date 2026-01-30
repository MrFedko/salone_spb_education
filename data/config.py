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

    admins = [
        os.getenv("ADMIN_ID"),
    ]

    worksheet_ids = {
    "Коктейли и бар": (0, "cocktails"),
    "Информация": (1253150009, "info"),
    "Кухня": (814666576, "cuisine"),
    "Salumeria": (1454248563, "salumeria"),
    "Вино": (1074670247, "wine"),
    }

    db_tables = {
        0: "cocktails",
        1253150009: "info",
        814666576: "cuisine",
        1454248563: "salumeria",
        1074670247: "wine",
    }

    # PROJECT_PATH = "/Users/mac/Desktop/my_projects/saloneSpbEducation/saloneSpbEducation/"

    PROJECT_PATH = "/home/educationBot/salone_spb_education/"
    CREDS_PATH = PROJECT_PATH + os.getenv("CREDS_PATH")
    PHOTO_PATH = PROJECT_PATH + "data/photo/"
    DB_PATH = PROJECT_PATH + DB_NAME
    CREDS_PATH = PROJECT_PATH + os.getenv("CREDS_PATH")
    SERVER_IP = "localhost"
    SERVER_PORT = 8000
    SERVER_LINK = f"http://{SERVER_IP}:{SERVER_PORT}"
    # GOOGLE_DRIVE_FOLDER_ID = "1v7he5jjYeT-sXtbySeMvLA2R_ls-wRzW"

settings = Settings()
