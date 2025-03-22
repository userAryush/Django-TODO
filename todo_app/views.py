from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

# we get objects when we request
# but we need to send json or http when we send response
# request is compulsory to be taken as param in every views and sending a reponse is also necessary


# home view will take the request(when we hit home page url a request is made) that user makes and display home page in resposne
def home(request):
    
    # query to bring all the data of Todo model database's table
    todo_obj = Todo.objects.all()
    
    # data = {'todo': todo_obj} → You cannot send the variable's data directly.The reason is that if you send the data to the frontend without assigning a key, how will the frontend call or access it? That's why we assign a key before sending the data.
    data = {'todos':todo_obj}
    
    # render sends the html file as response
    # using context param we send data to the html file
    return render(request,'home.html', context =data)

    #  Todo.objects.all()-> Since we are querying using an object, all the retrieved data will be in the form of objects. The objects belong to the class that we are calling (in this case, the Todo model).
    # before when fetching data from the database, the data used to come in raw form as tuples. Accessing values required using indexes, which was difficult. 
    # But now, by using objects, all the data comes as objects, making it easy to access attributes directly.


# frontend will send data to backend using POST request in json format when clicked on submit and then using this data we will create a new Todo object in database by querying
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')# data comes in request.POST from which we will get the data of fields
        task = request.POST.get('task')# name="" value in input is used as key to get data
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        
        if deadline == "":
            deadline = None
        
        # this method will create a new object in database 
        # keys are attributes of model and values are the data we get through request
        Todo.objects.create(name=name,task=task,status=status,deadline_day= deadline)
        return redirect('home')
    return render(request,'create.html')

# we sent pk in url then we also need to get it in views through param
def edit(request,pk):
    # get(id=pk) will only fetch pk data from database
    todo_obj = Todo.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        task = request.POST.get('task')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        
        todo_obj.name= name
        todo_obj.task = task
        todo_obj.status = status
        todo_obj.deadline_day = deadline
        
        if deadline == "":
            todo_obj.deadline_day = None
        
        todo_obj.save()
        return redirect('home')
    
    data = {'todo':todo_obj}
        
    return render(request,'edit.html', context = data)

def delete(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    # todo_obj  = Todo.objects.filter(name="Aryush") # this will return all the objects that have name as Aryush and we can delete them all
    todo_obj.delete()
    return redirect('home')

def delete_all(request):
    todo_obj = Todo.objects.all()
    todo_obj.delete()
    return redirect('home')
