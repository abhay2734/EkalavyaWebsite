from django.contrib import admin
from .models import HeroImage, TopBanner, HomeVideo, FunnelStep, AIAdvantagePage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage, ReadyForTestPage, TestBeforeTrustPage


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ["active", "created_at"]
    list_filter = ["active"]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(TopBanner)
class TopBannerAdmin(admin.ModelAdmin):
    list_display = ["active", "created_at"]
    list_filter = ["active"]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ["title", "video_type", "active", "created_at"]
    list_filter = ["active", "video_type"]


@admin.register(FunnelStep)
class FunnelStepAdmin(admin.ModelAdmin):
    list_display = ["title", "step_type", "order", "active", "created_at"]
    list_filter = ["active", "step_type"]
    list_editable = ["order", "active"]


@admin.register(AIAdvantagePage)
class AIAdvantagePageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(SkillTestPage)
class SkillTestPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(LearningSystemPage)
class LearningSystemPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(CareerRoadmapPage)
class CareerRoadmapPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(CareerCapsulesPage)
class CareerCapsulesPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(LanguageBarrierPage)
class LanguageBarrierPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description", "background_image")
        }),
        ("Video 1 (Left Button)", {
            "fields": ("video_1_title", "video_1_type", "video_1_youtube_url", "video_1_uploaded")
        }),
        ("Video 2 (Center Button)", {
            "fields": ("video_2_title", "video_2_type", "video_2_youtube_url", "video_2_uploaded")
        }),
        ("Video 3 (Right Button)", {
            "fields": ("video_3_title", "video_3_type", "video_3_youtube_url", "video_3_uploaded")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(ReadyForTestPage)
class ReadyForTestPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_title", "video_thumbnail", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(TestBeforeTrustPage)
class TestBeforeTrustPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description", "background_image")
        }),
        ("Video 1 (Left Button)", {
            "fields": ("video_1_title", "video_1_type", "video_1_youtube_url", "video_1_uploaded")
        }),
        ("Video 2 (Center Button)", {
            "fields": ("video_2_title", "video_2_type", "video_2_youtube_url", "video_2_uploaded")
        }),
        ("Video 3 (Right Button)", {
            "fields": ("video_3_title", "video_3_type", "video_3_youtube_url", "video_3_uploaded")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)
