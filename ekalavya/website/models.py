from django.db import models


class HeroImage(models.Model):
    """Single hero image for the homepage"""

    image = models.ImageField(upload_to="hero/")

    main_heading = models.CharField(
        max_length=300,
        default="Ekalavya Mission: From Zer0 to Industry-Ready — a Complete Transformation."
    )

    button_text = models.CharField(
        max_length=200,
        default="▶ Start with a 5-minute overview of what this system delivers"
    )

    subtitle = models.CharField(
        max_length=300,
        default="👉 Discover the All-in-One Skillset through a single, structured System before you Start."
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 Industry-ready Training is different from Exam-ready Learning.",
        help_text="First highlight line in the description card"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 The WINdianized Organic Learning System is built exactly for that transformation.",
        help_text="Second highlight line in the description card"
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

    highlight_1 = models.CharField(
        max_length=300,
        default="👉 Industry-ready Training is different from Exam-ready Learning.",
        help_text="First highlight line in the description card"
    )

    highlight_2 = models.CharField(
        max_length=300,
        default="👉 The WINdianized Organic Learning System is built exactly for that transformation.",
        help_text="Second highlight line in the description card"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for skill test section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for skill test section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for skill test section",
        help_text="Third highlight line in the card box"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for IT Aspirant section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for IT Aspirant section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for IT Aspirant section",
        help_text="Third highlight line in the card box"
    )

    line_4 = models.CharField(
        max_length=300,
        default="👉 Fourth highlight line for IT Aspirant section",
        help_text="Fourth highlight line in the card box"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for Career Capsules section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for Career Capsules section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for Career Capsules section",
        help_text="Third highlight line in the card box"
    )

    line_4 = models.CharField(
        max_length=300,
        default="👉 Fourth highlight line for Career Capsules section",
        help_text="Fourth highlight line in the card box"
    )

    line_5 = models.CharField(
        max_length=300,
        default="👉 Fifth highlight line for Career Capsules section",
        help_text="Fifth highlight line in the card box"
    )

    line_6 = models.CharField(
        max_length=300,
        default="👉 Sixth highlight line for Career Capsules section",
        help_text="Sixth highlight line in the card box"
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
        verbose_name = "Career Capsules Page"
        verbose_name_plural = "Career Capsules Page"

    def __str__(self):
        return self.title


class LearningSystemPage(models.Model):
    """Dynamic Learning System page content"""

    title = models.CharField(max_length=200, default="30 Minutes a day")

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for Learning System section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for Learning System section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for Learning System section",
        help_text="Third highlight line in the card box"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for 3 Career Paths section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for 3 Career Paths section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for 3 Career Paths section",
        help_text="Third highlight line in the card box"
    )

    line_4 = models.CharField(
        max_length=300,
        default="👉 Fourth highlight line for 3 Career Paths section",
        help_text="Fourth highlight line in the card box"
    )

    line_5 = models.CharField(
        max_length=300,
        default="👉 Fifth highlight line for 3 Career Paths section",
        help_text="Fifth highlight line in the card box"
    )

    line_6 = models.CharField(
        max_length=300,
        default="👉 Sixth highlight line for 3 Career Paths section",
        help_text="Sixth highlight line in the card box"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for Ready for Test section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for Ready for Test section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for Ready for Test section",
        help_text="Third highlight line in the card box"
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

    line_1 = models.CharField(
        max_length=300,
        default="👉 First highlight line for Test Before You Trust section",
        help_text="First highlight line in the card box"
    )

    line_2 = models.CharField(
        max_length=300,
        default="👉 Second highlight line for Test Before You Trust section",
        help_text="Second highlight line in the card box"
    )

    line_3 = models.CharField(
        max_length=300,
        default="👉 Third highlight line for Test Before You Trust section",
        help_text="Third highlight line in the card box"
    )

    line_4 = models.CharField(
        max_length=300,
        default="👉 Fourth highlight line for Test Before You Trust section",
        help_text="Fourth highlight line in the card box"
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
