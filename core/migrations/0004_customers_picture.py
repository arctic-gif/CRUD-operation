# Generated by Django 5.0.7 on 2024-08-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='picture',
            field=models.ImageField(blank='False', null='True', upload_to='', verbose_name='image'),
            preserve_default='True',
        ),
    ]
