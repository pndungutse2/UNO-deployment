# Generated by Django 2.2 on 2023-10-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Hoodie'), ('OW', 'Cap')], max_length=2),
        ),
    ]
