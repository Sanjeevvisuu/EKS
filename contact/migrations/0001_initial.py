# Generated by Django 5.0.2 on 2024-03-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('travel_name', models.CharField(max_length=200)),
                ('ph_no', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('wathsapp_no', models.IntegerField()),
            ],
        ),
    ]
