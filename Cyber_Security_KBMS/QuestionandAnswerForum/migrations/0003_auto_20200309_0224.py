# Generated by Django 2.2.6 on 2020-03-09 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionandAnswerForum', '0002_auto_20200309_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
