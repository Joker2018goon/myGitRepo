# Generated by Django 2.0.7 on 2019-03-04 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20180207_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sign.Event'),
        ),
    ]
