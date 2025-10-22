from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Attendance
from django.utils import timezone


def attendance_list(request):
    """Show all attendance records (simple list)."""
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, 'myapp/attendance_list.html', {
        'attendances': attendances,
        'today': timezone.now().date()
    })


def mark_attendance(request):
    """Display students with checkboxes and save attendance for selected date (today by default)."""
    today = timezone.now().date()

    if request.method == 'POST':
        present_students = request.POST.getlist('present_students')
        date = request.POST.get('date') or str(today)

        # Remove existing records for that date
        Attendance.objects.filter(date=date).delete()

        # Create attendance records: present for selected, absent for others
        all_students = Student.objects.all()
        for student in all_students:
            Attendance.objects.create(
                student=student,
                date=date,
                is_present=(str(student.id) in present_students)
            )

        messages.success(request, 'Attendance saved.')
        return redirect('attendance_list')

    students = Student.objects.all().order_by('name')
    return render(request, 'myapp/mark_attendance.html', {
        'students': students,
        'today': today
    })


def add_student(request):
    """Show simple add-student page and handle POST to create a student."""
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        if name and student_id:
            Student.objects.create(name=name, student_id=student_id)
            messages.success(request, 'Student added.')
            return redirect('mark_attendance')
        else:
            messages.error(request, 'Please provide both name and student id.')

    return render(request, 'myapp/add_student.html')

def edit_student(request, student_id):
    """Edit an existing student."""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id_new = request.POST.get('student_id')
        
        if name and student_id_new:
            student.name = name
            student.student_id = student_id_new
            student.save()
            messages.success(request, 'Student updated.')
            return redirect('mark_attendance')
        else:
            messages.error(request, 'Please provide both name and student id.')
    
    return render(request, 'myapp/edit_student.html', {'student': student})

def delete_student(request, student_id):
    """Delete a student."""
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, 'Student deleted.')
    return redirect('mark_attendance')