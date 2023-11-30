from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignupPokeView(CreateView):
    form_class=CustomUserCreationForm
    template_name="signup_poke.html"
    success_url=reverse_lazy('accounts:signup_poke_success')
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignupPokeSuccessView(TemplateView):
    template_name = 'signup_poke_success.html'
    
