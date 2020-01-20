# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 06:52
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("caluma_form", "0009_auto_20190321_1722")]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={"abstract": False},
        ),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("multiple_choice", "multiple_choice"),
                    ("integer", "integer"),
                    ("float", "float"),
                    ("date", "date"),
                    ("choice", "choice"),
                    ("textarea", "textarea"),
                    ("text", "text"),
                    ("table", "table"),
                    ("form", "form"),
                    ("file", "file"),
                ],
                max_length=15,
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="file",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="caluma_form.File",
            ),
        ),
    ]