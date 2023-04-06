# Generated by Django 4.2 on 2023-04-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('third_name', models.CharField(max_length=255)),
                ('j_b', models.FileField(upload_to='J_D')),
                ('job', models.CharField(max_length=255)),
            ],
        ),
    ]
