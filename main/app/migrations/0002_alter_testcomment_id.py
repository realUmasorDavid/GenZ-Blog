# Generated by Django 5.1 on 2024-08-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
