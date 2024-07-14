from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    question = items["question"]
    answer = items["correct_answer"]
    category = items["category"]
    difficulty = items["difficulty"]
    question_bank.append(Question(question, answer, difficulty, category))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
     quiz.next_question()
print("\nYou have finished the quiz!")
print(f" Your final score is {quiz.score}/{quiz.ques_num}")