from django.shortcuts import get_object_or_404, render

from .models import CardDatas, CardTexts

def home(request):
    return render(request, 'index.html')

def index(request):
    card_list = CardTexts.objects.all()
    context = {'card_list': card_list}
    return render(request, 'ygo_db/index.html', context)

def detail(request, id):
    card_text = get_object_or_404(CardTexts, pk=id)
    card_data = get_object_or_404(CardDatas, pk=id)
    return render(request, 'ygo_db/detail.html', {'card_text': card_text, 'card_data': card_data})

