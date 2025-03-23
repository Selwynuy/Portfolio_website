# portfolio/views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project, SkillCategory, Timeline


def home(request):
    # Fetch data for the about section
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    timeline_events = Timeline.objects.all().order_by('-date')

    # Fetch projects
    projects = Project.objects.all()

    # Debug: Print data to console
    print("Skill Categories:", skill_categories)
    for category in skill_categories:
        print(f"Category: {category.name}, Skills: {category.skills.all()}")

    print("Timeline Events:", timeline_events)

    context = {
        'skill_categories': skill_categories,
        'timeline_events': timeline_events,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        send_mail(
            f"Message from {name}",
            message,
            email,
            ["selwyn.uy@msugensan.edu.ph"],
            fail_silently=False,
        )

        return redirect("")

    return render(request, "portfolio/contact.html")
