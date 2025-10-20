from django import forms
from .models import Student, Attendance, Class

class StudentForm(forms.ModelForm):
    classes = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )
    
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'classes']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name',
                'autocomplete': 'off'
            }),
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student ID number',
                'autocomplete': 'off'
            })
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].help_text = 'Enter the full name of the student'
        self.fields['student_id'].help_text = 'Enter a unique student identification number'
        self.fields['classes'].help_text = 'Select the classes this student is enrolled in'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_instance', 'date', 'status', 'remarks']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        class_instance = cleaned_data.get('class_instance')
        date = cleaned_data.get('date')

        if student and class_instance and date:
            # Check if attendance already exists for this student on this date in this class
            existing = Attendance.objects.filter(
                student=student,
                class_instance=class_instance,
                date=date
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing.exists():
                raise forms.ValidationError(
                    'Attendance record already exists for this student on this date in this class.'
                )
        return cleaned_data

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'start_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }