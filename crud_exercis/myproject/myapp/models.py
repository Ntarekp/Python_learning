from django.db import models
from django.utils import timezone

class Class(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    classes = models.ManyToManyField('Class', related_name='students', blank=True)
    
    class Meta:
        db_table = "students"
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"
    
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'class_instance', 'date')
        ordering = ['-date', 'student__name']
        db_table = "attendance"

    def __str__(self):
        return f"{self.student.name} - {self.class_instance.name} on {self.date}: {self.status}"
