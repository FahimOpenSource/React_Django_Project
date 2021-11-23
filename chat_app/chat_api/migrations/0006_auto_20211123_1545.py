# Generated by Django 3.2.9 on 2021-11-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_api', '0005_alter_message_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file_url',
        ),
        migrations.AddField(
            model_name='message',
            name='response',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
