

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0004_mailingattempt_client_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailingattempt",
            name="client_email",
        ),
    ]
