# Generated by Django 2.0.1 on 2018-02-01 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ('form', 'index'), 'verbose_name': 'class', 'verbose_name_plural': 'classes'},
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('form', 'index')},
        ),
    ]