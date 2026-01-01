from django import forms
from .models import Interest, Skill, Career

class RecommendationForm(forms.Form):
    EDUCATION_CHOICES = [
        ('High School', 'High School'),
        ('Bachelor\'s', 'Bachelor\'s'),
        ('Master\'s', 'Master\'s'),
        ('PhD', 'PhD'),
        ('Diploma', 'Diploma'),
    ]
    
    WORK_STYLE_CHOICES = [('Team', 'Team'), ('Solo', 'Solo')]
    STRESS_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]

    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Select areas you are interested in"
    )
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().order_by('category'),
        widget=forms.CheckboxSelectMultiple,
        help_text="Select skills you possess"
    )
    education_level = forms.ChoiceField(choices=EDUCATION_CHOICES)
    preferred_work_type = forms.ChoiceField(choices=Career.WORK_TYPE_CHOICES)
    
    # Personalization Enhancements
    work_style = forms.ChoiceField(choices=WORK_STYLE_CHOICES, label="Work Style Preference")
    creativity_level = forms.IntegerField(min_value=1, max_value=10, initial=5, label="Creativity Level (1-10)")
    leadership_interest = forms.BooleanField(required=False, label="Interested in Leadership Roles?")
    stress_tolerance = forms.ChoiceField(choices=STRESS_CHOICES, label="Stress Tolerance Level")
