# Generated by Django 4.1.6 on 2023-05-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_myexamcenter_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='ExamCenter',
        ),
        migrations.DeleteModel(
            name='MyExamCenter',
        ),
    ]
