# Generated by Django 3.2.6 on 2022-09-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configrate', '0003_auto_20220911_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name_lo',
            field=models.CharField(max_length=50, unique=True, verbose_name='اسم الصنف المحلي'),
        ),
    ]
