from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date', 'student__name']
        unique_together = ('student', 'date')

    def __str__(self):
        status = "Present" if self.is_present else "Absent"
        return f"{self.student.name} - {self.date}: {status}"
