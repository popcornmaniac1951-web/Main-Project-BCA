from recommender.models import Interest, Skill, Career

def seed():
    # Helper to create/get Interest
    def get_interest(name):
        obj, _ = Interest.objects.get_or_create(name=name)
        return obj

    # Helper to create/get Skill
    def get_skill(name, category):
        obj, _ = Skill.objects.update_or_create(name=name, defaults={'category': category})
        return obj

    # 1. Domains (Interests)
    tech = get_interest("Technology")
    medical = get_interest("Medical")
    business = get_interest("Business")
    arts = get_interest("Arts")
    government = get_interest("Government")

    # 2. Tech Skills
    tech_skills = ["Programming", "Problem Solving", "Analytical Thinking", "Logical Reasoning", 
                   "System Design", "Data Analysis", "Debugging", "Algorithmic Thinking", 
                   "UI/UX Design", "Cloud & DevOps Basics", "Cybersecurity Awareness", 
                   "Continuous Learning", "Team Collaboration"]
    t_skills = [get_skill(s, "Technology") for s in tech_skills]

    # 3. Medical Skills
    med_skills = ["Clinical Knowledge", "Attention to Detail", "Critical Thinking", "Observation Skills", 
                  "Emotional Intelligence", "Communication (Patient Interaction)", "Decision Making Under Pressure", 
                  "Ethical Judgment", "Scientific Analysis", "Research Skills", "Empathy & Compassion", 
                  "Time Management"]
    m_skills = [get_skill(s, "Medical") for s in med_skills]

    # 4. Business Skills
    biz_skills = ["Communication", "Leadership", "Strategic Thinking", "Decision Making", 
                  "Financial Literacy", "Market Analysis", "Negotiation", "Problem Solving", 
                  "Sales & Persuasion", "Risk Management", "Team Management", "Presentation Skills"]
    b_skills = [get_skill(s, "Business") for s in biz_skills]

    # 5. Art Skills
    art_skills = ["Creativity", "Visual Thinking", "Design Principles", "Storytelling", 
                  "Artistic Expression", "Imagination", "Communication", "Aesthetic Sense", 
                  "Content Creation", "Attention to Detail", "Adaptability", "Software Tool Proficiency"]
    a_skills = [get_skill(s, "Arts") for s in art_skills]

    # 6. Government Skills
    gov_skills = ["Administrative Skills", "Leadership", "Policy Understanding", "Decision Making", 
                  "Communication", "Ethical Responsibility", "Analytical Thinking", "Problem Solving", 
                  "Public Speaking", "Law & Regulation Knowledge", "Crisis Management", 
                  "Time & Resource Management"]
    g_skills = [get_skill(s, "Government") for s in gov_skills]

    # 7. Update/Create Careers with full skill sets
    
    # TECHNOLOGY ROLES
    roles = [
        ("Software Developer", "Build and maintain software applications.", "Remote", ["Programming", "Debugging", "Problem Solving"]),
        ("Data Scientist", "Extract insights from complex data.", "Remote", ["Data Analysis", "Analytical Thinking", "Programming"]),
        ("AI Engineer", "Develop intelligent systems and models.", "Remote", ["Algorithmic Thinking", "Programming", "System Design"]),
        ("Web Developer", "Create websites and web applications.", "Remote", ["Programming", "UI/UX Design", "Continuous Learning"]),
        ("Cybersecurity Analyst", "Protect systems and networks.", "Office", ["Cybersecurity Awareness", "Analytical Thinking", "Logical Reasoning"])
    ]
    for title, desc, wtype, sklist in roles:
        c, _ = Career.objects.update_or_create(title=title, defaults={'description': desc, 'work_type': wtype, 'salary_range': "$80k - $150k", 'future_scope': "High demand in digital era."})
        c.interests.add(tech)
        for sname in sklist:
            s = Skill.objects.get(name=sname)
            c.skills.add(s)

    # MEDICAL ROLES
    roles = [
        ("Doctor", "Diagnose and treat illnesses.", "Field", ["Clinical Knowledge", "Decision Making Under Pressure", "Ethical Judgment"]),
        ("Nurse", "Provide patient care and support.", "Field", ["Empathy & Compassion", "Communication (Patient Interaction)", "Attention to Detail"]),
        ("Lab Technician", "Conduct medical tests and experiments.", "Office", ["Scientific Analysis", "Observation Skills", "Attention to Detail"]),
        ("Pharmacist", "Dispense medications and advice.", "Office", ["Clinical Knowledge", "Time Management", "Attention to Detail"])
    ]
    for title, desc, wtype, sklist in roles:
        c, _ = Career.objects.update_or_create(title=title, defaults={'description': desc, 'work_type': wtype, 'salary_range': "$60k - $200k+", 'future_scope': "Stable and essential."})
        c.interests.add(medical)
        for sname in sklist:
            s = Skill.objects.get(name=sname)
            c.skills.add(s)

    # BUSINESS ROLES
    roles = [
        ("Business Analyst", "Gap analysis and process improvement.", "Office", ["Market Analysis", "Problem Solving", "Communication"]),
        ("Manager", "Handle operations and people.", "Office", ["Leadership", "Team Management", "Decision Making"]),
        ("Entrepreneur", "Start and grow businesses.", "Remote", ["Risk Management", "Strategic Thinking", "Sales & Persuasion"]),
        ("Marketing Strategist", "Market research and campaigns.", "Remote", ["Market Analysis", "Creativity", "Communication"])
    ]
    for title, desc, wtype, sklist in roles:
        c, _ = Career.objects.update_or_create(title=title, defaults={'description': desc, 'work_type': wtype, 'salary_range': "$70k - $160k", 'future_scope': "Essential for growth."})
        c.interests.add(business)
        for sname in sklist:
            s = Skill.objects.get(name=sname)
            c.skills.add(s)

    print("Database seeded with enterprise data successfully!")

if __name__ == "__main__":
    seed()
