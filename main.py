from question_model import Question
from quiz_brain import QuizBrain
from trivia_data import trivia_data
import random


random.shuffle(trivia_data)
question_bank = []

for index in range(1,11):
    question = trivia_data[index]["question"]
    answer = trivia_data[index]["correct_answer"]

    new_question = Question(question, answer)

    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_ans = quiz.next_question()
    quiz.check_answer(user_ans)

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")


