# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('zip_start', models.IntegerField()),
                ('zip_end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('pincode', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.FloatField(default=0.0)),
                ('encountered_entries', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.State'),
        ),
    ]
