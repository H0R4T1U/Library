# Generated by Django 3.2 on 2021-06-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='extra',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
