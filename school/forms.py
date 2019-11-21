from django import forms

from .models import Career, Subject, Professor, Student, Grade, Absences


class CareerCreationForm(forms.ModelForm):

    class Meta:
        model = Career
        fields = ('name', 'code', 'subjects')


class SubjectCreationForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'code', 'subject_type', 'professors')


class SubjectEditForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'code', 'subject_type', 'professors', 'students')


class ProfessorCreationForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('code', )


class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('code', 'careers')


class GradeCreationForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = ('student', 'date', 'grade')


class GradeEditForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = ('date', 'grade')


class AbsenceCreationForm(forms.ModelForm):

    class Meta:
        model = Absences
        fields = ('student', 'date', 'absence')


class AbsenceEditForm(forms.ModelForm):

    class Meta:
        model = Absences
        fields = ('date', 'absence')
