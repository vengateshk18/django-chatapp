# Generated by Django 4.2.6 on 2023-10-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
