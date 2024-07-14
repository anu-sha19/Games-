#T0DO ask user questions
#attributs: ques_num =0  ques_list
#method

class QuizBrain:

    def __init__(self, q_list):
        self.ques_num = 0
        self.ques_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.ques_list[self.ques_num]
        self.ques_num +=1
        user_answer = input(f"{self.ques_num}:{current_question.question} Category:{current_question.category} (True/False) ")
        self.check_answer(user_answer, current_question.correct_answer)

    def still_has_questions(self):
        return self.ques_num < len(self.ques_list)

    def check_answer(self, answer, right_answer):
        if answer.lower() == right_answer.lower():
            self.score += 1
            print(f"You got it right! Score:{self.score}/{self.ques_num}")
        else:
            print("That's wrong")


