# Generated by Django 5.1 on 2024-08-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemini_e_commerce', '0005_chathistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='chat_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chathistory',
            name='response_text',
            field=models.CharField(max_length=200),
        ),
    ]
