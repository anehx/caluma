# Generated by Django 4.2.10 on 2024-05-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("caluma_form", "0047_alter_answer_documents"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaloption",
            name="is_hidden",
            field=models.TextField(default="false"),
        ),
        migrations.AddField(
            model_name="option",
            name="is_hidden",
            field=models.TextField(default="false"),
        ),
    ]
