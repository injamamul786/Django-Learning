# Generated by Django 4.1.6 on 2023-05-18 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.examcenter',),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
