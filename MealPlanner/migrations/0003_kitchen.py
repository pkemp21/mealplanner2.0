# Generated by Django 4.2 on 2023-04-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealPlanner', '0002_rename_image_url_meals_imageurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
            ],
        ),
    ]
