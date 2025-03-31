

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0008_remove_mailing_actual_end_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="actual_end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="mailing",
            name="actual_start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
