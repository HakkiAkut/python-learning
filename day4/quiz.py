class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer

class Quiz():
    def __init__(self,question):
        self.question=question
        self.score=0
        self.index=0
    def getQuestion(self):
        return self.question[self.index]

    def display(self):
        quest=self.getQuestion()
        print(f"question {self.index+1}: {quest.text}\n{quest.choices} ")
        ans=int(input("answer: "))
        if(quest.checkAnswer(ans)):
            print("correct answer")
            self.score +=1
        else:
            print("wrong answer")
        print(f"current score: {self.score}")
        self.index +=1
    

q1= Question("5**2",[10,5,25,50],25)
q2= Question("20//2",[5,10,20,4],10)
q3= Question("34%5",[4,5,6,7],4)

questions=[q1,q2,q3]
quiz=Quiz(questions)
while(quiz.index<len(quiz.question)):
    quiz.display()
    





