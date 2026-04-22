# Generated migration to restore ReadyForTestPage and TestBeforeTrustPage

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_delete_readyfortestpage_delete_testbeforetrustpage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadyForTestPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Ready for Test', max_length=200)),
                ('subtitle', models.CharField(default="Test your readiness before moving forward", max_length=300)),
                ('description', models.TextField(default="Ensure you're prepared for the next stage of your journey with our assessment tools.")),
                ('image', models.ImageField(help_text='Main image for the Ready for Test section', upload_to='ready_for_test/')),
                ('video_title', models.CharField(default='Watch Now', max_length=200)),
                ('video_thumbnail', models.ImageField(help_text='Video thumbnail image', upload_to='ready_for_test/thumbnails/')),
                ('video_type', models.CharField(choices=[('youtube', 'YouTube Link'), ('upload', 'Upload Video')], default='youtube', max_length=10)),
                ('youtube_url', models.URLField(blank=True, help_text='YouTube video URL')),
                ('uploaded_video', models.FileField(blank=True, help_text='Upload video file if not using YouTube', null=True, upload_to='ready_for_test/videos/')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ready for Test Page',
                'verbose_name_plural': 'Ready for Test Page',
            },
        ),
        migrations.CreateModel(
            name='TestBeforeTrustPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Test Before You Trust', max_length=200)),
                ('subtitle', models.CharField(default='Verify our quality before you commit', max_length=300)),
                ('description', models.TextField(default='Experience our teaching methodology and quality before making a decision.')),
                ('image', models.ImageField(help_text='Main image for the Test Before You Trust section', upload_to='test_before_trust/')),
                ('video_title', models.CharField(default='Watch Now', max_length=200)),
                ('video_thumbnail', models.ImageField(help_text='Video thumbnail image', upload_to='test_before_trust/thumbnails/')),
                ('video_type', models.CharField(choices=[('youtube', 'YouTube Link'), ('upload', 'Upload Video')], default='youtube', max_length=10)),
                ('youtube_url', models.URLField(blank=True, help_text='YouTube video URL')),
                ('uploaded_video', models.FileField(blank=True, help_text='Upload video file if not using YouTube', null=True, upload_to='test_before_trust/videos/')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Test Before You Trust Page',
                'verbose_name_plural': 'Test Before You Trust Page',
            },
        ),
    ]
