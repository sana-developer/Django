# Generated by Django 5.1.7 on 2025-03-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('candidate', 'Candidate'), ('employer', 'Employer')], default='candiate', max_length=100, null=True),
        ),
    ]
