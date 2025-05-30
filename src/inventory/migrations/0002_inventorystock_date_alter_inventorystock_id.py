# Generated by Django 5.2 on 2025-05-02 20:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorystock',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventorystock',
            name='id',
            field=models.AutoField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
