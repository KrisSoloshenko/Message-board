from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Ad
from .forms import AdForm, DeleteForm

class AdList(ListView):
    model = Ad
    template_name = 'ads.html'
    context_object_name = 'ads'
    ordering = '-creation_time'
    paginate_by = 10


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    

class AdCreate(LoginRequiredMixin, CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'
    raise_exception = True
    
    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        return super().form_valid(form)
    

class AdUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_update.html'
    raise_exception = True

    def form_valid(self, form):
        ad = form.save(commit=False)
        current_id = ad.id
        if ad.author == self.request.user:
            true_form = super().form_valid(form)
            return true_form
        return redirect(to=f'/ads/')
    

class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    form_class = DeleteForm
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_list')
    raise_exception = True

