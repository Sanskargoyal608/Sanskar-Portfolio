# Generated by Django 4.2.10 on 2024-03-05 12:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_upload_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_form',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
