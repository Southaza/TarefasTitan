from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import sitev


class SitevListView(ListView):
    model= sitev


class SitevCreateView(CreateView):
    model= sitev
    fields= ["title", "deadline"]
    success_url= reverse_lazy("sitev_list")
    

class SitevUpdateView(UpdateView):
    model= sitev
    fields=["title", "deadline"]
    success_url= reverse_lazy("sitev_list")

class SitevDeleteView(DeleteView):
    model= sitev
    success_url= reverse_lazy("sitev_list")

class SitevCompleteView(View):
    def get(self, request, pk):
        sitevs = get_object_or_404(sitev, pk=pk)
        sitevs.Mark_has_complete()
        return redirect("sitev_list")


