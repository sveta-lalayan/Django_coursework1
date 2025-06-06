

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "slug",
                    models.CharField(max_length=200, unique=True, verbose_name="Slug"),
                ),
                ("content", models.TextField(blank=True, verbose_name="Содержание")),
                (
                    "preview_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/preview",
                        verbose_name="Изображение превью",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост в блоге",
                "verbose_name_plural": "Посты в блоге",
                "ordering": ["-created_at"],
            },
        ),
    ]
