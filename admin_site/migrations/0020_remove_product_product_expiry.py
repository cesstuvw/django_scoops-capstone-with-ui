# Generated by Django 4.1.2 on 2022-12-16 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0019_alter_profile_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_expiry',
        ),
    ]
