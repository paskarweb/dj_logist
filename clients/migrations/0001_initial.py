# Generated by Django 3.0 on 2019-12-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('short_name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Короткое имя')),
                ('code_client', models.IntegerField(default=0, verbose_name='Код (ЕРДПО)')),
                ('address', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, default=None, null=True, verbose_name='Примечание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновление')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
