# Generated by Django 4.2.7 on 2023-11-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruit', 'Fruit'), ('Dairy', 'Dairy'), ('Vegetable', 'Vegetable')], max_length=30, null=True),
        ),
    ]
