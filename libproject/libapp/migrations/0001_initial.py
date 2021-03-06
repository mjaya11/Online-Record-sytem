# Generated by Django 4.0 on 2022-05-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(default='abc@xyz.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(default='abc@xyz.com', max_length=254)),
            ],
        ),
    ]
