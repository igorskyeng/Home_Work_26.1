# Generated by Django 5.0.4 on 2024-06-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_payments_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID платежа'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
    ]
