from django.contrib import admin
from .models import Interest, Skill, Career, UserRecommendation, CareerSkillWeight, CareerRoadmap, UserFeedback

class CareerSkillWeightInline(admin.TabularInline):
    model = CareerSkillWeight
    extra = 1

class CareerRoadmapInline(admin.TabularInline):
    model = CareerRoadmap
    extra = 1

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

from django.db.models import Count

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'career_count')
    list_filter = ('category',)
    search_fields = ('name',)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            careers_count=Count('careers')
        )
    
    def career_count(self, obj):
        return obj.careers_count
    career_count.short_description = 'Demand (Careers)'

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_type', 'salary_range', 'work_style', 'times_recommended')
    list_filter = ('work_type', 'work_style', 'stress_tolerance')
    search_fields = ('title', 'description')
    filter_horizontal = ('interests',)
    inlines = [CareerSkillWeightInline, CareerRoadmapInline]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            rec_count=Count('userrecommendation')
        )

    def times_recommended(self, obj):
        return obj.rec_count
    times_recommended.short_description = 'Times Recommended'

@admin.register(UserRecommendation)
class UserRecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'education_level', 'preferred_work_type', 'feedback_given', 'is_helpful')
    list_filter = ('education_level', 'preferred_work_type', 'created_at', 'feedback_given', 'feedback__is_helpful')
    readonly_fields = ('created_at', 'results_json')
    filter_horizontal = ('selected_interests', 'selected_skills', 'recommended_careers')

    def is_helpful(self, obj):
        if hasattr(obj, 'feedback'):
            return obj.feedback.is_helpful
        return "-"
    is_helpful.short_description = 'Helpful?'

@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('recommendation', 'is_helpful', 'created_at')
    list_filter = ('is_helpful', 'created_at')
    readonly_fields = ('created_at',)
