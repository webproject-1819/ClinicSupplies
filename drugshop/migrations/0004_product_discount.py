# Generated by Django 2.2 on 2019-05-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugshop', '0003_auto_20190511_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0, null=True),
        ),
    ]
