from backend.services.groq_service import llm
response = llm.invoke(
    "who are you ?"
)
print(response.content)