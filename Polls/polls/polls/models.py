from django.db import models

class Question(models.Model):
    question_txt=models.TextField()
    pub_date=models.DateField()
    def __str__(self):
        return self.question_txt