# Generated by Django 4.2.7 on 2023-12-02 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='release_year',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
