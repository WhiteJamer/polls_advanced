# Generated by Django 2.2.10 on 2020-05-27 11:19

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
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название', max_length=255)),
                ('start_date', models.DateTimeField(auto_now_add=True, help_text='Дата старта')),
                ('end_date', models.DateTimeField(blank=True, help_text='Дата окончания', null=True)),
                ('description', models.TextField(blank=True, help_text='Описание', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Активен?')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст вопроса')),
                ('type', models.CharField(choices=[('TEXT', 'Ответ текстом'), ('ONE', 'Выбор одного варианта'), ('MANY', 'Выбор несколький вариантов')], help_text='Тип вопроса', max_length=4)),
                ('poll', models.ForeignKey(help_text='Опрос', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст варианта')),
                ('question', models.ForeignKey(help_text='Вопрос', on_delete=django.db.models.deletion.CASCADE, related_name='options', to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст ответа')),
                ('owner', models.ForeignKey(help_text='Владелец', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(help_text='Вопрос', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Question')),
            ],
        ),
    ]
