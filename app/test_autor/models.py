from django.db import models


from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    def __str__(self):
        return self.answer_text


class CorrectAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.answer}"

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.test} - {self.student_name}"
