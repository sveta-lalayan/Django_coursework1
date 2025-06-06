

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("full_name", models.CharField(max_length=255)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Mailing",
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
                ("start_time", models.DateTimeField()),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("daily", "Daily"),
                            ("weekly", "Weekly"),
                            ("monthly", "Monthly"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("started", "Запущена"),
                            ("completed", "Завершена"),
                        ],
                        default="created",
                        max_length=10,
                    ),
                ),
                ("actual_start_time", models.DateTimeField(blank=True, null=True)),
                ("actual_end_time", models.DateTimeField(blank=True, null=True)),
                ("clients", models.ManyToManyField(to="mailing.client")),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.message",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mailing",
                "verbose_name_plural": "Mailings",
                "ordering": ["-start_time"],
            },
        ),
        migrations.CreateModel(
            name="MailingAttempt",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "Успешно"), ("failed", "Не успешно")],
                        max_length=10,
                    ),
                ),
                ("server_response", models.TextField(blank=True, null=True)),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempts",
                        to="mailing.mailing",
                    ),
                ),
            ],
        ),
    ]
