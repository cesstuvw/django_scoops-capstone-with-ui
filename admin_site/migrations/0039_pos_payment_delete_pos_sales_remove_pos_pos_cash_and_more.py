# Generated by Django 4.1.3 on 2023-01-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0038_remove_pos_sales_pos_cash_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pos_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_user', models.CharField(default=None, max_length=200, verbose_name='Role')),
                ('pos_TotalAmount', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Total Amount')),
                ('pos_cash', models.BigIntegerField(null=True, verbose_name='Cash')),
                ('pos_change', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Change')),
            ],
        ),
        migrations.DeleteModel(
            name='Pos_Sales',
        ),
        migrations.RemoveField(
            model_name='pos',
            name='pos_cash',
        ),
        migrations.RemoveField(
            model_name='pos',
            name='pos_change',
        ),
    ]