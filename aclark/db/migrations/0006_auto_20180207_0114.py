# Generated by Django 2.0.1 on 2018-02-07 01:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_invoice_sa_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Start Date'),
        ),
    ]
