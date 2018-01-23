# Generated by Django 2.0.1 on 2018-01-23 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('tables', '0002_auto_20180109_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
            preserve_default=False,
        ),
    ]