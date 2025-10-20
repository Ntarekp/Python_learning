from django.contrib import admin
from .models import Class, Student, Attendance

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id')
    search_fields = ('name', 'student_id')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_instance', 'date', 'status')
    list_filter = ('status', 'date', 'class_instance')
    search_fields = ('student__name', 'class_instance__name')
    date_hierarchy = 'date'
    list_per_page = 20
