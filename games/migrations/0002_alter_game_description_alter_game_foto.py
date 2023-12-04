# Generated by Django 4.2.7 on 2023-12-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='game',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pic_games/'),
        ),
    ]
