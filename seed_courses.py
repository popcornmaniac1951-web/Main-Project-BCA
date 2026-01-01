import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_recommender.settings')
django.setup()

from recommender.models import Course, CourseStep, Career

def seed_courses():
    # Clear existing
    Course.objects.all().delete()
    
    courses_data = [
        # TECHNOLOGY
        {
            "title": "AI & Machine Learning Specialization",
            "category": "Technology",
            "difficulty": "Advanced",
            "duration": "16 Weeks",
            "short_description": "Architect intelligent systems using deep learning and neural network protocols.",
            "description": "Master the mathematical foundations and architectural patterns of modern AI. From convolutional neural networks to large language models, this course prepares you for high-stakes AI engineering roles in the global tech sector.",
            "what_you_will_learn": "Neural Network Architecture\nDeep Learning Optimization\nNatural Language Processing (NLP)\nComputer Vision Systems\nMLOps and Deployment Scaling",
            "prerequisites": "Advanced Python Proficiency\nLinear Algebra and Calculus\nBasic Statistics",
            "tools_covered": "TensorFlow, PyTorch, CUDA, Docker, Kubernetes",
            "career_keyword": "AI Engineer"
        },
        {
            "title": "Cybersecurity Defensive Operations",
            "category": "Technology",
            "difficulty": "Intermediate",
            "duration": "10 Weeks",
            "short_description": "Protect critical infrastructure through advanced threat hunting and incident response.",
            "description": "Learn the art of digital defense. This course covers security operations center (SOC) protocols, forensic analysis, and proactive threat mitigation strategies to secure enterprise environments against malicious actors.",
            "what_you_will_learn": "Threat Vector Analysis\nIncident Response Frameworks\nNetwork Security Monitoring\nForensic Data Recovery\nCompliance & Risk Assessment",
            "prerequisites": "Foundational Networking Knowledge\nBasic Linux Administration\nUnderstanding of Virtualization",
            "tools_covered": "Wireshark, Splunk, Metasploit, Kali Linux, Nessus",
            "career_keyword": "Cybersecurity Analyst"
        },
        {
            "title": "Cloud Architecture & DevOps Mastery",
            "category": "Technology",
            "difficulty": "Advanced",
            "duration": "14 Weeks",
            "short_description": "Build and scale resilient cloud-native infrastructures for global applications.",
            "description": "Deep dive into distributed systems and continuous delivery. Learn to architect highly available cloud environments and automate development workflows using industry-standard DevOps tools and practices.",
            "what_you_will_learn": "Infrastructure as Code (IaC)\nCI/CD Pipeline Automation\nCloud Identity & Access Management\nServerless Architecture\nDistributed Database Scaling",
            "prerequisites": "Intermediate Linux Networking\nBasic Scripting (Python/Bash)\nAWS or Azure Fundamentals",
            "tools_covered": "Terraform, Ansible, AWS, Jenkins, Docker",
            "career_keyword": "Software Architect"
        },
        {
            "title": "Full-Stack Web Engineering",
            "category": "Technology",
            "difficulty": "Intermediate",
            "duration": "12 Weeks",
            "short_description": "Develop high-performance, secure web applications from database to interface.",
            "description": "A comprehensive journey through the modern web stack. Learn to build responsive frontends and robust backends, focusing on performance, security, and seamless user experiences for modern SaaS platforms.",
            "what_you_will_learn": "RESTful API Development\nState Management (Redux/Context)\nDatabase Schema Design\nFrontend Performance Optimization\nWeb Security Best Practices",
            "prerequisites": "HTML/CSS Fundamentals\nBasic JavaScript Syntax\nUnderstanding of the DOM",
            "tools_covered": "React, Node.js, PostgreSQL, MongoDB, Vite",
            "career_keyword": "Web Developer"
        },
        {
            "title": "Quantum Computing Fundamentals",
            "category": "Technology",
            "difficulty": "Advanced",
            "duration": "8 Weeks",
            "short_description": "Explore the next frontier of computation through quantum algorithms and qubits.",
            "description": "Understand the logic behind quantum supremacy. This course introduces you to superposition, entanglement, and the algorithms that will redefine encryption, materials science, and cryptography in the next decade.",
            "what_you_will_learn": "Quantum Circuit Design\nShor's and Grover's Algorithms\nQubit State Manipulation\nQuantum Error Correction\nHybrid Classical-Quantum Systems",
            "prerequisites": "Linear Algebra Mastery\nProbability Theory\nIntroductory Physics",
            "tools_covered": "Qiskit, Cirq, IBM Quantum Lab, PennyLane",
            "career_keyword": "Data Scientist"
        },
        {
            "title": "UX/UI Design for SaaS Platforms",
            "category": "Technology",
            "difficulty": "Beginner",
            "duration": "8 Weeks",
            "short_description": "Create intuitive, high-conversion interfaces for modern software-as-a-service products.",
            "description": "Focus on user-centric design principles. Learn to translate complex business requirements into elegant, functional designs while mastering the industry's most powerful prototyping and collaboration tools.",
            "what_you_will_learn": "User Research Methodologies\nWireframing and Prototyping\nDesign Systems Architecture\nAccessibility Standards (WCAG)\nInteraction Design Protocols",
            "prerequisites": "Basic Visual Literacy\nInterest in Human-Computer Interaction\nProblem-Solving Mindset",
            "tools_covered": "Figma, Adobe XD, Storybook, Miro",
            "career_keyword": "UI/UX Designer"
        },
        # MEDICAL
        {
            "title": "Digital Health & Telemedicine Protocols",
            "category": "Medical",
            "difficulty": "Intermediate",
            "duration": "6 Weeks",
            "short_description": "Implement and manage remote patient care systems in the modern healthcare era.",
            "description": "Bridge the gap between technology and patient care. Learn to navigate the legal, ethical, and technical requirements of remote consultations and wearable health data integration.",
            "what_you_will_learn": "Telehealth Platform Management\nPatient Privacy (HIPAA) Compliance\nRemote Diagnostic Procedures\nHealth Data Interoperability\nVirtual Patient Interaction Tactics",
            "prerequisites": "Basic Medical Terminology\nFamiliarity with Healthcare Regulations\nBasic Computer Literacy",
            "tools_covered": "Epic EHR, Doxy.me, Zoom for Healthcare, MyChart",
            "career_keyword": "Doctor"
        },
        {
            "title": "Biomedical Equipment Maintenance",
            "category": "Medical",
            "difficulty": "Beginner",
            "duration": "12 Weeks",
            "short_description": "Ensure the operational integrity of critical medical imaging and support systems.",
            "description": "Gain the technical skills required to calibrate, repair, and maintain sophisticated medical machinery, ranging from patient monitors to advanced MRI and CT scanners.",
            "what_you_will_learn": "Electronic Circuit Analysis\nMechanical Calibration Techniques\nMedical Device Safety Testing\nPredictive Maintenance Logic\nInventory & Spare Parts Management",
            "prerequisites": "High School Physics\nMechanical Aptitude\nBasic Electronics Interest",
            "tools_covered": "Oscilloscopes, Multimeters, Calibration Software",
            "career_keyword": "Lab Technician"
        },
        {
            "title": "Clinical Data Management",
            "category": "Medical",
            "difficulty": "Intermediate",
            "duration": "10 Weeks",
            "short_description": "Organize and secure clinical trial data for pharmaceutical and research success.",
            "description": "Master the lifecycle of clinical data. Learn to design case report forms, manage clinical databases, and ensure data quality and integrity for regulatory submission and medical breakthroughs.",
            "what_you_will_learn": "Clinical Database Design\nData Cleaning & Validation\nRegulatory Standard Compliance (GCP)\nElectronic Data Capture (EDC)\nStatistical Safety Analysis",
            "prerequisites": "Basic Biology Knowledge\nIntroductory Statistics\nAttention to Detail",
            "tools_covered": "Oracle Clinical, Medidata Rave, SQL, R",
            "career_keyword": "Pharmacist"
        },
        {
            "title": "Genetic Counseling & Ethics",
            "category": "Medical",
            "difficulty": "Advanced",
            "duration": "14 Weeks",
            "short_description": "Navigate the complex landscape of genomic data and ethical patient guidance.",
            "description": "Prepare for the frontier of personalized medicine. Learn to interpret complex genomic reports and communicate life-altering information to patients with empathy, accuracy, and ethical rigor.",
            "what_you_will_learn": "Genomic Sequence Interpretation\nEthical Decision Making Models\nPsychological Support Techniques\nInheritance Pattern Analysis\nVariant Classification Systems",
            "prerequisites": "Advanced Genetics Background\nClinical Experience Preferred\nCommunication Skills",
            "tools_covered": "ClinVar, IGV, Genomic Databases, Patient CRM",
            "career_keyword": "Doctor"
        },
        # BUSINESS
        {
            "title": "Strategic Leadership in Tech",
            "category": "Business",
            "difficulty": "Advanced",
            "duration": "10 Weeks",
            "short_description": "Lead high-growth organizations through innovation and digital transformation.",
            "description": "Develop the executive mindset. Focus on organizational design, product-market fit, and scaling culture in rapidly evolving technological industries.",
            "what_you_will_learn": "Organizational Architecture\nChange Management Protocols\nStrategic Financial Planning\nInnovation Cycle Management\nExecutive Communication Matrix",
            "prerequisites": "Prior Management Experience\nBusiness Fundamentals\nAnalytical Thinking",
            "tools_covered": "Jira, Salesforce, Power BI, Slack, Asana",
            "career_keyword": "Manager"
        },
        {
            "title": "Agile Project Management (Scrum/Kanban)",
            "category": "Business",
            "difficulty": "Beginner",
            "duration": "8 Weeks",
            "short_description": "Master the frameworks for iterative development and high-velocity team output.",
            "description": "Eliminate waste and increase value. Learn the ceremonies, roles, and artifacts of Scrum and Kanban to lead teams toward sustainable and predictable project success.",
            "what_you_will_learn": "Scrum Framework Mastery\nKanban Flow Visualization\nBacklog Grooming & Prioritization\nSprint Planning & Velocity Tracking\nServant Leadership Principles",
            "prerequisites": "Critical Thinking\nCollaboration Aptitude\nLogical Reasoning",
            "tools_covered": "Trello, Monday.com, Jira, Confluence, ClickUp",
            "career_keyword": "Business Analyst"
        },
        {
            "title": "Venture Capital & Startup Growth",
            "category": "Business",
            "difficulty": "Intermediate",
            "duration": "12 Weeks",
            "short_description": "Evaluate investment opportunities and scale disruptive startups to global markets.",
            "description": "Learn the mechanics of the venture ecosystem. From cap table management to growth hacking, this course covers the journey from seed-stage idea to IPO-ready organization.",
            "what_you_will_learn": "Valuation Methodologies\nTerm Sheet Negotiation\nGo-to-Market (GTM) Strategy\nUnit Economics Analysis\nPitch Deck Architecture",
            "prerequisites": "Financial Literacy\nMarket Analysis Basics\nStrategic Thinking",
            "tools_covered": "Excel, PitchBook, Crunchbase, Capdesk",
            "career_keyword": "Entrepreneur"
        },
        {
            "title": "Corporate Sustainability & ESG Reporting",
            "category": "Business",
            "difficulty": "Intermediate",
            "duration": "8 Weeks",
            "short_description": "Drive value through environmental, social, and governance (ESG) compliance.",
            "description": "Align corporate goals with global responsibility. Learn to measure and report on sustainability metrics that modern investors and regulators increasingly demand.",
            "what_you_will_learn": "Carbon Accounting Principles\nGlobal Reporting Initiative (GRI)\nSustainable Supply Chain Logic\nESG Data Visualization\nRegulatory Compliance Frameworks",
            "prerequisites": "Sustainability Interest\nData Analysis Basics\nPolicy Understanding",
            "tools_covered": "Tableau, SAP S/4HANA, ESG Dashboards",
            "career_keyword": "Marketing Strategist"
        },
        # ARTS
        {
            "title": "Cinematic 3D Animation & VFX",
            "category": "Arts",
            "difficulty": "Intermediate",
            "duration": "18 Weeks",
            "short_description": "Create hyper-realistic characters and visual effects for film and interactive media.",
            "description": "From modeling to rendering, master the pipeline of modern digital arts. Learn the technical rigor required to create convincing characters and breathtaking environments.",
            "what_you_will_learn": "3D Modeling & Sculpting\nRigging & Kinematics\nDynamic Particle Simulation\nLighting & Photorealistic Rendering\nCompositing and Post-Production",
            "prerequisites": "Basic Artistic Sense\nFamiliarity with 3D Space\nAttention to Detail",
            "tools_covered": "Maya, Houdini, ZBrush, Nuke, Arnold",
            "career_keyword": "Art Skills" # Fallback if specific career missing
        },
        {
            "title": "AI-Driven Content Strategy",
            "category": "Arts",
            "difficulty": "Beginner",
            "duration": "6 Weeks",
            "short_description": "Optimize digital storytelling and narrative reach using AI analytical tools.",
            "description": "Master the intersection of creativity and data. Learn to use AI to identify audience trends, generate content ideas, and optimize narrative performance across digital channels.",
            "what_you_will_learn": "Narrative Data Analysis\nGenerative AI for Ideation\nSEO and Semantic Content Logic\nMultichannel Distribution Strategy\nAudience Persona Modeling",
            "prerequisites": "Strong Written Communication\nCreative Imagination\nBasic Web Literacy",
            "tools_covered": "ChatGPT, Jasper, Google Analytics, Canva",
            "career_keyword": "Marketing Strategist"
        },
        {
            "title": "Sound Design for Interactive Media",
            "category": "Arts",
            "difficulty": "Intermediate",
            "duration": "10 Weeks",
            "short_description": "Architect immersive auditory experiences for games and virtual environments.",
            "description": "Learn the physics and psychology of sound. From foley recording to spatial audio implementation, this course prepares you for high-level audio engineering roles in gaming and VR.",
            "what_you_will_learn": "Spatial Audio Implementation\nFoley and Sound Synthesis\nDAW Workflow Optimization\nInteractive Music Systems\nGame Engine Audio Integration",
            "prerequisites": "Basic Musicality\nUnderstanding of Sound Physics\nLogical Reasoning",
            "tools_covered": "Ableton Live, Wwise, FMOD, Unity Audio",
            "career_keyword": "Art Skills"
        },
        {
            "title": "Modern Fine Arts & Digital Integration",
            "category": "Arts",
            "difficulty": "Beginner",
            "duration": "8 Weeks",
            "short_description": "Bridge traditional fine art techniques with digital tools and NFT ecosystems.",
            "description": "Expand your canvas. Learn to translate traditional skills into digital formats, exploring the new frontiers of digital ownership and generative art while maintaining fine art integrity.",
            "what_you_will_learn": "Digital Painting Techniques\nGenerative Art Algorithims\nCrypto-Art Ecosystem Logic\nDigital Gallery Curation\nHybrid Media Experimentation",
            "prerequisites": "Drawing/Painting Ability\nAesthetic Sense\nOpenness to Technology",
            "tools_covered": "Procreate, Photoshop, Blender, OpenSea",
            "career_keyword": "Art Skills"
        },
        # GOVERNMENT
        {
            "title": "Public Policy & Legislative Analysis",
            "category": "Government",
            "difficulty": "Advanced",
            "duration": "12 Weeks",
            "short_description": "Analyze complex legal frameworks and architect data-driven public policies.",
            "description": "Understand the mechanics of governance. Learn to evaluate legislative effectiveness, manage stakeholder interests, and design policies that address societal challenges at scale.",
            "what_you_will_learn": "Legislative Research Methods\nSocial Impact Assessment\nBudgetary Analysis Protocols\nStakeholder Management Matrix\nPublic Advocacy Strategy",
            "prerequisites": "Strong Analytical Skills\nWriting for Government\nLegal Fundamentals",
            "tools_covered": "LexisNexis, Westlaw, STATA, Policy Databases",
            "career_keyword": "Government Skills"
        },
        {
            "title": "Crisis Management & Civil Defense",
            "category": "Government",
            "difficulty": "Intermediate",
            "duration": "10 Weeks",
            "short_description": "Lead government responses to large-scale emergencies and infrastructure failures.",
            "description": "Prepare for the unexpected. Learn the command structures, communication protocols, and resource allocation strategies required to maintain order and safety during critical crises.",
            "what_you_will_learn": "Emergency Operations Center (EOC) Logic\nIncident Command Systems\nPublic Information Protocols\nDisaster Recovery Management\nCritical Infrastructure Protection",
            "prerequisites": "Decision Making Under Pressure\nLeadership Aptitude\nCommunication Skills",
            "tools_covered": "WebEOC, GIS Mapping, Communications Systems",
            "career_keyword": "Government Skills"
        },
        {
            "title": "Diplomatic Protocols & International Relations",
            "category": "Government",
            "difficulty": "Intermediate",
            "duration": "14 Weeks",
            "short_description": "Navigate global power dynamics and architect bilateral cooperation agreements.",
            "description": "Master the art of negotiation on the world stage. Learn the formal protocols, negotiation tactics, and geopolitical theories that drive international stability and cooperation.",
            "what_you_will_learn": "Bilateral Negotiation Tactics\nFormal Diplomatic Etiquette\nGeopolitical Conflict Resolution\nInternational Law Frameworks\nCross-Cultural Communication",
            "prerequisites": "Interest in Global Affairs\nPublic Speaking\nEthical Responsibility",
            "tools_covered": "Diplomatic Databases, Translation Tools, UN Protocols",
            "career_keyword": "Government Skills"
        }
    ]

    for cdata in courses_data:
        # Match related career
        kword = cdata.pop('career_keyword')
        rel_careers = Career.objects.filter(title__icontains=kword)
        if not rel_careers.exists():
            # Try searching interests if title match fails
            rel_careers = Career.objects.filter(interests__name__icontains=kword)
        
        course = Course.objects.create(**cdata)
        if rel_careers.exists():
            course.related_careers.add(rel_careers.first())

        # Create 4 steps for each course
        CourseStep.objects.create(course=course, step_number=1, title="Foundation Building", description="Core theoretical grounding and initial system calibration.")
        CourseStep.objects.create(course=course, step_number=2, title="Conceptual Deep-Dive", description="Advanced technical exploration and logic implementation.")
        CourseStep.objects.create(course=course, step_number=3, title="Applied Strategic Laboratory", description="Hands-on execution of real-world scenarios and protocols.")
        CourseStep.objects.create(course=course, step_number=4, title="Career Readiness Finalization", description="Portfolio verification and high-level architectural review for market entry.")

    print(f"Successfully seeded {len(courses_data)} professional courses and their learning roadmaps.")

if __name__ == "__main__":
    seed_courses()
