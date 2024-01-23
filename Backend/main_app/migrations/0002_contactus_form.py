# Generated by Django 5.0.1 on 2024-01-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(choices=[('Project', 'Project'), ('Blog', 'Blog'), ('UI/UX Project', 'UI/UX Project'), ('Certificate', 'Certificate'), ('Skills', 'Skills')], max_length=100)),
                ('PhoneNumber', models.IntegerField()),
                ('Topic', models.TextField()),
                ('Message', models.TextField()),
            ],
        ),
    ]
