# Generated by Django 4.2 on 2023-07-21 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_store_is_active_alter_post_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
