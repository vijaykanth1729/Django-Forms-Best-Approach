# Generated by Django 3.0.2 on 2020-01-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='address_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='address_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='forum',
            name='password',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='forum',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='zip',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
