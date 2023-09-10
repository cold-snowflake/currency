from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from currency.models import Rate, ContactUs, Source, RequstResponseLog
from currency.forms import RateForm, SourceForm, ContactForm
from currency.tasks import send_email_to_background


class RateListView(ListView):
    paginate_by = 10
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


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


class ContactListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact.html'


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


class SourceListView(ListView):
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
