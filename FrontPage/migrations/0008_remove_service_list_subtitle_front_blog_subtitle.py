# Generated by Django 4.2.14 on 2024-07-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontPage', '0007_service_list_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_list',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='front_blog',
            name='subtitle',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
