# Generated by Django 3.2.5 on 2021-09-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_ratings', '0004_auto_20210908_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
