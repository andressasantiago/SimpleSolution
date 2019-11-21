from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from .forms import UserRegistrationForm, ProfileRegistrationForm

from .models import Profile

from school.models import Professor, Student


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@staff_member_required
def user_list(request):
    admins = User.objects.filter(is_active=True, is_staff=True)
    admins_with_profile = []
    for admin in admins:
        if hasattr(admin, 'profile'):
            admins_with_profile.append(admin)

    professors = Professor.objects.all()
    students = Student.objects.all()
    return render(request, 'account/user/list.html', {'section': 'users',
                                                      'admins': admins_with_profile,
                                                      'professors': professors,
                                                      'students': students})


@staff_member_required
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])

            if profile_form.cleaned_data['profile_type'] == Profile.ADMIN:
                new_user.is_staff = True

            # Save objects
            new_user.save()

            # Create the user profile
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()

            if profile.profile_type == profile.PROFESSOR:
                professor = Professor.objects.create(profile=profile)
                return redirect('professor_detail', professor_id=professor.pk)

            if profile.profile_type == profile.STUDENT:
                student = Student.objects.create(profile=profile)
                return redirect('student_detail', student_id=student.pk)

            return redirect('users_list')

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form,
                                                     'profile_form': profile_form})
