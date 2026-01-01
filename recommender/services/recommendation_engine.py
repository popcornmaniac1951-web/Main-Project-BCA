from ..models import Career, Interest, Skill

def recommend_careers(interests, skills, education_level, preferred_work_type):
    """
    AI Logic: Rule-based recommendation engine.
    Matches user interests and skills against available Career objects.
    Returns a queryset of recommended careers.
    """
    # 1. Start with careers matching preferred work type
    recommendations = Career.objects.filter(work_type=preferred_work_type)
    
    # If no exact work type match, use all careers as base
    if not recommendations.exists():
        recommendations = Career.objects.all()

    # 2. Scoring System
    scored_careers = []
    
    for career in recommendations:
        score = 0
        
        # Match Interests (Strong signal)
        career_interests = set(career.interests.all())
        matching_interests = career_interests.intersection(interests)
        # Each matching interest adds 20 points
        score += len(matching_interests) * 20
        
        # Match Skills (Direct matching)
        career_skills = set(career.skills.all())
        matching_skills = career_skills.intersection(skills)
        
        # Calculate Match % for Skills
        if career_skills:
            match_percentage = (len(matching_skills) / len(career_skills)) * 100
        else:
            match_percentage = 0
            
        # Add skill matching to score
        score += len(matching_skills) * 10
        
        # If there's at least some interest or skill match
        if score > 0 or match_percentage > 50:
            # Store match percentage for display if needed
            career.match_percentage = round(match_percentage, 1)
            scored_careers.append((career, score))

    # 3. Sort by score descending
    scored_careers.sort(key=lambda x: x[1], reverse=True)
    
    # Return top 5 careers
    return [c[0] for c in scored_careers[:5]]
