from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from attendance.views import index, course, course_detail, CourseViewSet, semester, semester_detail, SemesterViewSet, \
    lecturer, lecturer_detail, LecturerViewSet, student, student_detail, StudentViewSet, classes, classes_detail, \
    ClassesViewSet, CollegeDayViewSet, collegeday, collegeday_detail, UserViewSet, users

router = DefaultRouter()
router.register('course_viewset', CourseViewSet, 'course_model_viewset')
router.register('semester_viewset', SemesterViewSet, 'semester_model_viewset')
router.register('lecturer_viewset', LecturerViewSet, 'lecturer_model_viewset')
router.register('student_viewset', StudentViewSet, 'student_model_viewset')
router.register('classes_viewset', ClassesViewSet, 'classes_model_viewset')
router.register('collegeday_viewset', CollegeDayViewSet, 'collegeday_model_viewset')
router.register('users', UserViewSet, "users")


urlpatterns = router.urls

urlpatterns.append(path('', index)),

urlpatterns.append(path('course/', course)),
urlpatterns.append(path('course/<int:pk>', course_detail)),

urlpatterns.append(path('semester/', semester)),
urlpatterns.append(path('semester/<int:pk>', semester_detail)),

urlpatterns.append(path('lecturer/', lecturer)),
urlpatterns.append(path('lecturer/<int:pk>', lecturer_detail)),

urlpatterns.append(path('student/', student)),
urlpatterns.append(path('student/<int:pk>', student_detail)),

urlpatterns.append(path('classes/', classes)),
urlpatterns.append(path('classes/<int:pk>', classes_detail)),

urlpatterns.append(path('collegeday/', collegeday)),
urlpatterns.append(path('collegeday/<int:pk>', collegeday_detail)),







