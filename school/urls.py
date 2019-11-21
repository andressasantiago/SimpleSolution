from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # Admin views
    url(r'^careers/$', views.career_list, name='careers_list'),
    url(r'^careers/create/$', views.career_create, name='career_create'),
    path('careers/<int:career_id>/', views.career_detail, name='career_detail'),
    path('careers/<int:career_id>/edit/', views.career_edit, name='career_edit'),

    url(r'^subjects/$', views.subject_list, name='subjects_list'),
    url(r'^subjects/create/$', views.subject_create, name='subject_create'),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subjects/<int:subject_id>/edit/', views.subject_edit, name='subject_edit'),

    url(r'^professors/$', views.professor_list, name='professors_list'),
    path('professors/<int:professor_id>/', views.professor_detail, name='professor_detail'),
    path('professors/<int:professor_id>/edit/', views.professor_edit, name='professor_edit'),

    url(r'^students/$', views.student_list, name='students_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/edit/', views.student_edit, name='student_edit'),

    path('admins/<int:admin_id>/', views.admin_detail, name='admin_detail'),
    path('admins/<int:admin_id>/edit/', views.admin_edit, name='admin_edit'),

    # Professor views
    path('professors/subjects/', views.professor_subjects_list, name='professor_subjects_list'),
    path('professors/subjects/<int:subject_id>/', views.professor_subject_detail, name='professor_subject_detail'),
    path('professor/subjects/<int:subject_id>/grade/', views.professor_grade_create, name='professor_grade_create'),
    path('professor/subjects/grade/<int:grade_id>/edit/', views.professor_grade_edit, name='professor_grade_edit'),
    path('absences/', views.absences_list, name='absences_list'),
    path('absences/create/', views.absence_create, name='absence_create'),
    path('absences/student/<int:student_id>/', views.student_absences_detail, name='student_absences_detail'),
    path('absences/<int:absence_id>/edit/', views.absence_edit, name='absence_edit'),

    # Student views
    path('student/subjects/', views.student_subjects_list, name='student_subjects_list'),
    path('student/subjects/<int:subject_id>/', views.student_subject_details, name='student_subject_details'),
    path('student/absences/', views.student_absences_list, name='student_absences_list'),
]
