# Generated by Django 3.2.6 on 2023-08-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_alter_story_items_stor'),
    ]

    operations = [
        migrations.AddField(
            model_name='story_items',
            name='purch_price',
            field=models.FloatField(default=1, verbose_name='purchases price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story_items',
            name='selling_price',
            field=models.FloatField(default=1, verbose_name='Selling price'),
            preserve_default=False,
        ),
    ]
