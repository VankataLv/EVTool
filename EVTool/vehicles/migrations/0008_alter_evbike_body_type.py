# Generated by Django 5.1.3 on 2024-11-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_alter_evcar_body_type_alter_evcar_drivetrain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evbike',
            name='body_type',
            field=models.CharField(choices=[('ATV', 'ATV'), ('Roadster', 'Roadster'), ('Cross', 'Cross'), ('Track', 'Track'), ('Тricycle', 'Тricycle')], default='unknown', max_length=15),
        ),
    ]
