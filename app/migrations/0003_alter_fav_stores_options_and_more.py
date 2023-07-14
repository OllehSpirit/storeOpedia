# Generated by Django 4.2 on 2023-07-09 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_store_closing_alter_store_opening'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fav_stores',
            options={'verbose_name': 'Favorite Store', 'verbose_name_plural': 'Favorite Stores'},
        ),
        migrations.AlterModelOptions(
            name='followed_stores',
            options={'verbose_name': 'Followed Store', 'verbose_name_plural': 'Followed Stores'},
        ),
        migrations.AlterModelOptions(
            name='liked_posts',
            options={'verbose_name': 'Liked Post', 'verbose_name_plural': 'Liked Posts'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='rated_stores',
            options={'verbose_name': 'Rated Store', 'verbose_name_plural': 'Rated Stores'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Store', 'verbose_name_plural': 'Stores'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.CreateModel(
            name='Saved_Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
            options={
                'verbose_name': 'Saved Post',
                'verbose_name_plural': 'Saved Posts',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='save_posts',
            field=models.ManyToManyField(related_name='saved', through='app.Saved_Posts', to='app.userprofile'),
        ),
    ]