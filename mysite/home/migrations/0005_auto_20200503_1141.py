# Generated by Django 3.0.5 on 2020-05-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200503_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='canvas_token',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
