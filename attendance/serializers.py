from django.contrib.auth.models import User
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
        fields = ["class_number", "course", "semester", "lecturer", "student"]


class CollegeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDay
        fields = ["date", "classes", "student"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

        extra_kwarg = {'password': {
            'write_only': True,
            'required': True
        }}
    def create(selfself, validated_data):
        user = User.objects.create_user(**validated_data)
        return user