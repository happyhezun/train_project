# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_secondmodel_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='DateTime',
            field=models.DateTimeField(default=b'2011-11-11', auto_now=True),
            preserve_default=True,
        ),
    ]
