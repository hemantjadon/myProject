# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diamond_earrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gold_wt_grams', models.DecimalField(max_digits=7, decimal_places=3)),
                ('gross_wt_gm', models.DecimalField(max_digits=7, decimal_places=3)),
                ('stones_price', models.IntegerField(blank=True)),
                ('stone_string_price', models.IntegerField(blank=True)),
                ('making_price', models.IntegerField()),
                ('diamond_price', models.IntegerField()),
                ('diamond_weight_carats', models.DecimalField(max_digits=7, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='earring_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jewel_code', models.CharField(max_length=20)),
                ('jewel_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='gold_and_stone_earrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gold_wt_grams', models.DecimalField(max_digits=7, decimal_places=3)),
                ('gross_wt_gm', models.DecimalField(max_digits=7, decimal_places=3)),
                ('stones_price', models.IntegerField(blank=True)),
                ('stone_string_price', models.IntegerField(blank=True)),
                ('making_price', models.IntegerField()),
                ('jewel_code', models.ForeignKey(to='Earrings.earring_code')),
            ],
        ),
        migrations.CreateModel(
            name='kundan_earrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gold_wt_grams', models.DecimalField(max_digits=7, decimal_places=3)),
                ('gross_wt_gm', models.DecimalField(max_digits=7, decimal_places=3)),
                ('stones_price', models.IntegerField(blank=True)),
                ('stone_string_price', models.IntegerField(blank=True)),
                ('making_price', models.IntegerField()),
                ('jewel_code', models.ForeignKey(to='Earrings.earring_code')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_image', models.ImageField(upload_to=b'/earrings')),
            ],
        ),
        migrations.CreateModel(
            name='polki_earrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gold_wt_grams', models.DecimalField(max_digits=7, decimal_places=3)),
                ('gross_wt_gm', models.DecimalField(max_digits=7, decimal_places=3)),
                ('stones_price', models.IntegerField(blank=True)),
                ('stone_string_price', models.IntegerField(blank=True)),
                ('making_price', models.IntegerField()),
                ('uncut_diamond_wt', models.DecimalField(max_digits=7, decimal_places=3)),
                ('uncut_diamond_price', models.IntegerField()),
                ('jewel_code', models.ForeignKey(to='Earrings.earring_code')),
            ],
        ),
        migrations.AddField(
            model_name='earring_code',
            name='photos',
            field=models.ForeignKey(to='Earrings.Photos'),
        ),
        migrations.AddField(
            model_name='diamond_earrings',
            name='jewel_code',
            field=models.ForeignKey(to='Earrings.earring_code'),
        ),
    ]
