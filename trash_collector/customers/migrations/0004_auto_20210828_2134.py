# Generated by Django 3.2.5 on 2021-08-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210828_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='balance',
        ),
        migrations.AddField(
            model_name='customer',
            name='account_balance',
            field=models.IntegerField(max_length=int, null=True, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(null=True, verbose_name='One Time Pick-Up Date'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street_address',
            field=models.CharField(max_length=50, verbose_name='Street Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='suspend_end',
            field=models.DateField(null=True, verbose_name='Suspension End Date'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='suspend_start',
            field=models.DateField(null=True, verbose_name='Suspension Start Date'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='weekly_pickup_day',
            field=models.CharField(max_length=9, verbose_name='Pick-Up Day'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='Zip Code'),
        ),
    ]
