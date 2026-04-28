from django.contrib import admin
from .models import HeroImage, HomeVideo, AIAdvantagePage, TheSystemPage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage, ReadyForTestPage, TestBeforeTrustPage

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ["active", "created_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Image", {
            "fields": ("image",)
        }),
        ("Hero Text Content", {
            "fields": ("main_heading", "button_text", "subtitle")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ["video_type", "active", "created_at"]
    list_filter = ["active", "video_type"]
    fieldsets = (
        ("Video Thumbnail", {
            "fields": ("thumbnail",)
        }),
        ("Video Content", {
            "fields": ("video_type", "youtube_url", "uploaded_video")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )


@admin.register(AIAdvantagePage)
class AIAdvantagePageAdmin(admin.ModelAdmin):
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("subtitle",)
        }),
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2")
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


@admin.register(TheSystemPage)
class TheSystemPageAdmin(admin.ModelAdmin):
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("highlight_1", "highlight_2")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3", "line_4")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3", "line_4", "line_5", "line_6")
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
    list_display = ["active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3", "line_4", "line_5", "line_6")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type")
        }),
        ("Career Paths Image", {
            "fields": ("image",)
        }),
        ("Left Career Path (Software Development)", {
            "fields": ("youtube_url_1", "uploaded_video_1")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3")
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
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("line_1", "line_2", "line_3", "line_4")
        }),
        ("Video Section", {
            "fields": ("video_thumbnail", "video_title", "video_type")
        }),
        ("Preview Buttons Videos", {
            "fields": ("youtube_url_1", "uploaded_video_1", "youtube_url_2", "uploaded_video_2", "youtube_url_3", "uploaded_video_3")
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
