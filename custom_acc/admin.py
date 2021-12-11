from django.contrib import admin

from custom_acc.models import (BotUsers,
                               ReferralLinks)


admin.site.register(BotUsers)
admin.site.register(ReferralLinks)
