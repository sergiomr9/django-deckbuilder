# Generated by Django 4.0.9 on 2023-02-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deckbuilder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='attribute',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='digi_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='stage',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]