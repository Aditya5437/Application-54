from langchain_groq import ChatGroq
from backend.config.settings import settings

llm = ChatGroq(
    groq_api_key = settings.GROQ_API_KEY,
    model = settings.MODEL_NAME,
    temperature=settings.TEMPERATURE,
    max_tokens = settings.MAX_TOKENS
)