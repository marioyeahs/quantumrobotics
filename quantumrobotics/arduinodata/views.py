from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import Http404, HttpResponseRedirect
from .models import Arduino, Data
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import Data
from datetime import datetime
from .models import ArduinoForm
# Create your views here.

class IndexListView(ListView):
    model=Arduino
    template_name='arduinodata/index.html'
    def get_context_data(self,**kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        board=Arduino.BOARD
        boards=[]
        boards_key=[]
        for i in range(len(board)):
            boards_key+=[board[i][0]]
            boards+=[board[i][1]]
        
        hard_by_model=[]
        for i in boards_key:
            hard_by_model+=[Arduino.objects.filter(board=i)]
        
        context['key_boards']=zip(boards_key,hard_by_model)
        context['value_boards']=zip(boards_key,boards)

        # Create the form class.
        form=context['form']=ArduinoForm()
        if form.is_valid():
            arduino = form.cleaned_data['arduino']
            print(arduino)
            sensor = form.cleaned_data['sensor']
            content = form.cleaned_data['content']
            date=datetime.today()
            data=Data(arduino=arduino,sensor=sensor,content=content,date=date)
            data.save()
            return HttpResponseRedirect(reverse('arduinodata:index'))
        
        return context

def model(request,board):
    board_keys=[]
    print(board)
    for i in Arduino.BOARD:
        board_keys.append(i[0])
    if board in board_keys:
        boards = Arduino.objects.filter(board=board)
        return render(request,"arduinodata/model.html",{
                "boards":boards,
                })
    else:
        raise Http404("No contamos con tal board")

def data(request,model_board):
    data=Data.objects.filter(arduino=model_board)
    
    return render(request, "arduinodata/data.html",{
        'data':data,
        })
