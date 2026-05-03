from django.db import models


class HeroImage(models.Model):
    """Single hero image for the homepage"""

    image = models.ImageField(upload_to="hero/")

    hero_interstitial_image = models.ImageField(
        upload_to="hero/interstitial/",
        blank=True,
        null=True,
        help_text="Image to display between hero section and home video section"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hero Image"
        verbose_name_plural = "Hero Image"

    def __str__(self):
        return "Hero Image"


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

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "1)The System"
        verbose_name_plural = "1)The System"

    def __str__(self):
        if self.title:
            return self.title
        return "Homepage Video"





class AIAdvantage(models.Model):
    """Dynamic AI Fear vs AI Advantage page content"""

    title = models.CharField(max_length=200, default="AI Fear vs AI Advantage")

    header_image = models.ImageField(
        upload_to="ai_advantage/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
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
        verbose_name = "3)AI Advantage"
        verbose_name_plural = "3)AI Advantage"

    def __str__(self):
        return self.title


class TheSystem(models.Model):
    """Dynamic The System page content - exact copy of AI Advantage page"""

    title = models.CharField(max_length=200, default="The System")

    header_image = models.ImageField(
        upload_to="the_system/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="the_system/thumbnails/",
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
        upload_to="the_system/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "2)Truth of AI"
        verbose_name_plural = "2)Truth of AI"

    def __str__(self):
        return self.title


class ConceptualCommunication(models.Model):
    """Dynamic Skill Test page content"""

    title = models.CharField(max_length=200, default="Conceptual Communication")

    header_image = models.ImageField(
        upload_to="conceptual_communication/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
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
        verbose_name = "4) Conceptual Communication"
        verbose_name_plural = "4) Conceptual Communication"

    def __str__(self):
        return self.title


class ITAspirant(models.Model):
    """Dynamic Career Roadmap page content"""

    title = models.CharField(max_length=200, default="IT Aspirant")

    header_image = models.ImageField(
        upload_to="it_aspirant/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
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
        verbose_name = "6) IT Aspirant"
        verbose_name_plural = "6) IT Aspirant"

    def __str__(self):
        return self.title


class ZeroToIndustry(models.Model):
    """Dynamic Career Capsules page content"""

    title = models.CharField(max_length=200, default="From Zero to Industry Ready")

    header_image = models.ImageField(
        upload_to="zero_to_industry/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="career_capsules/",
        help_text="Main image for the Career Capsules section",
        null=True
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
        verbose_name = "8)Zero to Industry"
        verbose_name_plural = "8)Zero to Industry"

    def __str__(self):
        return self.title


class ThirtyMinutes(models.Model):
    """Dynamic Learning System page content"""

    title = models.CharField(max_length=200, default="30 Minutes a day")

    header_image = models.ImageField(
        upload_to="thirty_minutes/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
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
        verbose_name = "5) 30Minutes"
        verbose_name_plural = "5) 30Minutes"

    def __str__(self):
        return self.title


class CareerPaths(models.Model):
    """Dynamic Language Barrier page content"""

    title = models.CharField(max_length=200, default="3 Career Paths")

    header_image = models.ImageField(
        upload_to="career_paths/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="language_barrier/",
        help_text="Main image for the Language Barrier section",
        null=True
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="language_barrier/thumbnails/",
        help_text="Video thumbnail image with 3 career path buttons",
        null=True
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

    # 3 Career Path Videos
    youtube_url_1 = models.URLField(
        blank=True,
        help_text="YouTube URL for Left Career Path (Software Development)"
    )

    uploaded_video_1 = models.FileField(
        upload_to="language_barrier/videos/left/",
        blank=True,
        null=True,
        help_text="Upload video for Left Career Path"
    )

    youtube_url_2 = models.URLField(
        blank=True,
        help_text="YouTube URL for Center Career Path (Data & AI)"
    )

    uploaded_video_2 = models.FileField(
        upload_to="language_barrier/videos/center/",
        blank=True,
        null=True,
        help_text="Upload video for Center Career Path"
    )

    youtube_url_3 = models.URLField(
        blank=True,
        help_text="YouTube URL for Right Career Path (Design & UX)"
    )

    uploaded_video_3 = models.FileField(
        upload_to="language_barrier/videos/right/",
        blank=True,
        null=True,
        help_text="Upload video for Right Career Path"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "9)3 Career Paths"
        verbose_name_plural = "9)3 Career Paths"

    def __str__(self):
        return self.title


class ReadyForTestPage(models.Model):
    """Dynamic Ready for Test page content"""

    title = models.CharField(max_length=200, default="Ready for Test")

    header_image = models.ImageField(
        upload_to="ready_for_test/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="ready_for_test/",
        help_text="Main image for the Ready for Test section"
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
        verbose_name = "7)Ready for Test Page"
        verbose_name_plural = "7)Ready for Test Page"

    def __str__(self):
        return self.title


class TestBeforeTrustPage(models.Model):
    """Dynamic Test Before You Trust page content"""

    title = models.CharField(max_length=200, default="Test Before You Trust")

    header_image = models.ImageField(
        upload_to="test_before_trust/",
        help_text="Header image displayed above the video section",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="test_before_trust/",
        help_text="Main image for the Test Before You Trust section"
    )

    video_title = models.CharField(max_length=200, default="Watch Now")

    video_thumbnail = models.ImageField(
        upload_to="test_before_trust/thumbnails/",
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
        upload_to="test_before_trust/videos/",
        blank=True,
        null=True,
        help_text="Upload video file if not using YouTube"
    )

    youtube_url_1 = models.URLField(
        blank=True,
        help_text="YouTube video URL for left button"
    )

    uploaded_video_1 = models.FileField(
        upload_to="test_before_trust/videos/",
        blank=True,
        null=True,
        help_text="Upload video file for left button"
    )

    youtube_url_2 = models.URLField(
        blank=True,
        help_text="YouTube video URL for center button"
    )

    uploaded_video_2 = models.FileField(
        upload_to="test_before_trust/videos/",
        blank=True,
        null=True,
        help_text="Upload video file for center button"
    )

    youtube_url_3 = models.URLField(
        blank=True,
        help_text="YouTube video URL for right button"
    )

    uploaded_video_3 = models.FileField(
        upload_to="test_before_trust/videos/",
        blank=True,
        null=True,
        help_text="Upload video file for right button"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "10)Test Before You Trust Page"
        verbose_name_plural = "10)Test Before You Trust Page"

    def __str__(self):
        return self.title
