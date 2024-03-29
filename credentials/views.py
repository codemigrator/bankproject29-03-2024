from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect
from .models import AccountType,FromTable,Branch,CheckboxOptions,LoggedUser

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conformpassword = request.POST['password2']
        if password == conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('credentials:register')
            elif User.objects.filter(password=password).exists():
                messages.info(request,'password already exists')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

                print('user created')
                return redirect('credentials:login')

        else:
            messages.info(request, 'user not created')
            return redirect('credentials:register')
        return redirect('/')
    return render(request, 'regist.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print('loggined')

        if user is not None:
            auth.login(request, user)
            # saved_user = LoggedUser.objects.create(name=username,password=password)
            # saved_user.save()
            # if user.username in LoggedUser.name:
            # if request.session.get("details_form_completed"):
            #
            #     return redirect('/')
            # else:
            return redirect('credentials:inform')
        else:
            messages.info(request, "invalid login")
            print('invalid login')
            return redirect('credentials:login')
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def inform(request):

    return render(request, 'informpage.html')


def personal_details_form(request):
    typ = AccountType.objects.all()
    options = CheckboxOptions.objects.all()
    print("1st")

    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        choice_ids = request.POST.get('option')
        user = FromTable.objects.create(name = name, date_of_birth = date_of_birth, age = age, phone_number = phone_number, mail_id = mail_id, address = address, district = district, branch = branch, account_type = account_type)
        print('2nd')

        for choice_id in choice_ids:
            option = CheckboxOptions.objects.get(id=choice_id)
            user.choices.add(option)
        user.save()
        print("registered")
        # request.session["details_form_completed"] = True
        return redirect('/')
    # else:
    #     print("not registered")

    return render(request, 'detailsform.html', {'typ': typ, 'options': options})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branch = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'dropdown.html', {'branches': branch})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)