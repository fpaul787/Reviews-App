# Generated by Django 3.0.7 on 2020-08-23 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_total_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='likes',
            new_name='users_like',
        ),
    ]
