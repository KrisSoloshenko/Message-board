from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .models import Ad, UserResponse
from .forms import AdForm, DeleteForm, UserResponseForm, DeleteResponseForm
from .filters import AuthorProfileFilter


class AdList(ListView):
    model = Ad
    template_name = 'ads.html'
    context_object_name = 'ads'
    ordering = '-creation_time'
    paginate_by = 5


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_respones'] = UserResponse.objects.filter(ad=self.kwargs['pk'])
        return context
    

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
        if ad.author == self.request.user:
            true_form = super().form_valid(form)
            return true_form
        raise PermissionDenied()
    

class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    form_class = DeleteForm
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_list')
    raise_exception = True
    
    def form_valid(self, form):
        if self.get_object().author == self.request.user:
            messages.success(self.request, "Объявление успешно удалено")
            return super(AdDelete, self).form_valid(form)
        raise PermissionDenied()


class UserResponseCreate(LoginRequiredMixin, CreateView):
    model = UserResponse
    form_class = UserResponseForm
    template_name = 'user_response_create.html'
    context_object_name = 'user_response'
    success_url = reverse_lazy('responses_list')
    raise_exception = True

    def form_valid(self, form):
        user_response = form.save(commit=False)
        user_response.user = self.request.user
        user_response.ad_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_id'] = Ad.objects.get(pk=self.kwargs['pk'])
        return context
    

class UserResponseList(LoginRequiredMixin, ListView):
    model = UserResponse
    template_name = 'user_responses.html'
    context_object_name = 'responses'
    ordering = '-creation_time'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_respones'] = UserResponse.objects.filter(user=self.request.user)
        return context
    
class UserResponseDelete(LoginRequiredMixin, DeleteView):
    model = UserResponse
    form_class = DeleteResponseForm
    template_name = 'user_response_delete.html'
    success_url = reverse_lazy('responses_list')
    raise_exception = True
    

class ProfileFilter(LoginRequiredMixin, ListView):
    model = UserResponse
    template_name = 'author_profile.html'
    ordering = '-creation_time'
    context_object_name = 'profile_responses'
    paginate_by = 5

    def get_queryset(self):
        queryset = UserResponse.objects.filter(ad__author__id=self.request.user.id)
        self.filterset = AuthorProfileFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context
    

@login_required
@csrf_protect
def confirm_response(request, **kwargs):
    if request.method == 'POST':
        user_response = UserResponse.objects.get(id=kwargs['pk'])
        action = request.POST.get('action')

        if action == 'confirm':
            user_response.status = True
            user_response.save()

    return redirect(request.META['HTTP_REFERER'])
    