import os

import openai
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dotenv import load_dotenv
from django.utils import timezone

from openai import ChatCompletion

from .forms import PromptForm
from .models import ChatHistory

load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)


@login_required
def chat(request):
    interests = ''
    if request.user.participantprofile:
        for i in request.user.participantprofile.categories.all():
            interests = f'{i}, {interests}'
        messages = [
            {"role": "system",
             "content": f"К тебе обратился человек обладающий следующим списком интересов: {interests}. "
                        f"Он будет задавать тебе вопросы. Отвечай ему предельно содержательно и уважительно, исходя из его"
                        f"интересов, предоставленных тебе выше. Обращайся к нему только на 'вы'."},
        ]
    if request.method == 'POST':
        openai.api_key = api_key
        prompt_form = PromptForm(data=request.POST)
        if prompt_form.is_valid():
            prompt = prompt_form.cleaned_data['prompt']
            messages.append({"role": "user",
                             "content": prompt})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=1,
            )
            ChatHistory.objects.create(text=prompt, user=request.user, author='user', sent=timezone.now())
            result = response.choices[0].message.content
            messages.append({"role": "assistant",
                             "content": result})
            ChatHistory.objects.create(text=result, user=request.user, author='ai', sent=timezone.now())
            return render(request,
                          'chat/chat.html',
                          {'prompt_form': prompt_form,
                           'history': ChatHistory.objects.filter(user=request.user).order_by('-sent')})
    else:
        prompt_form = PromptForm()
    return render(request,
                  'chat/chat.html',
                  {'prompt_form': prompt_form,
                   'history': ChatHistory.objects.filter(user=request.user).order_by('-sent')})
