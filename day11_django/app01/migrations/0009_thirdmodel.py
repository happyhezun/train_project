# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_secondmodel_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
