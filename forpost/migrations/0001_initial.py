# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 15:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention', models.CharField(choices=[('대출완료', '대출완료'), ('회수중', '회수중'), ('회수완료', '회수완료')], default='대출완료', max_length=10)),
                ('price', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payback', models.FloatField()),
                ('lone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forpost.Lone')),
            ],
        ),
    ]