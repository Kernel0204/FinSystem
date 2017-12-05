from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def index(request):

    return render(request , 'index.html',{

    })


def add(request):
    """ユーザ情報を登録するメソッド"""
    form = userAddForm()
    title = '新規登録画面'
    return render(request, 'analyzeViewer/form.html', {
      'form': form,
      'title': title,
      'body':'form.html',
    })

def group_add(request):
    """ワークスペースを新規で登録するメソッド"""
    form = groupAddForm()
    title = 'ワークスペース登録画面'

    return render(request, 'analyzeViewer/form.html', {
        'form':form,
        'title':title,
        'body':'form.html'
    })






def edit(request):
    return HttpResponse("edit")



def delete(request):
    return HttpResponse("delete")


def saver(request):
    """Formの内容をチェックし保存するメソッド"""
    if request.method == 'POST':
        form = sexAddForm(request.POST)
        if form.is_valid():
            form.save(commit = False)
        else:
            form = sexAddForm()

    return render(request, 'index.html', {'form': form})
