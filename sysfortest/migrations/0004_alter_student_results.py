# Generated by Django 4.2.15 on 2025-03-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysfortest', '0003_alter_student_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='results',
            field=models.JSONField(default={'primer': [], 'slova': []}),
        ),
    ]
