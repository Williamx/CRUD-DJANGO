# Generated by Django 3.1.5 on 2021-01-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
