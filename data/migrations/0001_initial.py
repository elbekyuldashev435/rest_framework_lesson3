# Generated by Django 5.0.4 on 2024-05-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]