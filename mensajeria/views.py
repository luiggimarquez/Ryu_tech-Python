from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ChatRoom, MessagesChat
from users.models import Profile
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect, HttpResponse  

def usersChat(request):

    users= Profile.objects.all()
    print(users)
    return render(request, 'mensajeria/profilesMessages.html',{'usuarios':users})


@login_required 
def getMessages(request, id):
    user = request.user
    receiver = User.objects.get(id=id)
    
    
    chat_rooms = ChatRoom.objects.filter(users__in=[user, receiver])
    
    if chat_rooms.exists():
        chat_room = chat_rooms.first()
    else:
        chat_room = ChatRoom.objects.create()
        chat_room.users.add(user, receiver)
    
    
    #messages = MessagesChat.objects.filter(chatroom=chat_room)
    #messages = MessagesChat.objects.filter(sender=request.user, receiver=id)
    messages = MessagesChat.objects.all()

    print(messages)

    message=[]
    for filterMessage in messages:
        print(type(filterMessage.sender.username))
        print(filterMessage.receiver)
        print(filterMessage.message)
        print("username: ",type(user.username))
        print("receiver: ",receiver.username)
        print("primera condicion", (filterMessage.sender.username == user.username) and (filterMessage.receiver.username == receiver.username))
        if((filterMessage.sender.username == user.username) and (filterMessage.receiver.username == receiver.username)):
            #message['sender']= filterMessage.message
            message.append({'message':filterMessage.message,'sender':filterMessage.sender.username})
            print("datoS: ",message)
        if((filterMessage.receiver.username == user.username) and (filterMessage.sender.username == receiver.username)):
            #message['receiver']= filterMessage.message
            message.append({'message':filterMessage.message, 'receiver':filterMessage.sender.username})
            print("datoR: : ",message)
        print("sender/receiver: ", message)


    
   

    
    #messages = MessagesChat.objects.filter(a=chat_room)
    #messages = MessagesChat.objects.filter()
    print(request.user.id)
    return render(request, 'mensajeria/chatRoom.html', {'messages': message, 'id': id, 'receiver':receiver})

 
@login_required 
def sendMessage(request):
    from django.db.models import Q
    user = request.user

    if (request.method == 'POST'):
        message = request.POST['message'] 
        receiver_id = request.POST['receiver']

        try:
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            # Manejar el caso si el usuario receptor no existe
            return HttpResponse("User does not exist.")

    


        chat_room = ChatRoom.objects.filter(Q(users=user) & Q(users=receiver)).first()

        if not chat_room:
            # Si la sala de chat no existe, crearla
            chat_room = ChatRoom.objects.create()
            chat_room.users.add(user, receiver)
            
        message = MessagesChat.objects.create(sender=request.user, receiver=receiver, message=message) 

        #chat_rooms = ChatRoom.objects.get((Q(users=user.id) & Q(users=receiver_id)))
        chat_room.messages.add(message) 

        return redirect('chatroom-getmsgs',  id=receiver_id)
    else:
        return HttpResponse("Invalid request method.")
