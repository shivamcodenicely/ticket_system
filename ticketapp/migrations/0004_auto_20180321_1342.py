# Generated by Django 2.0.3 on 2018-03-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0003_admin_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='catagory',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')]),
        ),
    ]
