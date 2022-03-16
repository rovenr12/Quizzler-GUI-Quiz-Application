import requests
from question_model import Question

TRIVIA_API = "https://opentdb.com/api.php"


def generate_new_data():
    params = {
        "amount": 10,
        "category": 18,
        "type": "boolean"
    }
    response = requests.get(TRIVIA_API, params=params)
    response.raise_for_status()
    return response.json()['results']


def generate_question_bank():
    question_data = generate_new_data()
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank