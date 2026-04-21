from django.shortcuts import render
from .models import HeroImage, HomeVideo, FunnelStep, AIAdvantagePage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage, ReadyForTestPage, TestBeforeTrustPage


def home(request):

    sliders = HeroImage.objects.filter(active=True).order_by("id")

    video = HomeVideo.objects.filter(active=True).first()

    funnel_steps = FunnelStep.objects.filter(active=True).order_by("order")

    context = {
        "sliders": sliders,
        "video": video,
        "funnel_steps": funnel_steps,
    }

    return render(request, "home.html", context)


def ai_advantage(request):
    ai_advantage_page = AIAdvantagePage.objects.filter(active=True).first()
    
    context = {
        "ai_advantage_page": ai_advantage_page,
    }
    
    return render(request, "ai_advantage.html", context)


def skill_test(request):
    skill_test_page = SkillTestPage.objects.filter(active=True).first()
    
    context = {
        "skill_test_page": skill_test_page,
    }
    
    return render(request, "skill_test.html", context)


def learning_system(request):
    learning_system_page = LearningSystemPage.objects.filter(active=True).first()
    
    context = {
        "learning_system_page": learning_system_page,
    }
    
    return render(request, "learning_system.html", context)


def career_roadmap(request):
    career_roadmap_page = CareerRoadmapPage.objects.filter(active=True).first()
    
    context = {
        "career_roadmap_page": career_roadmap_page,
    }
    
    return render(request, "career_roadmap.html", context)


def career_capsules(request):
    career_capsules_page = CareerCapsulesPage.objects.filter(active=True).first()
    
    context = {
        "career_capsules_page": career_capsules_page,
    }
    
    return render(request, "career_capsules.html", context)


def language_barrier(request):
    language_barrier_page = LanguageBarrierPage.objects.filter(active=True).first()
    
    context = {
        "language_barrier_page": language_barrier_page,
    }
    
    return render(request, "language_barrier.html", context)
