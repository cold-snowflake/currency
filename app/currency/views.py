from django.shortcuts import render
from django.http.response import HttpResponse
from currency.models import Rate, ContactUs

def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell},'
            f'created: {rate.created}, currency type:" {rate.currency_type}, source:{rate.source}<br>'
        )
    return HttpResponse(str(results))


def contact_list(request):
    result = []
    contacts = ContactUs.objects.all()

    for contact in contacts:
        result.append(
            f'ID: {contact.id}, email_from: {contact.email_from}, subject: {contact.subject}, message: {contact.message}'
        )
    return HttpResponse(str(result))
        