# Generated by Django 3.2.16 on 2022-12-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221226_0540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]
