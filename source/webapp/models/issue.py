from django.db import models


class Issue(models.Model):
    summary = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Подробное описание'
    )
    status = models.ForeignKey(
        'webapp.Status',
        related_name='statuses',
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='types',
        blank=True,
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
        null=True
    )

    def __str__(self):
        return f'{self.summary} - {self.description}'
