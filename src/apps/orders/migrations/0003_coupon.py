# Generated by Django 3.1.4 on 2021-01-04 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210104_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='код купона')),
                ('valid_from', models.DateTimeField(verbose_name='дата и время начала действия купона')),
                ('valid_to', models.DateTimeField(verbose_name='дата и время окончания действия купона')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='размер скидки в %')),
                ('active', models.BooleanField(verbose_name='активен')),
            ],
            options={
                'verbose_name': 'купон',
                'verbose_name_plural': 'купоны',
            },
        ),
    ]
