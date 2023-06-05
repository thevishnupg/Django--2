# Generated by Django 4.2.1 on 2023-06-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Cover',
            field=models.ImageField(blank=True, null=True, upload_to='coverimg'),
        ),
        migrations.AlterField(
            model_name='book',
            name='PDF',
            field=models.FileField(blank=True, null=True, upload_to='pdfs'),
        ),
    ]
