

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0012_client_owner_mailing_owner_message_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["-start_time"],
                "permissions": [
                    ("can_view_mailing", "can view mailing"),
                    ("can_edit_mailing", "can edit mailing"),
                ],
                "verbose_name": "Mailing",
                "verbose_name_plural": "Mailings",
            },
        ),
    ]
