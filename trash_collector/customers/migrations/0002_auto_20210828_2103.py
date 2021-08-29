# Generated by Django 3.2.5 on 2021-08-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='street_address',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspend_end',
            field=models.DateField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspend_start',
            field=models.DateField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='weekly_pickup_day',
            field=models.CharField(default=True, max_length=9),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default=True, max_length=5),
        ),
    ]
