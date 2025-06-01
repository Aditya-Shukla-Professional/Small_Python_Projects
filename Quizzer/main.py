from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

my_email="rthcdr13@gmail.com"
password="ofafkdnhndcbxxny"

response=requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data=response.json()
question_bank = []
for i in range(10):
    question_text = data["results"][i]["question"]
    question_answer = data["results"][i]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)




quiz = QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
