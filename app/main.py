from typing import List

import requests
from fastapi import FastAPI
from fastapi import HTTPException

from app.database import db_dependency
from app.database import engine
from app.helpers import check_existing_question
from app.helpers import create_question
from app.helpers import save_question
from app.models import Base
from app.schemas import QuestionBase
from app.schemas import RequestBase

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def main_page():
    return {}


@app.post("/quiz/", response_model=QuestionBase)
async def create_quiz(quiz_request: RequestBase, db: db_dependency):
    questions: List[QuestionBase] = []
    while len(questions) < quiz_request.questions_num:
        response = requests.get("https://jservice.io/api/random?count=1")
        if response.status_code == 200:
            data = response.json()
            question_data = data[0]
            question = create_question(question_data)
            existing_question = await check_existing_question(question, db)
            if not existing_question:
                await save_question(db, question)
                questions.append(question)
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Something wrong"
            )
    return questions[-1]
