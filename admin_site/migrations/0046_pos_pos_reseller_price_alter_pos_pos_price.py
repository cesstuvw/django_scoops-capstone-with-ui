# Generated by Django 4.1.3 on 2023-01-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0045_product_product_resellerprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos',
            name='pos_reseller_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Reseller Price'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='pos_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Pos Price'),
        ),
    ]
