# Generated by Django 4.1.3 on 2023-02-04 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0063_alter_transaction_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos_payment',
            name='pos_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
