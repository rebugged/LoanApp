# Generated by Django 2.2.14 on 2020-09-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='AppID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]