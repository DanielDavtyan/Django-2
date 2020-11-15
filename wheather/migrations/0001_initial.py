# Generated by Django 3.1.3 on 2020-11-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=100)),
                ('wheather1', models.FloatField()),
                ('humidity', models.FloatField()),
                ('speed', models.FloatField()),
            ],
        ),
    ]