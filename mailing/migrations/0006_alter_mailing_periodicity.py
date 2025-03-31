

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0005_remove_mailingattempt_client_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("daily", "Ежедневно"),
                    ("weekly", "Еженедельно"),
                    ("monthly", "Ежемесячно"),
                ],
                max_length=10,
            ),
        ),
    ]
