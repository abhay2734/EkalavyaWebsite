from django.contrib import admin
from .models import Slider, HomeVideo, FunnelStep, AIAdvantagePage, SkillTestPage, LearningSystemPage, CareerRoadmapPage, CareerCapsulesPage, LanguageBarrierPage


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "active", "created_at"]
    list_filter = ["active"]
    list_editable = ["order", "active"]


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
            "fields": ("title", "subtitle", "description", "image")
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
            "fields": ("title", "subtitle", "description", "image")
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
            "fields": ("title", "subtitle", "description", "image")
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
            "fields": ("title", "subtitle", "description", "image")
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
            "fields": ("title", "subtitle", "description", "image")
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
    list_display = ["title", "video_title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section Content", {
            "fields": ("title", "subtitle", "description", "image")
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
