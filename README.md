# Quiz app

---

## Usage

After successful build & run, you can open http://localhost:8000/docs

---

## Installation

Before doing something, make sure that you have

1. copied .env.example to .env
2. modified values in .env according to your realm

---

> docker-compose up --build
 
___

POST http://localhost:8000/quiz
Content-Type: application/json

{
  "questions_num": 5
}
