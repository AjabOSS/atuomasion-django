# Generated by Django 4.1 on 2022-09-09 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0007_alter_letter_options_letter_target_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='allow_for_l_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='allow_for_l_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='allow_for_l_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='publishing_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]