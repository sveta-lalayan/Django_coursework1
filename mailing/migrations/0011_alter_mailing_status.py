

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0010_remove_mailing_actual_start_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("started", "Активна"),
                    ("completed", "Завершена"),
                ],
                default="created",
                max_length=10,
                verbose_name="статус",
            ),
        ),
    ]
