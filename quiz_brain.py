
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        i = self.question_number
        self.question_number +=1
        user_answer = input(f"Q.{i + 1}: {self.question_list[i].text} (True/False)?: ")
        return user_answer

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer is: {self.question_list[self.question_number-1].answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n\n")

