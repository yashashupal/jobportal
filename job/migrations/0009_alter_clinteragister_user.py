# Generated by Django 4.2.1 on 2024-01-09 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0008_clinteragister_email_studentuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinteragister',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clinteragister', to=settings.AUTH_USER_MODEL),
        ),
    ]
