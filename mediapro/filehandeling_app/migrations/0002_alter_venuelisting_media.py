# Generated by Django 4.0.5 on 2022-06-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filehandeling_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuelisting',
            name='media',
            field=models.FileField(blank=True, default='media/default.jpg', null=True, upload_to='media'),
        ),
    ]