# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-10 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KodePeralatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_alat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LapakKerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lapak', models.CharField(max_length=50)),
                ('availabilitas', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeralatanKerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_alat', models.CharField(max_length=50)),
                ('availabilitas', models.BooleanField(default=True)),
                ('kodealat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectshop.KodePeralatan')),
            ],
        ),
    ]