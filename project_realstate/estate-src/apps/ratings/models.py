from django.db import models
from django.utils.translation import ugettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimestampUUIDModel
from apps.profiles.models import Profile

class Rating(TimestampUUIDModel):
    
    class Range(models.IntegerChoices):
        RATING_1 = 1, _('1 - Very bad')
        RATING_2 = 2, _('2 - Bad')
        RATING_3 = 3, _('3 - Good') 
        RATING_4 = 4, _('4 - Very good')
        RATING_5 = 5, _('5 - Excellent')
        
    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_('User providing the rating'),
        on_delete=models.SET_NULL, 
        null=True
    )
    agent = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_('Agent being rated'),
        related_name='agent_review',
        on_delete=models.SET_NULL,
        null=True
    )
    rating = models.IntegerField(
        verbose_name=_('Rating'),
        choices=Range.choices,
        help_text="1=very bad, 2=bad, 3=good, 4=very good, 5=excellent"
    )
    comment = models.TextField(verbose_name=_('Comment'))
    
    class Meta:
        unique_together = ['rater', 'agent']
        
    def __str__(self):
        return f"{self.agent} rated at {self.rating}"