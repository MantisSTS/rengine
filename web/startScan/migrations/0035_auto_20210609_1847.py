# Generated by Django 3.1.6 on 2021-06-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0034_auto_20210609_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='ports',
            field=models.ManyToManyField(related_name='ports', to='startScan.Port'),
        ),
    ]