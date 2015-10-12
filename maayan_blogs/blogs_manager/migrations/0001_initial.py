# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPageContentLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WildBlog',
            fields=[
                ('path', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='webpagecontentlocation',
            name='wild_blog',
            field=models.ForeignKey(to='blogs_manager.WildBlog'),
        ),
    ]
