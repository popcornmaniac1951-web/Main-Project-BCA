from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import UserRecommendation, Career, Interest, Skill, Course
from .recommender_forms import RecommendationForm
from .services.recommendation_engine import recommend_careers

from .services.ai_service import get_recommendations
import json

from django.db.models import Q

def home(request):
    return render(request, 'recommender/home.html')

def search_view(request):
    query = request.GET.get('q', '')
    careers = []
    courses = []
    
    if query:
        careers = Career.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        courses = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    return render(request, 'recommender/search_results.html', {
        'query': query,
        'careers': careers,
        'courses': courses
    })

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()
    return render(request, 'recommender/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'recommender/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def dashboard(request):
    recommendations = UserRecommendation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'recommender/dashboard.html', {'recommendations': recommendations})

@login_required
def recommend_view(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            interests = form.cleaned_data['interests']
            skills = form.cleaned_data['skills']
            education_level = form.cleaned_data['education_level']
            preferred_work_type = form.cleaned_data['preferred_work_type']
            
            personalization_data = {
                'preferred_work_type': preferred_work_type,
                'work_style': form.cleaned_data['work_style'],
                'creativity_level': form.cleaned_data['creativity_level'],
                'leadership_interest': form.cleaned_data['leadership_interest'],
                'stress_tolerance': form.cleaned_data['stress_tolerance'],
            }
            
            # Use AI logic to get careers
            results = get_recommendations(interests, skills, personalization_data)
            
            # Save recommendation
            user_rec = UserRecommendation.objects.create(
                user=request.user,
                education_level=education_level,
                preferred_work_type=preferred_work_type,
                results_json=json.dumps(results)
            )
            user_rec.selected_interests.set(interests)
            user_rec.selected_skills.set(skills)
            
            # For backward compatibility and generic access, still set the M2M careers
            career_ids = [r['career_id'] for r in results]
            user_rec.recommended_careers.set(Career.objects.filter(id__in=career_ids))
            
            return redirect('result', pk=user_rec.pk)
    else:
        form = RecommendationForm()
    
    return render(request, 'recommender/recommend.html', {
        'form': form,
        'interests': Interest.objects.all(),
        'skills': Skill.objects.all().order_by('category')
    })

@login_required
def result_view(request, pk):
    recommendation = get_object_or_404(UserRecommendation, pk=pk, user=request.user)
    results = recommendation.results_data
    
    # Enrich results with database objects
    for res in results:
        career_obj = None
        cid = res.get('career_id')
        ctitle = res.get('career_title')
        
        if cid:
            career_obj = Career.objects.filter(id=cid).first()
        if not career_obj and ctitle:
            career_obj = Career.objects.filter(title=ctitle).first()
        
        res['career'] = career_obj
        
    return render(request, 'recommender/result.html', {
        'recommendation': recommendation,
        'results': results
    })

@login_required
def delete_recommendation(request, pk):
    recommendation = get_object_or_404(UserRecommendation, pk=pk, user=request.user)
    if request.method == 'POST':
        recommendation.delete()
        messages.success(request, "Recommendation deleted successfully.")
        return redirect('dashboard')
    return redirect('dashboard')

@login_required
def submit_feedback(request, pk):
    if request.method == 'POST':
        from .models import UserFeedback
        recommendation = UserRecommendation.objects.get(pk=pk, user=request.user)
        is_helpful = request.POST.get('is_helpful') == 'true'
        comments = request.POST.get('comments', '')
        
        UserFeedback.objects.update_or_create(
            recommendation=recommendation,
            defaults={'is_helpful': is_helpful, 'comments': comments}
        )
        recommendation.feedback_given = True
        recommendation.save()
        
        messages.success(request, "Thank you for your feedback!")
        return redirect('result', pk=pk)
    return redirect('dashboard')

def about(request):
    return render(request, 'recommender/about.html')

def contact(request):
    return render(request, 'recommender/contact.html')

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'recommender/courses.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'recommender/course_detail.html', {'course': course})
