# Generated by Django 4.2.14 on 2024-07-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminground', '0003_bloglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
