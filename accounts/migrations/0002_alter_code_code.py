# Generated by Django 5.1.2 on 2024-10-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
