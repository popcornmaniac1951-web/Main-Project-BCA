from django.db import models
from django.contrib.auth.models import User
import json

class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True) # e.g., Technical, Soft Skill

    def __str__(self):
        return self.name

class Career(models.Model):
    WORK_TYPE_CHOICES = [
        ('Office', 'Office'),
        ('Remote', 'Remote'),
        ('Field', 'Field'),
        ('Research', 'Research'),
    ]
    
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    interests = models.ManyToManyField(Interest, related_name='careers')
    skills = models.ManyToManyField(Skill, through='CareerSkillWeight', related_name='careers')
    future_scope = models.TextField()
    salary_range = models.CharField(max_length=100) # e.g., "$50,000 - $80,000"
    recommended_courses = models.TextField(help_text="Comma separated course names or links")
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES, default='Office')
    
    # Personalization Enhancements (Soft Skills & Preferences)
    work_style = models.CharField(max_length=50, choices=[('Team', 'Team'), ('Solo', 'Solo')], default='Team')
    creativity_level = models.IntegerField(default=5) # scale 1-10
    leadership_interest = models.BooleanField(default=False)
    stress_tolerance = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium')

    def __str__(self):
        return self.title

class CareerSkillWeight(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    weight = models.FloatField(default=1.0) # Importance (1.0 to 10.0)

    class Meta:
        unique_together = ('career', 'skill')

    def __str__(self):
        return f"{self.career.title} - {self.skill.name} ({self.weight})"

class CareerRoadmap(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='roadmaps')
    level = models.CharField(max_length=50) # Entry-level, Mid-level, Senior
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.career.title} - {self.level}: {self.title}"

class UserRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    selected_interests = models.ManyToManyField(Interest)
    selected_skills = models.ManyToManyField(Skill)
    education_level = models.CharField(max_length=100)
    preferred_work_type = models.CharField(max_length=50)
    
    # New logic storage
    recommended_careers = models.ManyToManyField(Career)
    results_json = models.TextField(blank=True, help_text="Stored scoring, reasoning and gap analysis")
    
    created_at = models.DateTimeField(auto_now_add=True)
    feedback_given = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"
    
    @property
    def results_data(self):
        if not self.results_json:
            return []
        try:
            data = json.loads(self.results_json)
            # Normalization pass
            for item in data:
                if 'career_id' in item:
                    try:
                        item['career_id'] = int(item['career_id'])
                    except (ValueError, TypeError):
                        pass
            return data
        except:
            return []

class UserFeedback(models.Model):
    recommendation = models.OneToOneField(UserRecommendation, on_delete=models.CASCADE, related_name='feedback')
    is_helpful = models.BooleanField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Business', 'Business'),
        ('Medical', 'Medical'),
        ('Arts', 'Arts'),
        ('Government', 'Government'),
    ]
    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=255)
    description = models.TextField() # Full Overview
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    duration = models.CharField(max_length=50) # e.g., "8 Weeks"
    
    # Detailed Info
    what_you_will_learn = models.TextField(help_text="One learning point per line")
    prerequisites = models.TextField(blank=True, help_text="One prerequisite per line")
    recommended_background = models.TextField(blank=True)
    tools_covered = models.CharField(max_length=255, help_text="Comma separated tools")
    
    # Relationships
    related_careers = models.ManyToManyField(Career, related_name='courses')
    
    def __str__(self):
        return self.title

    @property
    def learning_points(self):
        return [p.strip() for p in self.what_you_will_learn.split('\n') if p.strip()]

    @property
    def prerequisite_list(self):
        return [p.strip() for p in self.prerequisites.split('\n') if p.strip()]

class CourseStep(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField() # 1, 2, 3, 4
    title = models.CharField(max_length=100) # e.g., Foundation Skills
    description = models.TextField()
    
    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"{self.course.title} - Step {self.step_number}: {self.title}"
