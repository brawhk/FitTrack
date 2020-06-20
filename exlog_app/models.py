from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ExerciseLog contains many exercises (acts like a list of exercises)
class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user) + "\t" + str(self.date)

class Exercise(models.Model):
    exercise_log = models.ForeignKey(ExerciseLog, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=32)
    num_sets = models.IntegerField()
    num_reps = models.IntegerField()
    exercise_weight = models.IntegerField()
    
    def __str__(self):
        return str(self.exercise_log) + "\t" + str(self.exercise_name) + "\t" + str(self.num_sets) + "x" + str(self.num_reps) + "\t" + str(self.exercise_weight)
    

