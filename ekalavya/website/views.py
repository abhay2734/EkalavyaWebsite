from django.shortcuts import render
from .models import HeroImage, HomeVideo, AIAdvantage, TheSystem, ConceptualCommunication, ThirtyMinutes, ITAspirant, ZeroToIndustry, CareerPaths, ReadyForTestPage, TestBeforeTrustPage


def home(request):
    hero_image = HeroImage.objects.filter(active=True).first()
    video = HomeVideo.objects.filter(active=True).first()

    ai_advantage_page = AIAdvantage.objects.filter(active=True).first()
    the_system_page = TheSystem.objects.filter(active=True).first()
    skill_test_page = ConceptualCommunication.objects.filter(active=True).first()
    learning_system_page = ThirtyMinutes.objects.filter(active=True).first()
    career_roadmap_page = ITAspirant.objects.filter(active=True).first()
    career_capsules_page = ZeroToIndustry.objects.filter(active=True).first()
    language_barrier_page = CareerPaths.objects.filter(active=True).first()
    ready_for_test_page = ReadyForTestPage.objects.filter(active=True).first()
    test_before_trust_page = TestBeforeTrustPage.objects.filter(active=True).first()

    context = {
        "hero_image": hero_image,
        "video": video,
        "ai_advantage_page": ai_advantage_page,
        "the_system_page": the_system_page,
        "conceptual_communication_page": skill_test_page,
        "thirty_minutes_page": learning_system_page,
        "it_aspirant_page": career_roadmap_page,
        "zero_to_industry_page": career_capsules_page,
        "career_paths_page": language_barrier_page,
        "ready_for_test_page": ready_for_test_page,
        "test_before_trust_page": test_before_trust_page,
    }

    return render(request, "home.html", context)
