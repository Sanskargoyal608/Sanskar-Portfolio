# Generated by Django 4.2.10 on 2024-03-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_upload_form_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_form',
            name='image',
            field=models.URLField(),
        ),
    ]
