# Generated by Django 4.1.6 on 2023-05-18 13:06

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_delete_examcenter_delete_myexamcenter'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('student', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
        ),
    ]
