# Generated by Django 4.0.9 on 2023-02-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deckbuilder', '0003_alter_card_cardrarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
