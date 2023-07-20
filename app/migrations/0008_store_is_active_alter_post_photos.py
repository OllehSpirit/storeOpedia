# Generated by Django 4.2 on 2023-07-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_inbox_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='photos/posts/%Y/%m/%d/'),
        ),
    ]