# Generated by Django 3.0.7 on 2020-06-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200626_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='signed_medical_form',
            field=models.BooleanField(blank=True),
        ),
    ]
