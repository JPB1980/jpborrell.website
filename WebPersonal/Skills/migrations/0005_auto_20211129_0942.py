# Generated by Django 3.2.9 on 2021-11-29 08:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0004_auto_20211129_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=ckeditor.fields.RichTextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=200),
        ),
    ]
