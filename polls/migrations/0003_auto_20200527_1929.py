# Generated by Django 2.2.10 on 2020-05-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_answer_vote_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='owner',
        ),
        migrations.AddField(
            model_name='answer',
            name='owner_id',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
