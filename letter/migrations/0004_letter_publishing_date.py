# Generated by Django 4.1 on 2022-09-07 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_letter_delete_status_alter_letter_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='publishing_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
