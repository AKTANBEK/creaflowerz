# Generated by Django 3.2.2 on 2021-05-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='flowers', verbose_name='Фото')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Старая цена')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('size', models.CharField(choices=[('Большой', 'Большой'), ('СРЕДНИЙ', 'Средний'), ('МАЛЕНЬКИЙ', 'Маленький')], max_length=9, verbose_name='Размер')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('category', models.ManyToManyField(related_name='flowers', to='flowers.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
            },
        ),
    ]
