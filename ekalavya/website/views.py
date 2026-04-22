from django.shortcuts import render
from .models import HeroImage, HomeVideo, FunnelStep, AIAdvantagePage, TheSystemPage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage, ReadyForTestPage, TestBeforeTrustPage


def home(request):
    hero_image = HeroImage.objects.filter(active=True).first()
    video = HomeVideo.objects.filter(active=True).first()
    funnel_steps = FunnelStep.objects.filter(active=True).order_by("order")

    ai_advantage_page = AIAdvantagePage.objects.filter(active=True).first()
    the_system_page = TheSystemPage.objects.filter(active=True).first()
    skill_test_page = SkillTestPage.objects.filter(active=True).first()
    learning_system_page = LearningSystemPage.objects.filter(active=True).first()
    career_roadmap_page = CareerRoadmapPage.objects.filter(active=True).first()
    career_capsules_page = CareerCapsulesPage.objects.filter(active=True).first()
    language_barrier_page = LanguageBarrierPage.objects.filter(active=True).first()
    ready_for_test_page = ReadyForTestPage.objects.filter(active=True).first()
    test_before_trust_page = TestBeforeTrustPage.objects.filter(active=True).first()

    context = {
        "hero_image": hero_image,
        "video": video,
        "funnel_steps": funnel_steps,
        "ai_advantage_page": ai_advantage_page,
        "the_system_page": the_system_page,
        "skill_test_page": skill_test_page,
        "learning_system_page": learning_system_page,
        "career_roadmap_page": career_roadmap_page,
        "career_capsules_page": career_capsules_page,
        "language_barrier_page": language_barrier_page,
        "ready_for_test_page": ready_for_test_page,
        "test_before_trust_page": test_before_trust_page,
    }

    return render(request, "home.html", context)
