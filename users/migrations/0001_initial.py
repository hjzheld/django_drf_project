# Generated by Django 4.2.5 on 2023-09-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(default=False, max_length=100)),
                ('fullname', models.CharField(default=False, max_length=100)),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
