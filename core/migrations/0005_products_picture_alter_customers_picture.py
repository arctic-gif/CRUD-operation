# Generated by Django 5.0.7 on 2024-08-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_customers_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(blank='False', null='True', upload_to='images/', verbose_name='image'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='customers',
            name='picture',
            field=models.ImageField(blank='False', null='True', upload_to='images/', verbose_name='image'),
        ),
    ]
