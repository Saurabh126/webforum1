from __future__ import unicode_literals
import random 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from Login.models import User

@python_2_unicode_compatible
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    answer_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.answer_text


