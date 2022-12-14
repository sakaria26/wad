# Generated by Django 4.0.4 on 2022-10-21 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomadation',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postaladdressid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.postal_address'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisationaddress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.address'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='paperid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.paper'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speakerorganisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organisation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='affiliateorganisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organisation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.title'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='addressid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.address'),
        ),
    ]
