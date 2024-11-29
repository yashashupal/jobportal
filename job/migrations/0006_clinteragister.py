# Generated by Django 4.2.1 on 2024-01-06 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0005_userpost_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='clinteragister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('image', models.ImageField(null=True, upload_to='profile_pic_clinte')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=15, null=True)),
                ('companyname', models.CharField(max_length=10, null=True)),
                ('industry', models.CharField(max_length=10, null=True)),
                ('orgtype', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=10, null=True)),
                ('landlinephone', models.CharField(max_length=10, null=True)),
                ('cellphone', models.CharField(max_length=10, null=True)),
                ('companywebsite', models.CharField(max_length=10, null=True)),
                ('noofemployees', models.CharField(max_length=10, null=True)),
                ('companydescription', models.CharField(max_length=10, null=True)),
                ('companylogo', models.FileField(max_length=10, null=True, upload_to='company_logo_clinte')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clinteuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
