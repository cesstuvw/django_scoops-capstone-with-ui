# Generated by Django 4.1.3 on 2022-12-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_no',
            field=models.CharField(max_length=200, unique=True, verbose_name='Transaction Number'),
        ),
    ]
