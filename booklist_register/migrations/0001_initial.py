# Generated by Django 3.0.6 on 2020-05-18 12:05

from django.db import migrations, models
import django.db.models.deletion
from django.db import connection


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publishdate', models.DateField()),
                ('pages', models.IntegerField()),
                ('booktype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booklist_register.Booktype')),
            ],
        ),
    ]
