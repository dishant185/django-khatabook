# Generated by Django 5.0 on 2024-10-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0003_deposit_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='amount1',
            field=models.IntegerField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='description1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
