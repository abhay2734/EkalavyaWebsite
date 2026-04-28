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


class TheSystemPage(models.Model):
    """Dynamic The System page content - exact copy of AI Advantage page"""

    title = models.CharField(max_length=200, default="The System")

    subtitle = models.CharField(
        max_length=300,
        default="AI is not replacing people — it is empowering those who learn how to use it."
    )

    description = models.TextField(
        default="We are living in a powerful technological shift. Many people fear that artificial intelligence will replace them, while others are learning how to use it as a tool to grow faster. The difference is not intelligence or talent — it is clarity and direction."
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
        verbose_name = "The System"
        verbose_name_plural = "The System"

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
        verbose_name = "3 Career Paths"
        verbose_name_plural = "3 Career Paths"

    def __str__(self):
        return self.title


class ReadyForTestPage(models.Model):
    """Dynamic Ready for Test page content"""

    title = models.CharField(max_length=200, default="Ready for Test")

    subtitle = models.CharField(
        max_length=300,
        default="Test your readiness before moving forward"
    )

    description = models.TextField(
        default="Ensure you're prepared for the next stage of your journey with our assessment tools."
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
        verbose_name = "Ready for Test Page"
        verbose_name_plural = "Ready for Test Page"

    def __str__(self):
        return self.title


class TestBeforeTrustPage(models.Model):
    """Dynamic Test Before You Trust page content"""

    title = models.CharField(max_length=200, default="Test Before You Trust")

    subtitle = models.CharField(
        max_length=300,
        default="Verify our quality before you commit"
    )

    description = models.TextField(
        default="Experience our teaching methodology and quality before making a decision."
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
        verbose_name = "Test Before You Trust Page"
        verbose_name_plural = "Test Before You Trust Page"

    def __str__(self):
        return self.title
