# Generated by Django 4.0.2 on 2022-02-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
