# Generated by Django 3.1.4 on 2021-02-04 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lenta', '0005_auto_20210130_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='post_comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='lenta.post'),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='text',
            field=models.TextField(max_length=200, verbose_name='text'),
        ),
    ]