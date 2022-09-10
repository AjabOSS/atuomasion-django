from django.shortcuts import render
from .models import Letter
from django.views.generic import ListView , DetailView , TemplateView
from django.views.generic.edit import UpdateView , DeleteView  , CreateView
from django.urls import reverse_lazy


class LetterCreateView(CreateView):
    model = Letter
    template_name = "letter/letter_create.html"
    fields = ('title', 'description', 'target', 'file', 'author') #, 
    success_url = reverse_lazy('letter_inbox')

# class LetterDetailView(DetailView):
#     model = Letter
#     template_name = 'letter/letter_detail.html'

def message_view(request, pk):
    message = Letter.objects.get(id=pk)
    message.read = True
    message.save()

    return render(request, 'letter/letter_detail.html')
        

class LetterUpdateView(UpdateView):
    model = Letter
    fields = ('allow_for_l_1',)
    template_name = 'letter/letter_edit.html'
    success_url = reverse_lazy('letter_inbox')

def home_view(request):
    letter = Letter.objects.all()
    context = {
        "letter" : letter
    }
    return render(request, "home.html", context)


def letter_inbox(request):
    letter = Letter.objects.all()
    context = {
        "letter" : letter
    }
    return render(request, "letter/letter_inbox.html", context)