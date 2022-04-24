# Generated by Django 3.2.9 on 2021-11-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('years', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]