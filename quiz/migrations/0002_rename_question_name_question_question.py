# Generated by Django 5.0.2 on 2024-03-21 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_name',
            new_name='question',
        ),
    ]
