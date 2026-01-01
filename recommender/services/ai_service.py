from ..models import Career, Interest, Skill, CareerSkillWeight
import json

class CareerAI:
    @staticmethod
    def calculate_score(career, user_interests, user_skills, personalization_data):
        """
        Calculates a weighted score for a career based on user profile.
        Returns (score, reasoning, skill_gaps)
        """
        score = 0
        reasoning = []
        
        # 1. Interest Matching (Max 30 points)
        career_interests = career.interests.all()
        if career_interests:
            matching_interests = career_interests.filter(id__in=[i.id for i in user_interests])
            interest_score = (matching_interests.count() / career_interests.count()) * 30
            score += interest_score
            if matching_interests.exists():
                reasoning.append(f"Matches your interest in: {', '.join([i.name for i in matching_interests])}.")
        
        # 2. Weighted Skill Matching (Max 50 points)
        career_skill_weights = CareerSkillWeight.objects.filter(career=career)
        total_weight = sum(sw.weight for sw in career_skill_weights)
        
        user_skill_ids = [s.id for s in user_skills]
        matched_weight = 0
        matching_skills = []
        missing_skills = []
        
        for sw in career_skill_weights:
            if sw.skill.id in user_skill_ids:
                matched_weight += sw.weight
                matching_skills.append(sw.skill.name)
            else:
                missing_skills.append(sw.skill.name)
        
        if total_weight > 0:
            skill_score = (matched_weight / total_weight) * 50
            score += skill_score
            if matching_skills:
                reasoning.append(f"You have key skills like {', '.join(matching_skills[:3])} which are highly valued here.")
        
        # 3. Personalization & Soft Skills (Max 20 points)
        personal_score = 0
        if career.work_type == personalization_data.get('preferred_work_type'):
            personal_score += 5
            reasoning.append(f"Fits your preference for {career.work_type} work.")
            
        if career.work_style == personalization_data.get('work_style'):
            personal_score += 5
            reasoning.append(f"Matches your {career.work_style} work style.")
            
        # Creativity match (within 2 points)
        if abs(career.creativity_level - personalization_data.get('creativity_level', 5)) <= 2:
            personal_score += 5
            reasoning.append("The creativity level required aligns with your profile.")
            
        if career.stress_tolerance == personalization_data.get('stress_tolerance'):
            personal_score += 5
            reasoning.append(f"Aligns with your {career.stress_tolerance} stress tolerance.")
            
        # 4. Education Alignment (Base 5 points)
        user_edu = personalization_data.get('education_level', '')
        personal_score += 5
        reasoning.append(f"Mapped against your {user_edu} qualification.")
            
        score += personal_score

        # 5. Course Recommendations
        from ..models import Course
        recommended_courses = Course.objects.filter(related_careers=career).values_list('title', flat=True)[:3]
        
        return {
            'career_id': career.id,
            'career_title': career.title,
            'score': round(score, 1),
            'reasoning': " ".join(reasoning),
            'matching_skills': matching_skills,
            'skill_gaps': missing_skills,
            'readiness_score': round((matched_weight / total_weight * 100) if total_weight > 0 else 0, 1),
            'dash_offset': round(440 * (1 - (matched_weight / total_weight if total_weight > 0 else 0))),
            'recommended_courses': list(recommended_courses)
        }

def get_recommendations(interests, skills, personalization_data):
    """
    Main entry point for AI recommendations.
    """
    careers = Career.objects.all()
    results = []
    
    for career in careers:
        analysis = CareerAI.calculate_score(career, interests, skills, personalization_data)
        if analysis['score'] > 20: # Minimum threshold to recommend
            results.append(analysis)
    
    # Sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return results[:5] # Return top 5
