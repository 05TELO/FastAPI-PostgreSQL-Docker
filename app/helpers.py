from datetime import datetime

from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app import schemas


def create_question(question_data: dict) -> models.Question:
    question = models.Question(
        id_question=question_data["id"],
        question_text=question_data["question"],
        answer_text=question_data["answer"],
        created_at=datetime.strptime(
            question_data["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ),
    )
    return question


async def check_existing_question(
    question: schemas.QuestionBase, db: AsyncSession
) -> models.Question | None:
    existing_question = await db.execute(
        select(models.Question).where(
            models.Question.id == question.id_question
        )
    )
    return existing_question.scalar()


async def save_question(db: AsyncSession, question: schemas.QuestionBase):
    db.add(question)
    await db.commit()
    await db.refresh(question)


async def get_question(client: AsyncClient, url: str):
    async with client as client:
        response = await client.get(url)
    return response

