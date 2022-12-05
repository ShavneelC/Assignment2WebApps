from django.contrib import admin

# Register your models here.
from attendance.models import Student, Lecturer, Course, Semester, CollegeDay, Classes, User, Attendance

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(CollegeDay)
admin.site.register(User)
admin.site.register(Attendance)





