# Generated by Django 4.0.2 on 2022-03-12 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyStudent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('student.student',),
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
    ]
