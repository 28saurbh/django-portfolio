# Generated by Django 3.1.2 on 2020-10-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_auto_20201030_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
