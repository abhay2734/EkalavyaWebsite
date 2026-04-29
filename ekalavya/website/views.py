import re

from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import HeroImage, HomeVideo, AIAdvantage, TheSystem, ConceptualCommunication, ThirtyMinutes, ITAspirant, ZeroToIndustry, CareerPaths, ReadyForTestPage, TestBeforeTrustPage


def home(request):
    hero_image = HeroImage.objects.filter(active=True).first()
    if hero_image:
        hero_heading = hero_image.main_heading.replace(
            "Complete Transformation",
            "Complete<br><span class=\"hero-highlight\">Self</span>-Transformation"
        )
        hero_heading = mark_safe(hero_heading)

        hero_subtitle = hero_image.subtitle
        hero_subtitle = re.sub(
            r"\b([Ss])ingle\b",
            r"<span class=\"hero-highlight\">S</span>ingle",
            hero_subtitle,
            flags=re.IGNORECASE,
        )
        hero_subtitle = re.sub(
            r"\b([Ss])tructured\b",
            r"<span class=\"hero-highlight\">S</span>tructured",
            hero_subtitle,
            flags=re.IGNORECASE,
        )
        hero_subtitle = mark_safe(hero_subtitle)
    else:
        hero_heading = None
        hero_subtitle = None

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

    def highlight_it_aspirant_text(text: str) -> str:
        if not text:
            return text
        text = re.sub(
            r"(Candidates fail in job)",
            r"<span class=\"hero-highlight\">\1</span>",
            text,
            flags=re.IGNORECASE,
        )
        text = re.sub(
            r"(what they know)\.?",
            r"<span class=\"hero-highlight\">\1</span>.",
            text,
            flags=re.IGNORECASE,
        )
        return text

    it_aspirant_line_1_html = None
    it_aspirant_line_2_html = None
    it_aspirant_line_3_html = None
    it_aspirant_line_4_html = None

    if career_roadmap_page:
        it_aspirant_line_1_html = mark_safe(highlight_it_aspirant_text(career_roadmap_page.line_1))
        it_aspirant_line_2_html = mark_safe(highlight_it_aspirant_text(career_roadmap_page.line_2))
        it_aspirant_line_3_html = mark_safe(highlight_it_aspirant_text(career_roadmap_page.line_3))
        it_aspirant_line_4_html = mark_safe(highlight_it_aspirant_text(career_roadmap_page.line_4))

    context = {
        "hero_image": hero_image,
        "hero_heading_html": hero_heading,
        "hero_subtitle_html": hero_subtitle,
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
        "it_aspirant_line_1_html": it_aspirant_line_1_html,
        "it_aspirant_line_2_html": it_aspirant_line_2_html,
        "it_aspirant_line_3_html": it_aspirant_line_3_html,
        "it_aspirant_line_4_html": it_aspirant_line_4_html,
    }

    return render(request, "home.html", context)
