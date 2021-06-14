from django.db import models


class LottoCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Lotto category'
        verbose_name_plural = 'Lotto categories'

    def __str__(self):
        return self.name


class LottoResultItem(models.Model):
    category = models.ForeignKey(
        LottoCategory,
        related_name='items',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    number = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Lotto result'
        verbose_name_plural = 'Lotto results'

    def __str__(self):
        return f'{self.category} {self.date} {self.number}'


class LottoResultNumber(models.Model):
    number = models.PositiveSmallIntegerField()
    result = models.ForeignKey(
        LottoResultItem,
        related_name='numbers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('number', 'result')

        verbose_name = 'Lotto result number'
        verbose_name_plural = 'Lotto result numbers'

    def __str__(self):
        return f'{self.number}'
