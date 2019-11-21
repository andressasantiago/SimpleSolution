from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from collections import defaultdict

from .models import Career, Subject, Professor, Student, Grade, Absences

from .forms import CareerCreationForm, SubjectCreationForm, ProfessorCreationForm, StudentCreationForm,\
    SubjectEditForm, GradeCreationForm, GradeEditForm, AbsenceCreationForm, AbsenceEditForm

from account.forms import ProfileEditForm, UserEditForm
from account.models import Profile


@staff_member_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student/list.html', {'section': 'students',
                                                        'students': students})


@staff_member_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'school/student/detail.html', {'section': 'students',
                                                          'student': student})


@staff_member_required
def admin_detail(request, admin_id):
    admin = get_object_or_404(User, pk=admin_id)
    return render(request, 'school/admin/detail.html', {'section': 'users',
                                                        'admin': admin})


@staff_member_required
def admin_edit(request, admin_id):
    try:
        if request.method == 'POST':
            admin = get_object_or_404(User, pk=admin_id)
            user_form = UserEditForm(request.POST, instance=admin)
            profile = Profile.objects.get(pk=admin.profile.pk)
            profile_form = ProfileEditForm(request.POST, instance=profile)

            if profile_form.is_valid() and user_form.is_valid():
                profile_form.save()
                user_form.save()
                return redirect('admin_detail', admin_id=admin_id)

        else:
            admin = get_object_or_404(User, pk=admin_id)
            profile = Profile.objects.get(pk=admin.profile.pk)
            profile_form = ProfileEditForm(instance=profile)
            user_form = UserEditForm(instance=admin)

        return render(request, 'school/admin/edit.html', {'section': 'users',
                                                          'profile_form': profile_form,
                                                          'user_form': user_form})
    except Exception:
        return redirect('admin_detail', admin_id=admin_id)


@staff_member_required
def student_edit(request, student_id):
    try:
        if request.method == 'POST':
            student = get_object_or_404(Student, pk=student_id)
            student_form = StudentCreationForm(request.POST, instance=student)
            profile = Profile.objects.get(pk=student.profile.pk)
            profile_form = ProfileEditForm(request.POST, instance=profile)
            user_form = UserEditForm(request.POST, instance=profile.user)

            if student_form.is_valid() and profile_form.is_valid() and user_form.is_valid():
                student_form.save()
                profile_form.save()
                user_form.save()
                return redirect('student_detail', student_id=student_id)

        else:
            student = get_object_or_404(Student, pk=student_id)
            student_form = StudentCreationForm(instance=student)
            profile = Profile.objects.get(pk=student.profile.pk)
            profile_form = ProfileEditForm(instance=profile)
            user_form = UserEditForm(instance=profile.user)

        return render(request, 'school/student/edit.html', {'section': 'students',
                                                            'student_form': student_form,
                                                            'profile_form': profile_form,
                                                            'user_form': user_form})
    except Exception:
        return redirect('students_list')


@staff_member_required
def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'school/professors/list.html', {'section': 'professors',
                                                           'professors': professors})


@staff_member_required
def professor_detail(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    return render(request, 'school/professors/detail.html', {'section': 'professors',
                                                             'professor': professor})


@staff_member_required
def professor_edit(request, professor_id):
    try:
        if request.method == 'POST':
            professor = get_object_or_404(Professor, pk=professor_id)
            professor_form = ProfessorCreationForm(request.POST, instance=professor)
            profile = Profile.objects.get(pk=professor.profile.pk)
            profile_form = ProfileEditForm(request.POST, instance=profile)
            user_form = UserEditForm(request.POST, instance=profile.user)

            if professor_form.is_valid() and profile_form.is_valid() and user_form.is_valid():
                professor_form.save()
                profile_form.save()
                user_form.save()
                return redirect('professor_detail', professor_id=professor_id)

        else:
            professor = get_object_or_404(Professor, pk=professor_id)
            professor_form = ProfessorCreationForm(instance=professor)
            profile = Profile.objects.get(pk=professor.profile.pk)
            profile_form = ProfileEditForm(instance=profile)
            user_form = UserEditForm(instance=profile.user)

        return render(request, 'school/professors/edit.html', {'section': 'professors',
                                                               'professor_form': professor_form,
                                                               'profile_form': profile_form,
                                                               'user_form': user_form})
    except Exception:
        return redirect('professors_list')


@staff_member_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'school/subject/list.html', {'section': 'subjects',
                                                        'subjects': subjects})


