# Generated by Django 4.2 on 2023-05-11 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_quiz_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='category',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questions',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Leaderboard',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]