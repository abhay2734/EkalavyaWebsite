from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_aiadvantagepage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='languagebarrierpage',
            name='uploaded_video_1',
            field=models.FileField(blank=True, help_text='Upload video for Left Career Path', null=True, upload_to='language_barrier/videos/left/'),
        ),
        migrations.AddField(
            model_name='languagebarrierpage',
            name='uploaded_video_2',
            field=models.FileField(blank=True, help_text='Upload video for Center Career Path', null=True, upload_to='language_barrier/videos/center/'),
        ),
        migrations.AddField(
            model_name='languagebarrierpage',
            name='uploaded_video_3',
            field=models.FileField(blank=True, help_text='Upload video for Right Career Path', null=True, upload_to='language_barrier/videos/right/'),
        ),
        migrations.AddField(
            model_name='languagebarrierpage',
            name='youtube_url_1',
            field=models.URLField(blank=True, help_text='YouTube URL for Left Career Path (Software Development)'),
        ),
        migrations.AddField(
            model_name='languagebarrierpage',
            name='youtube_url_2',
            field=models.URLField(blank=True, help_text='YouTube URL for Center Career Path (Data & AI)'),
        ),
        migrations.AddField(
            model_name='languagebarrierpage',
            name='youtube_url_3',
            field=models.URLField(blank=True, help_text='YouTube URL for Right Career Path (Design & UX)'),
        ),
    ]