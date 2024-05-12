# Generated by Django 5.0.4 on 2024-04-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
    ]
