# Generated by Django 4.0 on 2021-12-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_acc', '0003_rename_chat_id_botusers_referral_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botusers',
            name='referral_link',
        ),
        migrations.RemoveField(
            model_name='referrallinks',
            name='used',
        ),
        migrations.AddField(
            model_name='botusers',
            name='super_code',
            field=models.CharField(default='000AB', max_length=15),
        ),
    ]
