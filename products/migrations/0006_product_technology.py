# Generated by Django 3.2.23 on 2024-01-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.technology'),
        ),
    ]
