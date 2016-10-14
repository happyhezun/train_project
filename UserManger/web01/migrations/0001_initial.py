# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserName', models.CharField(max_length=50)),
                ('PassWord', models.CharField(max_length=200)),
                ('Gender', models.BooleanField()),
                ('Age', models.IntegerField()),
                ('Data', models.DateField(auto_now_add=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
