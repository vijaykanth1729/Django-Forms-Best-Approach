# Generated by Django 3.0.2 on 2020-01-22 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='published date'),
            preserve_default=False,
        ),
    ]
