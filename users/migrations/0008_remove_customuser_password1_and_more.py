# Generated by Django 4.1 on 2022-08-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_password1_customuser_password2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
