# Generated by Django 4.1.3 on 2023-02-04 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0060_alter_transaction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Date Ordered'),
        ),
    ]
