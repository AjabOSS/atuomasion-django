# Generated by Django 4.1 on 2022-09-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0009_letter_replay'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='letter',
            name='reject_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]