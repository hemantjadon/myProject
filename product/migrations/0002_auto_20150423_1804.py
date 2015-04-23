# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diamond',
            name='sub_product_code',
        ),
        migrations.AddField(
            model_name='diamond',
            name='product_code',
            field=models.ForeignKey(to='product.ProductCode', default=datetime.datetime(2015, 4, 23, 12, 34, 56, 888297, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
