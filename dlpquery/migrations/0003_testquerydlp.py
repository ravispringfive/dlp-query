# Generated by Django 3.2 on 2021-05-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlpquery', '0002_rename_testapi_queryapi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testquerydlp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('lastname', models.CharField(default='', max_length=80)),
                ('comp', models.CharField(default='', max_length=80)),
            ],
        ),
    ]
