# Generated by Django 3.2.6 on 2021-10-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(db_index=True, editable=False, max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
