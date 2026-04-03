from django.db import models


class Slider(models.Model):

    title = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to="sliders/")

    order = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        if self.title:
            return self.title
        return f"Slider {self.id}"



class HomeVideo(models.Model):

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    title = models.CharField(max_length=200, blank=True)

    thumbnail = models.ImageField(upload_to="video_thumbnails/")

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(blank=True)

    uploaded_video = models.FileField(
        upload_to="homepage_videos/",
        blank=True,
        null=True
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return self.title
        return "Homepage Video"


class FunnelStep(models.Model):
    """Dynamic funnel steps that can be managed through Django admin"""

    STEP_TYPE_CHOICES = [
        ("clarity", "Clarity Entry"),
        ("challenge", "Challenge"),
        ("conversion", "Conversion"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    button_text = models.CharField(max_length=200)

    button_url = models.URLField(blank=True, help_text="URL for the button (e.g., /clarity-50/)")

    step_type = models.CharField(
        max_length=20,
        choices=STEP_TYPE_CHOICES,
        default="clarity"
    )

    order = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.get_step_type_display()}: {self.title}"


class AIAdvantagePage(models.Model):
    """Dynamic AI Fear vs AI Advantage page content"""

    title = models.CharField(max_length=200, default="AI Fear vs AI Advantage")

    subtitle = models.CharField(
        max_length=300,
        default="AI is not replacing people — it is empowering those who learn how to use it."
    )

    description = models.TextField(
        default="We are living in a powerful technological shift. Many people fear that artificial intelligence will replace them, while others are learning how to use it as a tool to grow faster. The difference is not intelligence or talent — it is clarity and direction."
    )

    image = models.ImageField(
        upload_to="ai_advantage/",
        help_text="Main image for the AI Advantage section"
    )

    video_title = models.CharField(max_length=200, default="Who Controls AI?")

    video_thumbnail = models.ImageField(
        upload_to="ai_advantage/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL (e.g., https://www.youtube.com/watch?v=...)"
    )

    uploaded_video = models.FileField(
        upload_to="ai_advantage/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AI Advantage Page"
        verbose_name_plural = "AI Advantage Page"

    def __str__(self):
        return self.title


class SkillTestPage(models.Model):
    """Dynamic Skill Test page content"""

    title = models.CharField(max_length=200, default="Skill Test")

    subtitle = models.CharField(
        max_length=300,
        default="Test your skills and knowledge"
    )

    description = models.TextField(
        default="Assess your abilities and understand where you stand."
    )

    image = models.ImageField(
        upload_to="skill_test/",
        help_text="Main image for the Skill Test section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="skill_test/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL"
    )

    uploaded_video = models.FileField(
        upload_to="skill_test/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill Test Page"
        verbose_name_plural = "Skill Test Page"

    def __str__(self):
        return self.title


class CareerRoadmapPage(models.Model):
    """Dynamic Career Roadmap page content"""

    title = models.CharField(max_length=200, default="Career Roadmap")

    subtitle = models.CharField(
        max_length=300,
        default="Every successful career begins with a clear path"
    )

    description = models.TextField(
        default="This roadmap provides a simple and structured journey from zero knowledge to industry readiness."
    )

    image = models.ImageField(
        upload_to="career_roadmap/",
        help_text="Main image for the Career Roadmap section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="career_roadmap/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL"
    )

    uploaded_video = models.FileField(
        upload_to="career_roadmap/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Career Roadmap Page"
        verbose_name_plural = "Career Roadmap Page"

    def __str__(self):
        return self.title


class LanguageBarrierPage(models.Model):
    """Dynamic Language Barrier page content"""

    title = models.CharField(max_length=200, default="Language Barrier")

    subtitle = models.CharField(
        max_length=300,
        default="Overcome communication challenges"
    )

    description = models.TextField(
        default="Break through language barriers in your career."
    )

    image = models.ImageField(
        upload_to="language_barrier/",
        help_text="Main image for the Language Barrier section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="language_barrier/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL"
    )

    uploaded_video = models.FileField(
        upload_to="language_barrier/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Language Barrier Page"
        verbose_name_plural = "Language Barrier Page"

    def __str__(self):
        return self.title


class CareerCapsulesPage(models.Model):
    """Dynamic Career Capsules page content"""

    title = models.CharField(max_length=200, default="Career Capsules")

    subtitle = models.CharField(
        max_length=300,
        default="Short, focused career insights"
    )

    description = models.TextField(
        default="Quick lessons to boost your career growth."
    )

    image = models.ImageField(
        upload_to="career_capsules/",
        help_text="Main image for the Career Capsules section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="career_capsules/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL"
    )

    uploaded_video = models.FileField(
        upload_to="career_capsules/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Career Capsules Page"
        verbose_name_plural = "Career Capsules Page"

    def __str__(self):
        return self.title


class LearningSystemPage(models.Model):
    """Dynamic Learning System page content"""

    title = models.CharField(max_length=200, default="Learning System")

    subtitle = models.CharField(
        max_length=300,
        default="Learn the right way"
    )

    description = models.TextField(
        default="Master the skills you need for your career."
    )

    image = models.ImageField(
        upload_to="learning_system/",
        help_text="Main image for the Learning System section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="learning_system/thumbnails/",
        help_text="Video thumbnail image"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_type = models.CharField(
        max_length=10,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube"
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL"
    )

    uploaded_video = models.FileField(
        upload_to="learning_system/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Learning System Page"
        verbose_name_plural = "Learning System Page"

    def __str__(self):
        return self.title
