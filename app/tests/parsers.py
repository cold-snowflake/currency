from unittest.mock import MagicMock
from currency.tasks import parse_privatbank, parse_monobank
from currency.models import Rate, Source
from currency.choices import RateCurrencyChoices
from currency import consts
import json


def test_parse_privatbank(mocker):
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.43920", "sale": "42.01681"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"}
    ]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
        )

    intial_count = Rate.objects.count()
    parse_privatbank()

    assert Rate.objects.count() == intial_count + 2
    assert request_get_mock.call_count == 1
    assert request_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'


def test_privatbank_parser_prevent_duplicates(mocker):
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.43920", "sale": "42.01681"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"}
    ]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )
    source = Source.objects.get(code_name=consts.PRIVATBANK_CODE_NAME)
    Rate.objects.create(buy='39.43', sell='42.01', source=source, currency=RateCurrencyChoices.EUR)
    Rate.objects.create(buy='36.56', sell='37.45', source=source, currency=RateCurrencyChoices.USD)

    intial_count = Rate.objects.count()

    parse_privatbank()

    assert Rate.objects.count() == intial_count + 2


with open("app/tests/fixtures/monobank.json", "r") as f:
    monobank_data = json.load(f)


def test_parse_monobank(mocker):
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
        )

    intial_count = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == intial_count + 2
    assert request_get_mock.call_count == 1
    assert request_get_mock.call_args[0][0] == 'https://api.monobank.ua/bank/currency'


def test_monobank_parser_prevent_duplicates(mocker):
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )
    source = Source.objects.get(code_name=consts.MONO_BANK_CODE_NANE)
    Rate.objects.create(buy='39.43', sell='42.01', source=source, currency=RateCurrencyChoices.EUR)
    Rate.objects.create(buy='36.56', sell='37.45', source=source, currency=RateCurrencyChoices.USD)

    intial_count = Rate.objects.count()

    parse_monobank()

    assert Rate.objects.count() == intial_count + 2
