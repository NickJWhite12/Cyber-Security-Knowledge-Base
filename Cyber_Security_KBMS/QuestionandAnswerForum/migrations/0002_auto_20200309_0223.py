# Generated by Django 2.2.6 on 2020-03-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionandAnswerForum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='posted_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
