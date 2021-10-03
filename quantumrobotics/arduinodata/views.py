from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from .models import Arduino
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
        
        return context

def model(request,board):
    board_keys=[]
    for i in Arduino.BOARD:
        board_keys.append(i[0])
    if board in board_keys:
        boards = Arduino.objects.filter(board=board)
        return render(request,"arduinodata/model.html",{
                "boards":boards,
                })
    else:
        raise Http404("No contamos con tal board")