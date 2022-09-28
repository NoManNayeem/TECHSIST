# Generated by Django 4.1 on 2022-09-28 11:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Discount_App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="discount",
            name="end_time",
            field=models.TimeField(
                default=datetime.datetime(2022, 9, 28, 17, 28, 45, 283585)
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="start_time",
            field=models.TimeField(
                default=datetime.datetime(2022, 9, 28, 17, 28, 45, 283585)
            ),
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("price", models.IntegerField(default=0)),
                ("stock", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Discount_App.category",
                    ),
                ),
                (
                    "discount",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Discount_App.discount",
                    ),
                ),
            ],
        ),
    ]