from django.shortcuts import render, redirect
from .models import SecretToken
import openai

# Create your views here.


def search_page_gpt(request):
    searched_text = request.GET.get('searched_text')
    response_text = None
    if searched_text:
        openai.api_key = SecretToken.objects.all().first().token
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=searched_text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["text"]
    print(response_text)
    context = {'searched_text': searched_text, 'response_text': response_text}
    return render(request, "search_page.html", context)
