from custom_acc.models import *


def check_code_valid(unique_code):
    """
    Check uniq referral link
    :param unique_code:
    :return: True/False
    """
    ref_link = ReferralLinks.objects.filter(referral_id=unique_code).first()
    if ref_link:
        return True
    else:
        return False


def extract_unique_code(text):
    """
    Extracts the unique_code from the sent /start command
    :param text:
    :return: unique referral code
    """
    return text.split()[1] if len(text.split()) > 1 else None


def get_super_code(username):
    """
    Get SuperCode by username telegram user
    :param username: username telegram user
    :return: user's SuperCode/Для Вас пока ничего нету :(
    """
    bot_user = BotUsers.objects.filter(user_name=username).first()
    if bot_user:
        return bot_user.super_code
    else:
        return 'Для Вас пока ничего нету :('
