from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ParticipantProfileEditForm, OrganizerProfileEditForm
from .models import ParticipantProfile, OrganizerProfile


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вход произведен успешно!')
                else:
                    return HttpResponse('Аккаунт неактивен!')
            else:
                return HttpResponse('Пароль и/или логин неверны!')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def participant_register(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST)
        profile_form = ParticipantProfileEditForm(
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            ParticipantProfile.objects.create(user=new_user)
            profile_form.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserEditForm()
        profile_form = ParticipantProfileEditForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def organizer_register(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST)
        profile_form = OrganizerProfileEditForm(
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            OrganizerProfile.objects.create(user=new_user)
            profile_form.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserEditForm()
        profile_form = OrganizerProfileEditForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def edit_participant(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ParticipantProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ParticipantProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def edit_organizer(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = OrganizerProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = OrganizerProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
