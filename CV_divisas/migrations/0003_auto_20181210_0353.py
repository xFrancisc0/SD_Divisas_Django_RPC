# Generated by Django 2.1.4 on 2018-12-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV_divisas', '0002_auto_20181126_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion_moneda',
            name='pais',
            field=models.CharField(db_column='pais', max_length=20, verbose_name='pais'),
        ),
    ]
