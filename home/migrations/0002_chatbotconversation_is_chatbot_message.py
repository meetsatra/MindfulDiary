# Generated by Django 4.2.5 on 2024-01-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotconversation',
            name='is_chatbot_message',
            field=models.BooleanField(default=False),
        ),
    ]