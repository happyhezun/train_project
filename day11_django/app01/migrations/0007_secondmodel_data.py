# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_secondmodel_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='Data',
            field=models.DateField(default='2016-10-11', auto_now_add=True),
            preserve_default=False,
        ),
    ]
