# Generated by Django 3.2.16 on 2022-12-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_create_eatreport_nightreport_walkreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('is_checked_by_staff', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]