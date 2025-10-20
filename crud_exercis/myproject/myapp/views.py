from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Class, Student, Attendance
from .forms import StudentForm, AttendanceForm, ClassForm
from django.utils import timezone

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'myapp/attendance_list.html'
    context_object_name = 'attendances'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'myapp/attendance_form.html'
    form_class = AttendanceForm
    success_url = reverse_lazy('attendance_list')

    def form_valid(self, form):
        messages.success(self.request, 'Attendance record created successfully.')
        return super().form_valid(form)

class AttendanceUpdateView(UpdateView):
    model = Attendance
    template_name = 'myapp/attendance_form.html'
    form_class = AttendanceForm
    success_url = reverse_lazy('attendance_list')

    def form_valid(self, form):
        messages.success(self.request, 'Attendance record updated successfully.')
        return super().form_valid(form)

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'myapp/attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Attendance record deleted successfully.')
        return super().delete(request, *args, **kwargs)

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'myapp/student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'myapp/student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
