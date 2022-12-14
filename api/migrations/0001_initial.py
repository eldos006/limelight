# Generated by Django 4.1.3 on 2022-11-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('marka', models.CharField(max_length=150, verbose_name='Марка')),
                ('year', models.CharField(max_length=150, verbose_name='Год')),
                ('price', models.CharField(max_length=250, verbose_name='Цена')),
                ('color', models.CharField(max_length=150, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('anons', models.TextField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
