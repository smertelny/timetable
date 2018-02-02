# Generated by Django 2.0.1 on 2018-02-02 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0011_auto_20180202_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.Class'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.Lessons'),
        ),
    ]