# Generated by Django 4.1.2 on 2022-12-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthtracker', '0002_remove_suggested_levels_max_protein_intake_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggested_levels',
            name='max_protein_intake',
        ),
        migrations.AlterField(
            model_name='food',
            name='food_name',
            field=models.CharField(max_length=200),
        ),
    ]