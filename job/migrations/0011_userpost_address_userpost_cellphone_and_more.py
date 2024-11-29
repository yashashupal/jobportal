# Generated by Django 4.2.1 on 2024-01-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_alter_clinteragister_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='cellphone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='companydescription',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='companyname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='companywebsite',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='industry',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='landlinephone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