@staff_member_required
def subject_create(request):
    if request.method == 'POST':
        subject_form = SubjectCreationForm(request.POST)

        if subject_form.is_valid():
            subject_form.save()
            return redirect('subjects_list')
    else:
        subject_form = SubjectCreationForm()

    return render(request, 'school/subject/create.html', {'section': 'subjects',
                                                          'subject_form': subject_form})


@staff_member_required
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'school/subject/detail.html', {'section': 'subjects',
                                                          'subject': subject})


@staff_member_required
def subject_edit(request, subject_id):
    try:
        if request.method == 'POST':
            subject = get_object_or_404(Subject, pk=subject_id)
            subject_form = SubjectEditForm(request.POST, instance=subject)

            if subject_form.is_valid():
                subject_form.save()
                return redirect('subject_detail', subject_id=subject_id)

        else:
            subject = get_object_or_404(Subject, pk=subject_id)
            subject_form = SubjectEditForm(instance=subject)
            subject_form.fields['students'].queryset = Student.objects.filter(careers__in=subject.career_set.all())

        return render(request, 'school/subject/edit.html', {'section': 'subjects',
                                                            'subject_form': subject_form})
    except Exception:
        return redirect('subjects_list')


@staff_member_required
def career_list(request):
    careers = Career.objects.all()
    return render(request, 'school/career/list.html', {'section': 'careers',
                                                       'careers': careers})


@staff_member_required
def career_create(request):
    if request.method == 'POST':
        career_form = CareerCreationForm(request.POST)

        if career_form.is_valid():
            career_form.save()
            return redirect('careers_list')
    else:
        career_form = CareerCreationForm()

    return render(request, 'school/career/create.html', {'section': 'careers',
                                                         'career_form': career_form})


@staff_member_required
def career_detail(request, career_id):
    career = get_object_or_404(Career, pk=career_id)
    return render(request, 'school/career/detail.html', {'section': 'careers',
                                                         'career': career})


@staff_member_required
def career_edit(request, career_id):
    try:
        if request.method == 'POST':
            career = get_object_or_404(Career, pk=career_id)
            career_form = CareerCreationForm(request.POST, instance=career)
            if career_form.is_valid():
                career_form.save()
                return redirect('career_detail', career_id=career_id)

        else:
            career = get_object_or_404(Career, pk=career_id)
            career_form = CareerCreationForm(instance=career)

        return render(request, 'school/career/edit.html', {'section': 'careers',
                                                           'career_form': career_form})
    except Exception:
        return redirect('careers_list')


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def professor_subjects_list(request):
    user = User.objects.get(pk=request.user.pk)
    professor = Professor.objects.filter(profile=user.profile)[0]
    subjects = professor.subject_set.all()
    return render(request, 'school/professors/subjects/list.html', {'section': 'subjects',
                                                                    'subjects': subjects})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def professor_subject_detail(request, subject_id):
    user = User.objects.get(pk=request.user.pk)
    professor = Professor.objects.filter(profile=user.profile)[0]
    subject = professor.subject_set.filter(pk=subject_id)
    if subject:
        subject = subject[0]
        return render(request, 'school/professors/subjects/detail.html', {'section': 'subjects',
                                                                          'subject': subject})
    else:
        return redirect('professor_subjects_list')


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def professor_grade_create(request, subject_id):
    professor = Professor.objects.filter(profile=request.user.profile)[0]
    subject = professor.subject_set.filter(pk=subject_id)
    if subject:
        subject = subject[0]

        if request.method == 'POST':
            grade_form = GradeCreationForm(request.POST)

            if grade_form.is_valid():
                grade = grade_form.save(commit=False)
                grade.grade_creator = request.user.profile
                grade.subject = subject
                grade.save()
                return redirect('professor_subject_detail', subject_id=subject_id)
        else:
            grade_form = GradeCreationForm()
            grade_form.fields['student'].queryset = subject.students.all()
            if subject.subject_type == Subject.PROFESORADO:
                grade_form.fields['grade'].choices = Grade.GRADES_PROFESORADO
            elif subject.subject_type == Subject.SEMINARIO:
                grade_form.fields['grade'].choices = Grade.GRADES_SEMINAR

        return render(request, 'school/professors/grades/create.html', {'section': 'subjects',
                                                                        'subject': subject,
                                                                        'grade_form': grade_form})
    else:
        return redirect('professor_subjects_list')


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def professor_grade_edit(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    professor = Professor.objects.filter(profile=request.user.profile)[0]
    subject = professor.subject_set.filter(pk=grade.subject.pk)
    if subject:
        subject = subject[0]

        if request.method == 'POST':
            if '_method' in request._post and request._post['_method'] == 'delete':
                grade.delete()
                return redirect('professor_subject_detail', subject_id=subject.pk)
            else:
                grade_form = GradeEditForm(request.POST, instance=grade)

                if grade_form.is_valid():
                    grade = grade_form.save(commit=False)
                    grade.grade_creator = request.user.profile
                    grade.save()
                    return redirect('professor_subject_detail', subject_id=grade.subject.pk)
        else:
            grade_form = GradeEditForm(instance=grade)
            if subject.subject_type == Subject.PROFESORADO:
                grade_form.fields['grade'].choices = Grade.GRADES_PROFESORADO
            elif subject.subject_type == Subject.SEMINARIO:
                grade_form.fields['grade'].choices = Grade.GRADES_SEMINAR

        return render(request, 'school/professors/grades/edit.html', {'section': 'subjects',
                                                                      'subject': subject,
                                                                      'grade_form': grade_form})
    else:
        return redirect('professor_subjects_list')


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.STUDENT)
def student_subjects_list(request):
    user = User.objects.get(pk=request.user.pk)
    student = Student.objects.filter(profile=user.profile)[0]
    subjects = student.subject_set.all()
    return render(request, 'school/student/subjects/list.html', {'section': 'subjects',
                                                                 'subjects': subjects})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.STUDENT)
