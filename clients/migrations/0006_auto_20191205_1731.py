# Generated by Django 3.0 on 2019-12-05 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20191205_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.ForeignKey(blank=True, default=None, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.ClientType', verbose_name='Тип клиента'),
        ),
    ]
