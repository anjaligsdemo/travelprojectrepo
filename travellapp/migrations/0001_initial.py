# Generated by Django 4.1.3 on 2022-11-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('banner', models.ImageField(upload_to='home_images')),
                ('description', models.TextField()),
            ],
        ),
    ]
