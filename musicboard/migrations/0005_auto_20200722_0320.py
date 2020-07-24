# Generated by Django 3.0.8 on 2020-07-21 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicboard', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicpost',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_music', to=settings.AUTH_USER_MODEL),
        ),
    ]