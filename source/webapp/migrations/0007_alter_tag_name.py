# Generated by Django 5.1.3 on 2024-12-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20241215_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=31, unique=True, verbose_name='Тег'),
        ),
    ]
