import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from currency import consts
from currency.choices import RateCurrencyChoices
from currency.utils import to_2_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    # source = Source.objects.filter(code_name=consts.PRIVATBANK_CODE_NAME).first()
    # if source is None:
    #     source = Source.objects.create(code_name=consts.PRIVATBANK_CODE_NAME, name='PrivatBank')

    source, _ = Source.objects.get_or_create(
        code_name=consts.PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank'
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR
    }

    for rate in rates:
        buy = to_2_decimal(rate['buy'])
        sale = to_2_decimal(rate['sale'])
        currency = rate['ccy']

        if currency not in available_currencies:
            continue

        currency = available_currencies[currency]

        last_rate = Rate.objects.filter(source=source, currency=currency)\
            .order_by('-created')\
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sale:
            Rate.objects.create(
                buy=buy,
                sell=sale,
                source=source,
                currency=currency
            )


@shared_task
def send_email_to_background(subject, message):
    from time import sleep
    recipient = settings.EMAIL_HOST_USER
    sleep(20)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False
    )
