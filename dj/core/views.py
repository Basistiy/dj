from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Contacts
from core.serializers import ContactSerializer


def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def contact(request):

    if request.method == 'GET':
        print('get fired')
        note = Contacts.objects.all()
        serializer = ContactSerializer(note, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        print('post fired')
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            print("saving the contact...")
            serializer.save()
        return render(request, "index.html")
