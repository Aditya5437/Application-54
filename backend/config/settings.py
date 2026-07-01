from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    USDA_API_KEY = os.getenv("USDA_API_KEY")


    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", 0)
    )

    MAX_TOKENS = int(
        os.getenv("MAX_TOKENS", 2048)
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )


settings = Settings()