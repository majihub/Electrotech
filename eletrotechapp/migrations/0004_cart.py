# Generated by Django 5.0.4 on 2024-05-18 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eletrotechapp', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eletrotechapp.products')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eletrotechapp.customers')),
            ],
        ),
    ]