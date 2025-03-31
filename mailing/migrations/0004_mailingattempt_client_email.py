

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_remove_mailingattempt_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailingattempt",
            name="client_email",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
