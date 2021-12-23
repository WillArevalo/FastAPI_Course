# Internal imports
from core.config import settings
# External imports
from fastapi import FastAPI

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get('/')
def hello_api():
    return {"detail:Hello World!"}

# Run with: uvicorn main:app --reload