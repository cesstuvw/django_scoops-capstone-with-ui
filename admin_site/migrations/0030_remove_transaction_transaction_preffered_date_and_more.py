# Generated by Django 4.1.3 on 2023-01-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0029_remove_transaction_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_preffered_date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_preferred_date',
            field=models.CharField(max_length=250, null=True, verbose_name='Preferred Date'),
        ),
    ]