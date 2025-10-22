import os
import sys
import django
from datetime import date
from pathlib import Path

# Ensure project root is on sys.path so Django can import settings
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.test import Client
from myapp.models import Student, Attendance

client = Client()

print('Starting test flows...')

# 1) Ensure DB is available and list students
print('Existing students:', Student.objects.count())

# 2) Add a test student via the POST view
resp = client.post('/students/add/', {'name': 'AutoTest Student', 'student_id': 'AT001'})
print('Add student POST status code:', resp.status_code)

# Get the created student
student = Student.objects.filter(student_id='AT001').first()
if not student:
    print('Failed to create student via view; creating directly via ORM as fallback')
    student = Student.objects.create(name='AutoTest Student', student_id='AT001')
else:
    print('Created student:', student.id, student.name)

# 3) Mark attendance for today, marking the created student present
today = date.today().isoformat()
resp2 = client.post('/attendance/mark/', {'date': today, 'present_students': [str(student.id)]})
print('Mark attendance POST status code:', resp2.status_code)

# 4) Query attendance records for today
records = Attendance.objects.filter(date=today)
print('Attendance records for', today, ':', records.count())
for r in records:
    print(f'- Student {r.student.name} (id={r.student_id}) present={r.is_present}')

print('Test flows completed.')
