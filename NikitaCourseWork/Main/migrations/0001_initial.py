# Generated by Django 4.0.2 on 2022-02-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Prime_Numbers', models.IntegerField()),
                ('List', models.CharField(max_length=1000, null=True)),
                ('Username_Id', models.IntegerField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
