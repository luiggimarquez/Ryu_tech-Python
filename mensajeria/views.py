from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from .models import ChatRoom, MessagesChat
from users.models import Profile
from django.contrib.auth.decorators import login_required 
from django.http import  HttpResponse
from django.contrib import messages

@login_required 
def usersProfile(request):

    canDelete=False
    if (request.user.has_perm('blog.can_delete')):
        canDelete=True 
    users= User.objects.all()

    if(request.method == "POST"):
        id=request.POST['id']
        access=request.POST['permiso']

        user = User.objects.get(id=id)
        user.user_permissions.clear()
        user.user_permissions.add(Permission.objects.get(codename=access))
        user.save()
        messages.success(request, f"Permiso '{access}' asignado con éxito")


    return render(request, 'mensajeria/profilesMessages.html',{
        'usuarios':users, 'canDelete':canDelete})


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

    messages = MessagesChat.objects.all()

    message=[]
    for filterMessage in messages:
        
        if((filterMessage.sender.username == user.username) and (filterMessage.receiver.username == receiver.username)):
            message.append({'message':filterMessage.message,'sender':filterMessage.sender.username})
    
        if((filterMessage.receiver.username == user.username) and (filterMessage.sender.username == receiver.username)):
            message.append({'message':filterMessage.message, 'receiver':filterMessage.sender.username})
   
    return render(request, 'mensajeria/chatRoom.html', {'messages': message, 'id': id, 'receiver':receiver})

 
@login_required 
def sendMessage(request):
    from django.db.models import Q
    user = request.user

    if (request.method == 'POST'):
        message = request.POST['message'] 
        receiver_id = request.POST['receiver']

        receiver = User.objects.get(id=receiver_id)
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