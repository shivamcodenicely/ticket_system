# Generated by Django 2.0.3 on 2018-03-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.IntegerField(default=0)),
                ('address1', models.TextField(blank=True, default='', null=True)),
                ('city', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('zipcode', models.IntegerField(blank=True, default=0, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]