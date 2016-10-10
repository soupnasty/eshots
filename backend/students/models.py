from django.db import models


class Student(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return u"{} {}".format(self.first, self.last)

    @property
    def full_name(self):
        return self.first + ' ' + self.last

    @property
    def average_gpa(self):
        grades = [float(obj.grade) for obj in self.classes.all()]
        if not grades:
            return None
        return float("{0:.2f}".format(sum(grades) / float(len(grades))))
