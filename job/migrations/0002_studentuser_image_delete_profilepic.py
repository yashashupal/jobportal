# Generated by Django 4.2.1 on 2023-12-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pic'),
        ),
        migrations.DeleteModel(
            name='profilepic',
        ),
    ]
