# Generated by Django 5.0.4 on 2024-05-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eletrotechapp', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNumber', models.CharField(max_length=200)),
                ('cvv', models.IntegerField()),
                ('expiry', models.CharField(max_length=20)),
                ('PaidUser', models.CharField(max_length=200)),
            ],
        ),
    ]
