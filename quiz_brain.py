class QuizBrain:

  def __init__(self,question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
    
  def next_question(self) :
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)")
    self.check_answer(user_answer,current_question.answer)

  def still_have_questions(self):
    return self.question_number < len(self.question_list)
  
  def check_answer(self,user_answer,actual_answer):
    if user_answer.lower() == actual_answer.lower():
      self.score += 1
      print("You Right")
    else :
      print("You Wrong")
    print(f"The correct Answer is {actual_answer}")
    print(f"Your Score is : {self.score}/{self.question_number}")
    print("\n")
      
    