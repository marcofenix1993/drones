# Generated by Django 3.2.16 on 2022-10-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='id',
        ),
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
