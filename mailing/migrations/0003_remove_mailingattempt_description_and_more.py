

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_mailingattempt_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailingattempt",
            name="description",
        ),
        migrations.AddField(
            model_name="mailing",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
