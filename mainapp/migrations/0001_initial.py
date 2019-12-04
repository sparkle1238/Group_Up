# Generated by Django 3.0 on 2019-12-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Group name')),
                ('profile_photo', models.ImageField(upload_to='group_photo', verbose_name='Group profile photo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=30, verbose_name='Nick name')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('profile_photo', models.ImageField(upload_to='user_photo', verbose_name='User profile photo')),
            ],
        ),
    ]