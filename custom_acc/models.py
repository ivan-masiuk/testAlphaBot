from django.db import models


class BotUsers(models.Model):
    """
    Model of bot user
    """
    user_name = models.CharField(max_length=150, default='Test Name')
    super_code = models.CharField(max_length=15, default='000AB')

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class ReferralLinks(models.Model):
    """
    Referral links model
    """
    referral_id = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Реферальная ссылка"
        verbose_name_plural = "Реферальные ссылки"
