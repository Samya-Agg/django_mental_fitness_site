# Generated by Django 4.2.11 on 2024-06-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_chat_recipient_profile_therapist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='recipient',
            field=models.TextField(default=False, max_length=50),
        ),
    ]
