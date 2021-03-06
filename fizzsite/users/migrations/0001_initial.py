# Generated by Django 3.0.3 on 2020-02-09 13:04

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
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.BooleanField(default='True')),
                ('q2', models.BooleanField(default='True')),
                ('q3', models.BooleanField(default='True')),
                ('q4', models.BooleanField(default='True')),
                ('q5', models.BooleanField(default='True')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Full Name', max_length=20)),
                ('location', models.CharField(default='Location', max_length=50)),
                ('age', models.PositiveSmallIntegerField(default=18)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('bio', models.TextField(default='Max 500 characters.', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
