# Generated by Django 4.1.2 on 2022-12-13 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0006_alter_profile_profile_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='OrderItem_user',
        ),
    ]