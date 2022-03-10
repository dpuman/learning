# Generated by Django 4.0.2 on 2022-02-16 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuId', models.IntegerField()),
                ('stuName', models.CharField(max_length=70)),
                ('stuEmail', models.EmailField(max_length=70)),
                ('stuPassword', models.CharField(max_length=70)),
                ('comments', models.TextField(blank=True, default='No Comments', null=True)),
            ],
        ),
    ]
