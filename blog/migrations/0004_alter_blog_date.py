# Generated by Django 4.0.4 on 2022-05-05 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 13, 32, 43, 93038, tzinfo=utc)),
        ),
    ]