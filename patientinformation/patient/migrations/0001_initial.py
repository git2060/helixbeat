# Generated by Django 5.1.4 on 2024-12-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_of_field', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
            ],
        ),
    ]
