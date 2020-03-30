# Generated by Django 3.0.2 on 2020-02-26 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('slug', models.SlugField(max_length=40)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CSKnowledgeBase.Expertise')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'expertise_id')},
            },
        ),
        migrations.CreateModel(
            name='KnowledgeTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CSKnowledgeBase.Knowledge')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CSKnowledgeBase.Topic')),
            ],
            options={
                'unique_together': {('knowledge_id', 'topic_id')},
            },
        ),
        migrations.CreateModel(
            name='KnowledgeRelationLookUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asset', to='CSKnowledgeBase.Knowledge')),
                ('countermeasure_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='countermeasure', to='CSKnowledgeBase.Knowledge')),
                ('policy_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='policy', to='CSKnowledgeBase.Knowledge')),
                ('threat_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='threat', to='CSKnowledgeBase.Knowledge')),
                ('vulnerability_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vulnerability', to='CSKnowledgeBase.Knowledge')),
            ],
            options={
                'unique_together': {('asset_entry_id', 'countermeasure_entry_id', 'threat_entry_id', 'vulnerability_entry_id', 'policy_entry_id')},
            },
        ),
        migrations.CreateModel(
            name='EntrySubEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='child', to='CSKnowledgeBase.Knowledge')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parent', to='CSKnowledgeBase.Knowledge')),
            ],
            options={
                'unique_together': {('parent_id', 'child_id')},
            },
        ),
    ]
