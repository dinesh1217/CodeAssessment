from django.db import models
from django.apps import apps


class Question(models.Model):
    """Model definition for Question."""
    title = models.CharField(max_length=150)
    correct_choice = models.OneToOneField('question.Choice', related_name='correct_choice',
                                        on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        """Meta definition for Question."""
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return f'{self.title}'


class Choice(models.Model):
    """Model definition for Choice."""

    value = models.CharField(max_length=50)
    question = models.ForeignKey(Question, related_name='question',on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Choice."""

        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        """Unicode representation of Choice."""
        return f'{self.value}'
