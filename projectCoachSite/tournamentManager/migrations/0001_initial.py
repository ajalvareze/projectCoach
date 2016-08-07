# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200, verbose_name='ubicacion')),
                ('date', models.DateTimeField(verbose_name='fecha')),
                ('result1', models.PositiveIntegerField()),
                ('result2', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('DFB', models.CharField(max_length=200)),
                ('matches', models.ManyToManyField(to='tournamentManager.Match')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='tournamentManager.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='tournamentManager.Team'),
        ),
    ]
