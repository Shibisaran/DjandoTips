from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tip
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class TipListView(ListView):
    model = Tip
    template_name = 'tips/home.html'
    context_object_name = 'tips'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        if category:
            context['tips'] = Tip.objects.filter(category=category)
        context['categories'] = dict(Tip.CATEGORY_CHOICES)
        return context

class TipDetailView(DetailView):
    model = Tip
    template_name = 'tips/tip_detail.html'
    context_object_name = 'tip'

    def post(self, request, *args, **kwargs):
        tip = self.get_object()
        tip.upvotes += 1
        tip.save()
        return redirect('tips:tip_detail', pk=tip.pk)

class TipCreateView(CreateView):
    model = Tip
    template_name = 'tips/add_tip.html'
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('tips:home')

    def form_valid(self, form):
        messages.success(self.request, 'Tip added successfully!')
        return super().form_valid(form)
