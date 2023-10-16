from sqlalchemy.orm import Session

from app import models
from app import schemas


def create_question(question_data: dict) -> models.Question:
    question = models.Question(
        id_question=question_data["id"],
        question_text=question_data["question"],
        answer_text=question_data["answer"],
        created_at=question_data["created_at"],
    )
    return question


async def check_existing_question(
    question: schemas.QuestionBase, db: Session
) -> models.Question | None:
    existing_question = (
        db.query(models.Question)
        .filter(models.Question.id == question.id_question)
        .first()
    )
    return existing_question


async def save_question(db: Session, question: schemas.QuestionBase):
    db.add(question)
    db.commit()
    db.refresh(question)
