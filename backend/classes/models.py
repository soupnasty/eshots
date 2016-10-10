from django.db import models

from students.models import Student


CLASS_CHOICES = (
    ('1', 'Math 101'),
    ('2', 'English 101'),
    ('3', 'Science 101'),
    ('4', 'Social Studies 101'),
    ('5', 'Health 101'),
    ('6', 'Chemistry 101'),
    ('7', 'English 201'),
    ('8', 'Math 201'),
)


class Class(models.Model):
    course = models.CharField(max_length=1, choices=CLASS_CHOICES, null=True, blank=False)
    grade = models.DecimalField(max_digits=2, decimal_places=1)
    student = models.ForeignKey(Student, related_name='classes', null=True, blank=True)

    class Meta:
        unique_together = (('course', 'student'),)
        ordering = ["student", "course"]

    def __str__(self):
        return u"Grade: {}".format(self.grade)


