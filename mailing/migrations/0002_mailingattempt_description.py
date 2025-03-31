

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailingattempt",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
