# Generated by Django 5.0.2 on 2024-02-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0002_alter_headstailsresult_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=5)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RandomInt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=5)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]