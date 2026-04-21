from django.db import models


class HeroImage(models.Model):
    """Single hero image for the homepage"""

    image = models.ImageField(upload_to="hero/")

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hero Image"
        verbose_name_plural = "Hero Image"

    def __str__(self):
        return "Hero Image"


class TopBanner(models.Model):
    """Top banner image for the website"""

    image = models.ImageField(upload_to="banner/")

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Top Banner"
        verbose_name_plural = "Top Banner"

    def __str__(self):
        return "Top Banner"


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

    title = models.CharField(max_length=200, default="Conceptual Communication")

    subtitle = models.CharField(
        max_length=300,
        default="Test your skills and knowledge"
    )

    description = models.TextField(
        default="Assess your abilities and understand where you stand."
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
        verbose_name = "Conceptual Communication"
        verbose_name_plural = "Conceptual Communication"

    def __str__(self):
        return self.title


class CareerRoadmapPage(models.Model):
    """Dynamic Career Roadmap page content"""

    title = models.CharField(max_length=200, default="IT Aspirant")

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
        verbose_name = "IT Aspirant"
        verbose_name_plural = "IT Aspirant"

    def __str__(self):
        return self.title


class LanguageBarrierPage(models.Model):
    """Dynamic Language Barrier page content"""

    title = models.CharField(max_length=200, default="3 Career Paths")

    subtitle = models.CharField(
        max_length=300,
        default="Overcome communication challenges"
    )

    description = models.TextField(
        default="Break through language barriers in your career."
    )

    background_image = models.ImageField(
        upload_to="language_barrier/background/",
        blank=True,
        null=True,
        help_text="Background image with three Explore This Path buttons"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_1_title = models.CharField(max_length=200, default="Left Video", blank=True)
    video_1_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_1_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for left button")
    video_1_uploaded = models.FileField(upload_to="language_barrier/videos/1/", blank=True, null=True)

    video_2_title = models.CharField(max_length=200, default="Center Video", blank=True)
    video_2_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_2_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for center button")
    video_2_uploaded = models.FileField(upload_to="language_barrier/videos/2/", blank=True, null=True)

    video_3_title = models.CharField(max_length=200, default="Right Video", blank=True)
    video_3_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_3_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for right button")
    video_3_uploaded = models.FileField(upload_to="language_barrier/videos/3/", blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "3 Career Paths"
        verbose_name_plural = "3 Career Paths"

    def __str__(self):
        return self.title


class ReadyForTestPage(models.Model):
    """Dynamic Ready For Test page content"""

    title = models.CharField(max_length=200, default="Ready for Test")

    subtitle = models.CharField(
        max_length=300,
        default="Test your readiness"
    )

    description = models.TextField(
        default="Check if you're ready for the next step."
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="ready_for_test/thumbnails/",
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
        upload_to="ready_for_test/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ready For Test Page"
        verbose_name_plural = "Ready For Test Page"

    def __str__(self):
        return self.title


class TestBeforeTrustPage(models.Model):
    """Dynamic Test Before Trust page content"""

    title = models.CharField(max_length=200, default="Test Before You Trust")

    subtitle = models.CharField(
        max_length=300,
        default="Verify before you commit"
    )

    description = models.TextField(
        default="Test our system before you trust us completely."
    )

    background_image = models.ImageField(
        upload_to="test_before_trust/background/",
        blank=True,
        null=True,
        help_text="Background image with three Explore This Path buttons"
    )

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube Link"),
        ("upload", "Upload Video"),
    ]

    video_1_title = models.CharField(max_length=200, default="Left Video", blank=True)
    video_1_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_1_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for left button")
    video_1_uploaded = models.FileField(upload_to="test_before_trust/videos/1/", blank=True, null=True)

    video_2_title = models.CharField(max_length=200, default="Center Video", blank=True)
    video_2_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_2_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for center button")
    video_2_uploaded = models.FileField(upload_to="test_before_trust/videos/2/", blank=True, null=True)

    video_3_title = models.CharField(max_length=200, default="Right Video", blank=True)
    video_3_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default="youtube")
    video_3_youtube_url = models.URLField(blank=True, default="", help_text="YouTube video URL for right button")
    video_3_uploaded = models.FileField(upload_to="test_before_trust/videos/3/", blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Test Before Trust Page"
        verbose_name_plural = "Test Before Trust Page"

    def __str__(self):
        return self.title


class CareerCapsulesPage(models.Model):
    """Dynamic Career Capsules page content"""

    title = models.CharField(max_length=200, default="From Zero to Industry Ready")

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

    title = models.CharField(max_length=200, default="30 Minutes a day")

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
