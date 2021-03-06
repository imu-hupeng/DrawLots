# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=200)),
                ('user_group', models.IntegerField()),
                ('add_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrawResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Draw')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('user_type', models.IntegerField()),
                ('user_group', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='drawresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
    ]
