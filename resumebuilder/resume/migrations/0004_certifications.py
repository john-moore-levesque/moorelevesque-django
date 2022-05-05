# Generated by Django 3.2.13 on 2022-05-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
