# Generated by Django 2.0.1 on 2018-02-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('first_name_en_us', models.CharField(max_length=50, null=True, verbose_name='first name')),
                ('first_name_uk', models.CharField(max_length=50, null=True, verbose_name='first name')),
                ('second_name', models.CharField(max_length=80, verbose_name='second name')),
                ('second_name_en_us', models.CharField(max_length=80, null=True, verbose_name='second name')),
                ('second_name_uk', models.CharField(max_length=80, null=True, verbose_name='second name')),
                ('is_class_teacher', models.BooleanField(default=False, verbose_name='is class teacher?')),
                ('default_classroom', models.SmallIntegerField(verbose_name='default classroom')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
        ),
    ]
