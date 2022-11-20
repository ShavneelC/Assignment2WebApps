from rest_framework import serializers

from attendance.models import Course, Semester, Lecturer, Student, Classes, CollegeDay


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_id", "code", "name", "semester"]


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ["semester_id", "year", "semester"]


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ["user", "staff_id", "dob"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["user", "student_id", "dob"]


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["Class_number", "course", "semester", "lecturer", "student"]


class CollegeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDay
        fields = ["date", "classes", "student"]