def student_subject_details(request, subject_id):
    user = User.objects.get(pk=request.user.pk)
    student = Student.objects.filter(profile=user.profile)[0]
    subject = student.subject_set.filter(pk=subject_id)
    if subject:
        subject = subject[0]
        return render(request, 'school/student/subjects/detail.html', {'section': 'subjects',
                                                                       'subject': subject,
                                                                       'student': student})
    else:
        return redirect('student_subjects_list')


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def absences_list(request):
    absences = Absences.objects.all()
    # Dict to count the total absences of the student
    absences_dict = defaultdict(float)
    # Dict to store the pk of the students to redirect to students absences details
    students_pk_dict = dict()
    for absence in absences:
        students_pk_dict[str(absence.student)] = absence.student.pk
        absences_dict[str(absence.student)] += float(absence.absence)

    absence_data_list = list()
    for student_name in absences_dict:
        absence_data_list.append({'student_name': str(student_name), 'absences': absences_dict[student_name],
                                  'student_id': students_pk_dict[str(student_name)]})
    return render(request, 'school/absences/list.html', {'section': 'absences',
                                                         'absences_list': absence_data_list})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def absence_create(request):
    if request.method == 'POST':
        absence_form = AbsenceCreationForm(request.POST)

        if absence_form.is_valid():
            absence = absence_form.save(commit=False)
            absence.absence_creator = request.user.profile
            absence.save()
            return redirect('absences_list')

    else:
        absence_form = AbsenceCreationForm()

    return render(request, 'school/absences/create.html', {'section': 'absences',
                                                           'absence_form': absence_form})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def student_absences_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'school/absences/student/detail.html', {'section': 'absences',
                                                                   'student': student})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.PROFESSOR)
def absence_edit(request, absence_id):
    absence = get_object_or_404(Absences, pk=absence_id)

    if request.POST:
        if '_method' in request._post and request._post['_method'] == 'delete':
            absence.delete()
            return redirect('student_absences_detail', student_id=absence.student.pk)

        absence_form = AbsenceEditForm(request.POST, instance=absence)

        if absence_form.is_valid():
            absence = absence_form.save(commit=False)
            absence.absence_creator = request.user.profile
            absence.save()
            return redirect('student_absences_detail', student_id=absence.student.pk)
    else:
        absence_form = AbsenceEditForm(instance=absence)

    return render(request, 'school/absences/edit.html', {'section': 'absences',
                                                         'absence_form': absence_form})


@login_required
@user_passes_test(lambda user: user.profile.profile_type == Profile.STUDENT)
def student_absences_list(request):
    student = get_object_or_404(Student, profile=request.user.profile)
    absences = student.absences_set.all()
    total_absences = {'total': 0.0}
    for absence in absences:
        total_absences['total'] += float(absence.absence)

    return render(request, 'school/student/absences/list.html', {'section': 'absences',
                                                                 'total_absences': total_absences,
                                                                 'student': student})
