# Generated by Django 4.2.14 on 2024-07-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='landing_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='statc/forntpage/images')),
            ],
        ),
    ]
