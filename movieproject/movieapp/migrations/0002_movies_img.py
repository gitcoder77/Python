# Generated by Django 4.2.8 on 2024-01-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='exit', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
