

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0006_alter_mailing_periodicity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="body",
            field=models.TextField(blank=True, null=True, verbose_name="Сообщение"),
        ),
        migrations.AlterField(
            model_name="message",
            name="subject",
            field=models.CharField(max_length=255, verbose_name="Тема"),
        ),
    ]
