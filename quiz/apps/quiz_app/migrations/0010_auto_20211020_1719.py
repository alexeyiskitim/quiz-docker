# Generated by Django 3.2.7 on 2021-10-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0009_auto_20211020_1645'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OptionsToAnswer',
            new_name='OptionToAnswer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='textAnswer',
        ),
        migrations.RemoveField(
            model_name='quizquestionresult',
            name='answer',
        ),
        migrations.AddField(
            model_name='quizquestionresult',
            name='option_to_answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.optiontoanswer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizquestionresult',
            name='textAnswer',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200, null=True, unique=True, verbose_name='Ответ'),
        ),
    ]
