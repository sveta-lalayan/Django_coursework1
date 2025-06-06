

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0007_alter_message_body_alter_message_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailing",
            name="actual_end_time",
        ),
        migrations.RemoveField(
            model_name="mailing",
            name="actual_start_time",
        ),
        migrations.AlterField(
            model_name="client",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="комментарий"),
        ),
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="e-mail адрес"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="full_name",
            field=models.CharField(max_length=255, verbose_name="Ф.И.О клиента"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="clients",
            field=models.ManyToManyField(to="mailing.client", verbose_name="клиенты"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="description",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="описание"
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing.message",
                verbose_name="сообщение",
            ),
        ),
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
                verbose_name="периодичность",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="start_time",
            field=models.DateTimeField(verbose_name="дата начала рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("started", "Запущена"),
                    ("completed", "Завершена"),
                ],
                default="created",
                max_length=10,
                verbose_name="статус",
            ),
        ),
    ]
