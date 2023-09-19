from django.shortcuts import render, redirect
from .models import Message, Room
from django.http import HttpResponse, JsonResponse

# Create your views here.
# endpoint ke end mein '/?username=' = aata hai


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    # getting perticular modele from db which has the name room
    room_details = Room.objects.get(name=room)
    # Now the the room_details username etc to the room.html file
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    # check if the room already exist
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    # save this data i.e message, username, room_id to the db
    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    # we dont render or go to page we just go back to the rooms page as we stay there only
    return HttpResponse('sent')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
