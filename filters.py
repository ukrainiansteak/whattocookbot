from telegram.ext import MessageFilter
import re


class FilterCooking(MessageFilter):
    def filter(self, message):
        return bool(re.match(r'([шщ]о )?приготувати\??', message.text))
