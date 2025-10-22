from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id')
    search_fields = ('name', 'student_id')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'is_present')
    list_filter = ('date', 'is_present')
    search_fields = ('student__name', 'class_instance__name')
    date_hierarchy = 'date'
    list_per_page = 20
