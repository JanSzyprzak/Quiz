# Generated by Django 4.2 on 2023-05-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Quiz', '0003_remove_leaderboard_user_remove_question_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderboardEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score', 'timestamp'],
            },
        ),
    ]
