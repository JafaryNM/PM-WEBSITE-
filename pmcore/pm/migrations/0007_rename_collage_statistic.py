# Generated by Django 4.0.3 on 2022-04-12 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0006_remove_collage_college_allumn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collage',
            new_name='Statistic',
        ),
    ]