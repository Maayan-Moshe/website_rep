# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maayan_wild_blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='web_page_content_location',
        ),
    ]
