from django.contrib import admin
from .models import HeroImage, HomeVideo, FunnelStep, AIAdvantagePage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage, ReadyForTestPage, TestBeforeTrustPage


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
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

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


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
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(SkillTestPage)
class SkillTestPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(LearningSystemPage)
class LearningSystemPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(CareerRoadmapPage)
class CareerRoadmapPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(CareerCapsulesPage)
class CareerCapsulesPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(LanguageBarrierPage)
class LanguageBarrierPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Career Paths Image", {
            "fields": ("video_thumbnail",)
        }),
        ("Left Career Path (Software Development)", {
            "fields": ("video_type", "youtube_url_1", "uploaded_video_1")
        }),
        ("Center Career Path (Data & AI)", {
            "fields": ("youtube_url_2", "uploaded_video_2")
        }),
        ("Right Career Path (Design & UX)", {
            "fields": ("youtube_url_3", "uploaded_video_3")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(ReadyForTestPage)
class ReadyForTestPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(TestBeforeTrustPage)
class TestBeforeTrustPageAdmin(admin.ModelAdmin):
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    class Media:
        js = ("js/admin_video_toggle.js",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
