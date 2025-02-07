# Generated by Django 4.2.1 on 2023-12-27 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='studentuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('resume', models.FileField(null=True, upload_to='Profile_pic')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profilepic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profilepicture', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
