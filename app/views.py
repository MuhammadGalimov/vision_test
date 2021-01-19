from django.shortcuts import render
from django.http import HttpResponse
from .models import BlockFormModel, BlockTextModel, BlockHeadingModel, BlockSectionModel
from .forms import MailForm


def main_view(request):
    heading = BlockHeadingModel.objects.get(pk=1)
    section = BlockSectionModel.objects.get(pk=1)
    text = BlockTextModel.objects.get(pk=1)

    context = {
        'heading': {
            'title': heading.title,
            'desc': heading.description,
            'btn_text': heading.buttonText,
            'img': heading.img,
            'back': heading.background_color,
        },
        'section': {
            'title': section.title,
            'subtitle': section.subtitle,
            'desc': section.description,
            'img': section.img,
            'back': section.background_color,
        },
        'text': {
            'text': text.text,
            'img': text.img,
            'back': text.background_color,
        },
        'form': form,
    }

    return render(request, 'index.html', context=context)
