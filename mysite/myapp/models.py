from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200) 
class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

