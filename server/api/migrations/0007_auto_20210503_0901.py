# Generated by Django 3.1.8 on 2021-05-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_addr_isprivate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='pluginEnabled',
            new_name='modulesEnabled',
        ),
    ]
