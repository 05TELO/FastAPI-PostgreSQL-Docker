from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    id_question = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime)
