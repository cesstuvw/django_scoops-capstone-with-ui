# Generated by Django 4.1.3 on 2023-01-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0046_pos_pos_reseller_price_alter_pos_pos_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos',
            name='pos_ResellerAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Reseller Amount'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='pos_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Pos Amount'),
        ),
    ]
