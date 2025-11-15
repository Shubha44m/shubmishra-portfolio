from django.core.management.base import BaseCommand
from main.models import Profile, Education, SkillCategory, Skill, Experience, Project, Certification, Achievement

class Command(BaseCommand):
    help = 'Load initial data for Shubham Mishra portfolio'
    
    def handle(self, *args, **options):
        self.stdout.write("Loading initial data for Shubham Mishra portfolio...")
        
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name="Shubham Mishra",
            defaults={
                'email': 'mishrashubham3322@gmail.com',
                'phone': '+91 73900 56662',
                'location': 'Uttar Pradesh, India',
                'github_url': 'https://github.com/ShubhamMishra',
                'linkedin_url': 'https://linkedin.com/in/shubham-mishra',
                'career_objective': 'Motivated and enthusiastic developer with experience in Python, Web development and real-time AI/Computer Vision prototyping using OpenCV and MediaPipe.'
            }
        )
        if created:
            self.stdout.write(f"✓ Created profile: {profile.name}")
        
        # Create Education
        education, created = Education.objects.get_or_create(
            institution="Shri Ramswaroop Memorial University",
            degree="B.Tech - Computer Science",
            duration="2022-2026",
            achievements="Smart India Hackathon Participant"
        )
        if created:
            self.stdout.write(f"✓ Created education: {education.institution}")
        
        # Create Skill Categories and Skills
        categories_skills = {
            'Languages': ['Python'],
            'Frameworks': ['Django', 'FastAPI', 'Flask'],
            'Frontend/UI': ['HTML', 'CSS', 'UI/UX Basics'],
            'AI/CV Tools': ['OpenCV', 'MediaPipe', 'NumPy'],
            'Tools': ['Git', 'GitHub', 'VS Code']
        }
        
        for category_name, skills in categories_skills.items():
            category, created = SkillCategory.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(f"✓ Created skill category: {category_name}")
            
            for skill_name in skills:
                skill, created = Skill.objects.get_or_create(name=skill_name, category=category)
                if created:
                    self.stdout.write(f"  ✓ Added skill: {skill_name}")
        
        # Create Experience
        experience, created = Experience.objects.get_or_create(
            title="AI / Computer Vision Project Work",
            duration="Freelance + Academic",
            description="Built multiple CV prototypes using Python, OpenCV, and MediaPipe. Worked on gesture recognition, face detection, and real-time video processing."
        )
        if created:
            self.stdout.write(f"✓ Created experience: {experience.title}")
        
        # Create Projects
        projects_data = [
            {
                'title': "VR Try-On Model",
                'description': "Real-time try-on system overlaying outfits on user clothing. Used MediaPipe Pose for skeletal landmarks + OpenCV for masking transformation. NumPy used for scaling, alignment warping operations.",
                'technologies': "Python, OpenCV, MediaPipe, NumPy",
                'github_url': 'https://github.com/ShubhamMishra/vr-try-on',
                'is_featured': True
            },
            {
                'title': "Tasty Bites",
                'description': "Full-stack restaurant website for table reservations food ordering. Built using HTML, CSS, JavaScript, Django, Python backend. Adding authentication (login/signup) for production-ready workflow.",
                'technologies': "Django, Python, HTML, CSS, JavaScript",
                'github_url': 'https://github.com/ShubhamMishra/tasty-bites',
                'live_url': '#',
                'is_featured': True
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f"✓ Created project: {project.title}")
        
        # Create Certifications
        certifications = [
            ("Basics of Python", "2025"),
            ("HP Life – AI for Beginners", ""),
            ("ChatGPT AI Fundamentals", "2025"),
            ("NCAT Certification", ""),
            ("Smart India Hackathon – Project Selection", "")
        ]
        
        for name, year in certifications:
            cert, created = Certification.objects.get_or_create(name=name, year=year)
            if created:
                self.stdout.write(f"✓ Created certification: {name}")
        
        # Create Achievements
        achievement, created = Achievement.objects.get_or_create(
            title="Smart India Hackathon",
            description="Selected prototype in national level hackathon"
        )
        if created:
            self.stdout.write(f"✓ Created achievement: {achievement.title}")
        
        self.stdout.write(
            self.style.SUCCESS('✅ Successfully loaded all initial data for Shubham Mishra portfolio!')
        )