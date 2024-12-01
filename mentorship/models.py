from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name

    def student_count(self):
        return self.student_set.count()

class Student(models.Model):
    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
