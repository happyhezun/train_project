# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_secondmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='Address',
            field=models.CharField(default=b'alex', max_length=20),
            preserve_default=True,
        ),
    ]
