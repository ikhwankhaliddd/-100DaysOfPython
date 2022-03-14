from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)

  question_bank.append(new_question)



quizzes = QuizBrain(question_bank)

while quizzes.still_have_questions() :
  quizzes.next_question()

print("You completed the quizzes!")
print(f"Your final score is {quizzes.score}/{quizzes.question_number}")