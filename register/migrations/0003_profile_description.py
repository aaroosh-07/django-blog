# Generated by Django 2.2.15 on 2020-11-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20201030_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]