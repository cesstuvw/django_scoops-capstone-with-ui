# Generated by Django 4.1.3 on 2022-12-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0010_alter_product_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Price'),
        ),
    ]