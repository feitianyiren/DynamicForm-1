# Generated by Django 2.1.2 on 2018-11-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_custom_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldmodel',
            name='field',
            field=models.CharField(max_length=100),
        ),
    ]