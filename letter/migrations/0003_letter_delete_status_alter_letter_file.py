# Generated by Django 4.1 on 2022-09-07 02:45

from django.db import migrations, models
import letter.validators


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0002_letter_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='delete_status',
            field=models.BooleanField(default=True, verbose_name='delete after a year ? '),
        ),
        migrations.AlterField(
            model_name='letter',
            name='file',
            field=models.FileField(default='', upload_to='docs/', validators=[letter.validators.validate_file_extension], verbose_name=' پیوست : '),
        ),
    ]
