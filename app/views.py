from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import BlockFormModel, BlockTextModel, BlockHeadingModel, BlockSectionModel, MailsModel
from .forms import MailForm


def main_view(request):
    heading = BlockHeadingModel.objects.get(pk=1)
    section = BlockSectionModel.objects.get(pk=1)
    text = BlockTextModel.objects.get(pk=1)
    formblock = BlockFormModel.objects.get(pk=1)
    form = MailForm()

    if request.method == 'POST':
        form = MailForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']

            # высылаем письмо
            send_mail(subject='Письмо из сайта',
                      message='Имя: {}\nТелефон: {}\n'.format(name, phone) + text,
                      from_email=email,
                      recipient_list=['kakasi.muham@gmail.com'],
                      fail_silently=False)

            # заносим данные в базу
            m = MailForm.objects.create(email=email, name=name, phone=phone, text=text)

            return HttpResponseRedirect('/')

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
        'form': {
            'btn_text': formblock.buttonText,
        },
        'Form': form,
    }

    return render(request, 'index.html', context=context)
