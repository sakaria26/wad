# Generated by Django 4.0.4 on 2022-10-21 03:24

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_accomadation_tenant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(default=base.models.generateuserid, editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]