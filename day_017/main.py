from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank_text = []
question_bank_ans = []
quiz_done = True

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_question = Question(text, answer)
    question_bank_text.append(new_question.q_text)
    question_bank_ans.append(new_question.q_answer)


quiz = QuizBrain(question_bank_text, question_bank_ans)

while quiz.still_has_questions():
    quiz.next_question()


print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
