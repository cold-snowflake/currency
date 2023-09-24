from currency.filters import ContactUsFilter, RateFilter, SourceFilter
from currency.forms import ContactForm, RateForm, SourceForm
from currency.models import ContactUs, Rate, RequstResponseLog, Source
from currency.tasks import send_email_to_background
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_filters.views import FilterView


class RateListView(FilterView):
    paginate_by = 10
    queryset = Rate.objects.all().select_related('source')
    filterset_class = RateFilter
    template_name = 'rate_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter_params'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items()
            if key != 'page')
        return context


class RateCreateView(UserPassesTestMixin, CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateUpdateView(UserPassesTestMixin, UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactListView(FilterView):
    paginate_by = 10
    filterset_class = ContactUsFilter
    queryset = ContactUs.objects.all()
    template_name = 'contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter_params'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items()
            if key != 'page')
        return context


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact_create.html'
    success_url = reverse_lazy('currency:contact-list')

    def _send_mail(self):
        subject = "User Contact Us"
        message = f'''
        Email_from: {self.object.email_from},
        Subject: {self.object.subject},
        Message: {self.object.message}
    '''

        send_email_to_background.apply_async(
            kwargs={
                'subject': subject,
                'message': message
            },
            countdown=10
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactForm
    template_name = 'contact_update.html'
    success_url = reverse_lazy('currency:contact-list')


class ContactDeleteView(DeleteView):
    model = ContactUs
    template_name = 'contact_delete.html'
    success_url = reverse_lazy('currency:contact-list')


class ContactDetailView(DetailView):
    model = ContactUs
    template_name = 'contact_details.html'


class SourceListView(FilterView):
    paginate_by = 10
    filterset_class = SourceFilter
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'


class RequestResponseLogView(ListView):
    model = RequstResponseLog
    template_name = 'request_response_log.html'


class IndexView(TemplateView):
    template_name = 'index.html'

# def api_rate(queriset):
#     import json
#     objects = Rate.objects.all()
#     object_list = []
#     for obj in objects:
#         object_list.append({
#             'id': obj.id,
#             'buy': float(obj.buy),
#             'sell': float(obj.sell)
#         })
#     return HttpResponse(json.dumps(object_list), content_type='application/json')
