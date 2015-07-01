# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diamond_color', models.CharField(max_length=2)),
                ('diamond_clarity', models.CharField(max_length=2)),
                ('diamond_weight_carats', models.IntegerField()),
                ('shape', models.CharField(max_length=20)),
                ('setting_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karat', models.IntegerField(unique=True)),
                ('price_per_gram', models.IntegerField()),
            ],
            options={
                'db_table': 'gold',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_image', models.ImageField(upload_to=b'/uploads')),
                ('first_image', models.ImageField(upload_to=b'/uploads')),
                ('second_image', models.ImageField(upload_to=b'/uploads')),
                ('third_image', models.ImageField(upload_to=b'/uploads')),
                ('fourth_image', models.ImageField(upload_to=b'/uploads')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jewel_code', models.CharField(max_length=15)),
                ('jewel_name', models.CharField(max_length=50)),
                ('photos', models.ForeignKey(to='product.Photos')),
            ],
        ),
        migrations.CreateModel(
            name='subProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_jewel', models.CharField(max_length=30)),
                ('weight_grams', models.IntegerField()),
                ('height_mm', models.IntegerField()),
                ('width_mm', models.IntegerField()),
                ('stones_or_pearls_price', models.IntegerField()),
                ('stones_string_price', models.IntegerField()),
                ('uncut_diamond_weight', models.IntegerField()),
                ('uncut_diamond_price', models.IntegerField()),
                ('making_price', models.IntegerField()),
                ('stock_quantity', models.IntegerField(default=0)),
                ('size', models.IntegerField()),
                ('jewel_code', models.ForeignKey(to='product.ProductCode')),
                ('karat', models.ForeignKey(to='product.Gold')),
            ],
        ),
        migrations.AddField(
            model_name='diamond',
            name='product_code',
            field=models.ForeignKey(to='product.ProductCode'),
        ),
    ]
