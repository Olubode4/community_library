# Generated by Django 3.2.20 on 2024-01-11 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='cover_logo/%Y/%m/%d/'),
        ),
    ]
