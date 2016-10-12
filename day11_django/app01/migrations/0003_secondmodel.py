# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20161011_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondModel',
            fields=[
                ('Nid', models.AutoField(serialize=False, primary_key=True)),
                ('Name', models.CharField(default=b'hanxin', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
