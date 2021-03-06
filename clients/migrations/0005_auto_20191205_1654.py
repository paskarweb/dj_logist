# Generated by Django 3.0 on 2019-12-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_client_client_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
