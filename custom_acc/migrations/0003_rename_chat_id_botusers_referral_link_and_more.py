# Generated by Django 4.0 on 2021-12-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_acc', '0002_rename_user_bot_id_botusers_chat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botusers',
            old_name='chat_id',
            new_name='referral_link',
        ),
        migrations.AddField(
            model_name='botusers',
            name='user_id',
            field=models.PositiveIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]