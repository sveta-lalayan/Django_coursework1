

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0009_mailing_actual_end_time_mailing_actual_start_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailing",
            name="actual_start_time",
        ),
        migrations.AlterField(
            model_name="mailing",
            name="actual_end_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="дата завершения рассылки"
            ),
        ),
    ]
