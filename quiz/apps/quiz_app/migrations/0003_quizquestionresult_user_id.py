# Generated by Django 3.2.6 on 2021-10-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_quiz_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestionresult',
            name='user_id',
            field=models.PositiveIntegerField(default=0, verbose_name='ID пользователя'),
            preserve_default=False,
        ),
    ]
