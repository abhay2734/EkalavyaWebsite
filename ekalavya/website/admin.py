from django.contrib import admin
from .models import HeroImage, HomeVideo, AIAdvantage, TheSystem, ConceptualCommunication, ThirtyMinutes, ITAspirant, ZeroToIndustry, CareerPaths, ReadyForTestPage, TestBeforeTrustPage

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ["active", "created_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Image", {
            "fields": ("image",)
        }),
        ("Hero Text Content", {
            "fields": ("main_heading", "button_text", "subtitle", "secondary_subtitle")
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

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(AIAdvantage)
class AIAdvantageAdmin(admin.ModelAdmin):
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ()
        }),
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


@admin.register(TheSystem)
class TheSystemAdmin(admin.ModelAdmin):
    list_display = ["video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Highlight Lines (Card Box)", {
            "fields": ("highlight_1", "highlight_2", "highlight_3")
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


@admin.register(ConceptualCommunication)
class ConceptualCommunicationAdmin(admin.ModelAdmin):
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


@admin.register(ThirtyMinutes)
class ThirtyMinutesAdmin(admin.ModelAdmin):
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


@admin.register(ITAspirant)
class ITAspirantAdmin(admin.ModelAdmin):
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


@admin.register(ZeroToIndustry)
class ZeroToIndustryAdmin(admin.ModelAdmin):
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


@admin.register(CareerPaths)
class CareerPathsAdmin(admin.ModelAdmin):
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
