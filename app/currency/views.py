from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView,
)
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactForm


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(LoginRequiredMixin, CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')

    def get_object(self, queryset=None):
        return self.request.user.is_superuser


class RateUpdateView(LoginRequiredMixin, UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')

    def get_object(self, queryset=None):
        return self.request.user.is_superuser


class RateDetailView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'

    def get_object(self, queryset=None):
        return self.request.user


class RateDeleteView(LoginRequiredMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def get_object(self, queryset=None):
        return self.request.user.is_superuser


class ContactListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact.html'


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact_create.html'
    success_url = reverse_lazy('currency:contact-list')


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


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    queryset = get_user_model().objects.all()
    model = get_user_model()
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy("index")
    fields = (
        'first_name',
        'last_name'
    )

    def get_object(self, queryset=None):
        return self.request.user
