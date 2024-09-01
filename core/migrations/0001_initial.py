# Generated by Django 5.0.7 on 2024-08-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='False', max_length=100, null='False', verbose_name='name')),
                ('address', models.CharField(blank='False', max_length=100, null='False', verbose_name='address')),
                ('phone', models.CharField(blank='False', max_length=100, null='False', verbose_name='phone')),
                ('email', models.CharField(blank='False', max_length=100, null='False', verbose_name='email')),
            ],
        ),
    ]
