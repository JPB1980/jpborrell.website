# Generated by Django 3.2.9 on 2021-11-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0003_auto_20211129_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]