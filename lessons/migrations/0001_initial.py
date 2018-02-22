# Generated by Django 2.0.1 on 2018-02-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('name_en_us', models.CharField(max_length=30, null=True, unique=True, verbose_name='name')),
                ('name_uk', models.CharField(max_length=30, null=True, unique=True, verbose_name='name')),
                ('short_name', models.CharField(help_text="Can't be longer than 5 characters", max_length=5, unique=True, verbose_name='short name')),
                ('short_name_en_us', models.CharField(help_text="Can't be longer than 5 characters", max_length=5, null=True, unique=True, verbose_name='short name')),
                ('short_name_uk', models.CharField(help_text="Can't be longer than 5 characters", max_length=5, null=True, unique=True, verbose_name='short name')),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessons',
            },
        ),
    ]
