# Generated by Django 3.2.16 on 2022-12-09 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_create_walk'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0004_create_eatwanttovisit_nightwanttovisit_walkwanttovisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalkReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('is_checked_by_staff', models.BooleanField(default=False)),
                ('place', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='places.walk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NightReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('is_checked_by_staff', models.BooleanField(default=False)),
                ('place', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='places.night')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EatReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('is_checked_by_staff', models.BooleanField(default=False)),
                ('place', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='places.eat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]