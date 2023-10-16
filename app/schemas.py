from datetime import datetime

from pydantic import BaseModel


class RequestBase(BaseModel):
    questions_num: int


class QuestionBase(BaseModel):
    id_question: int
    question_text: str
    answer_text: str
    created_at: datetime
