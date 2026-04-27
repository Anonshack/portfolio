from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils import translation
from django.conf import settings as django_settings
from .forms import RegisterForm, LoginForm, ReviewForm
from .models import Review, Project


def home(request):
    reviews = Review.objects.filter(is_approved=True)
    projects = Project.objects.filter(is_active=True)
    review_form = ReviewForm()
    return render(request, 'portfolio_app/index1.html', {
        'reviews': reviews,
        'projects': projects,
        'review_form': review_form,
        'user': request.user,
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _('Registration successful! Welcome!'))
            return redirect('home')
        else:
            messages.error(request, _('Please fix the errors below.'))
    else:
        form = RegisterForm()
    return render(request, 'portfolio_app/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('Welcome back!'))
            return redirect('home')
        else:
            messages.error(request, _('Invalid username or password.'))
    else:
        form = LoginForm()
    return render(request, 'portfolio_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, _('You have been logged out.'))
    return redirect('home')


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            if not review.full_name:
                review.full_name = request.user.get_full_name() or request.user.username
            review.save()
            messages.success(request, _('Your review has been posted!'))
        else:
            messages.error(request, _('Please fix the errors.'))
    return redirect('home')


def set_language_view(request):
    if request.method == 'POST':
        lang = request.POST.get('language', 'uz')
        next_url = request.POST.get('next', '/')

        available_langs = [code for code, name in django_settings.LANGUAGES]
        if lang not in available_langs:
            lang = 'uz'

        translation.activate(lang)
        response = redirect(next_url)
        response.set_cookie(
            'django_language',
            lang,
            max_age=365 * 24 * 60 * 60,
            path='/',
            samesite='Lax',
        )
        return response
    return redirect('/')