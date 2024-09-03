# Question classı oluşturun

# Quiz classı oluşturupu Question class'ındaki soruları alıp sırasıyla kullanıcıya
# soruları göstermesi gerek. Soruya cevaplar verilmesi istenecek ve verilen cevaplara
# göre de skor belirlenecek.

#QUESTION

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
'''
q1 = Question('en iyi programlama dili hangisidir?', ['c#', 'python', 'javascript', 'java'], 'python')
q2 = Question('en popüler programlama dili hangisidir?', ['python', 'c#',  'javascript', 'java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?', ['c#', 'javascript', 'java', 'python'], 'python')

print(q1.checkAnswer('java')) # Çıktı: False
print(q2.checkAnswer('python')) # Çıktı: True
'''

# QUIZ
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0  #başlangıçta skor sıfır
        self.questionIndex = 0 #0. indeksteki yani birinci soruyla başlıyoruz.

        #Index ile sürekli işlem yapmak doğru olmaz, bunun için bir metod tanımlıyoruz.

        def getQuestion(self):
            return self.questions[self.questionIndex]

q1 = Question('en iyi programlama dili hangisidir?', ['c#', 'python', 'javascript', 'java'], 'python')
q2 = Question('en popüler programlama dili hangisidir?', ['python', 'c#',  'javascript', 'java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?', ['c#', 'javascript', 'java', 'python'], 'python')

questions = [q1, q2, q3]

quiz = Quiz(questions)
# question = quiz.questions[quiz.questionIndex]
question = quiz.getQuestion()
print(question.text)

##### BU KISMI YAPAMADIMM!! NESNE TABANLI PROGRAMLAMA, QUIZ KISMINA BAK #####