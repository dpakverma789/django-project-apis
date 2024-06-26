# Generated by Django 3.2.14 on 2022-08-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(max_length=20)),
                ('show_name', models.CharField(max_length=50)),
                ('show_time', models.DateTimeField()),
                ('total_seats', models.IntegerField()),
                ('reserved_seats', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
