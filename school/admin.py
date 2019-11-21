from django.contrib import admin
from .models import Career, Subject, Professor, Student, Grade


class StudentAdmin(admin.ModelAdmin):
    list_display = ['profile', 'code']


class CareerAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'subject_type']


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['profile', 'code']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade_creator', 'student', 'subject', 'date', 'grade']


admin.site.register(Grade, GradeAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Student, StudentAdmin)
