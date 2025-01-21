from django.shortcuts import render, redirect
from.models import Recipient, Blood, Hospital
from ACCOUNT.models import Users
from.forms import RecipientForm, BloodForm, HospitalForm
from django.contrib import messages
from django.db.models import Sum

from django.contrib.auth.decorators import login_required

# Create your views here.

def dashboard(request,pk=0):
    users=Users.objects.all()
  

    reciever=Recipient.objects.all().count()
    reciever_view=Recipient.objects.all()
    allblood=Blood.objects.all().order_by('-exp_date')
    total_quantity = Blood.objects.aggregate(Sum('quantity'))['quantity__sum']
    form_b = BloodForm(request.POST, request.FILES)
    HospitalForm = BloodForm(request.POST, request.FILES)
    forms_rp=RecipientForm(request.POST)
    if request.method == "POST":
        forms_rp=RecipientForm(request.POST)
        form_b = BloodForm(request.POST, request.FILES)
        if  form_b.is_valid():
            instance=form_b.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.success(request, "Blood added successfully!")
            return redirect('dashboard')
        elif forms_rp.is_valid():
            forms_rp.save()
            messages.success(request, "Blood added successfully!")
            return redirect('dashboard')
        
        elif HospitalForm.is_valid():
            HospitalForm.save()
            messages.success(request, "Blood added successfully!")
            return redirect('dashboard')
        
        else:
            messages.error(request, 'There was an error adding the blood.')
            return redirect('dashboard')
    context={
        'reciever_view':reciever_view,
        'form_r':forms_rp,
        'user':users,
        'receiver':reciever,
        'blood':allblood,
        'form_b':form_b,
        "HospitalForm":HospitalForm,
        'totalblood':total_quantity,
    }
    return render(request, 'blood/dashboard.html', context )


def donoraddblood(request):
    pass
    # # Initialize both forms
    # form_donor = DonorForm()
    # form_b = BloodForm()

    # if request.method == "POST":
    #     form_b = BloodForm(request.POST, request.FILES)
    #     form_donor = DonorForm(request.POST, request.FILES)
    #     if form_donor.is_valid() and form_b.is_valid():
    #         instance = form_b.save(commit=False)
    #         instance2=form_donor.save(commit=False)
    #         instance2.donor_name=request.user
    #         instance.blood_type = form_donor.cleaned_data['blood_type']
    #         instance.quantity = form_donor.cleaned_data['quantity']
    #         instance.image = form_donor.cleaned_data['image']

    #         instance.save()
    #         instance2.save()

    #         messages.success(request, "Blood added successfully!")
    #         return redirect('dashboard')

    #     else:
    #         messages.error(request, 'There was an error adding the blood.')
    #         return redirect('donoraddblood')

    # context = {
    #     'form': form_donor,
    #     'form_b': form_b,
    # }
    # return render(request, 'blood/donoraddblood.html', context)




# def recipient(request):
#     forms=RecipientForm()
    
#     if request.method =="POST":
#         forms=RecipientForm(request.POST, request.FILES)
#         if forms.is_valid():
#             instance=forms.save(commit=False)
#             instance.recipient_name =request.user
#             instance.save()
#             messages.info(request, 'Success full recipeting')
#             return redirect('dashboard')
#         else:
#             messages.warning(request, 'error in post data in recipete')
#             return redirect('dashboard')
        
#     context={
#         'form':forms
#     }
#     return render(request, 'blood/recipient.html', context)


@login_required(login_url='login')
def bloodupdate(request, pk):
    blood_id=Blood.objects.get(pk=pk)
    forms=BloodForm(instance=blood_id)
    
    if request.method == "POST":
        form=BloodForm(request.POST, instance=blood_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfull blood updated')
            return redirect('dashboard')
        messages.error(request, 'Error in blood updating')
        return redirect('dashboard')
    context={
        'form':forms
    }
    return render(request, 'blood/bloodupdate.html', context)


def deleteblood(request, pk):
    blood_id=Blood.objects.get(pk=pk)
    blood_id.delete()
    messages.info(request, 'successfull blood deleted')
    return redirect('dashboard')


# ########### HERE FULL MANAGE USER####

@login_required(login_url='login')
def userdeact_act(request, pk):
    user_id=Users.objects.get(pk=pk)
    if user_id.is_active:
        user_id=False
        user_id.save()
    else:
        user_id =True
        user_id.save()

def orderstatus(request, pk):
    order_id=Recipient.objects.get(pk=pk)
    if order_id.is_complete:
        order_id.is_complete=False
        order_id.save()
        messages.warning(request,"successfull order not approved")
        return redirect('dashboard')
    else:
        order_id.is_complete=True
        order_id.save()
        messages.info(request,"successfull order approved")
        return redirect('dashboard')
    
    
    # here full manage users
@login_required(login_url='login')  
def myuser(request):
    alluser=Users.objects.all()
    usercount=Users.objects.all().count
    
    context={
        "alluser":alluser,
        "usercount":usercount,
    }
    
    return render(request, 'user/manageuser.html', context)


@login_required(login_url='login')
def managemyuser(request, pk):
    user_id=Users.objects.get(pk=pk)
    if user_id.is_active:
        user_id.is_active=False
        user_id.save()
        messages.warning(request, 'successfull user deactivate')
        return redirect('alluser')
    else:
        user_id.is_active=True
        user_id.save()
        messages.success(request, 'successfull user activate')
        return redirect('alluser')
    
    
    


# for user

def userindex(request):
    bloods=Blood.objects.all()
   
    forms_p=RecipientForm()
    allblood=Blood.objects.all().order_by('-exp_date')
    rcp=Recipient.objects.all()
    
    if request.method == "POST":
        forms_rp=RecipientForm(request.POST)
        form_b = BloodForm(request.POST, request.FILES)
        if form_b.is_valid():
            form_b.save

            messages.success(request, "Blood added successfully!")
            return redirect('userpage')
        elif forms_rp.is_valid():
            instance=forms_rp.save(commit=False)
            instance.recipient_name=request.user
            forms_rp.save()
            messages.success(request, "Blood added successfully!")
            return redirect('userpage')
    
        elif forms_p.is_valid():
            instance=forms_p.save(commit=False)
            instance.recipient_name =request.user
            instance.save()
            messages.info(request, 'Success full recipeting')
            return redirect('userpage')
        else:
            messages.warning(request, 'error in post data in recipete')
            return redirect('userpage')
    context={
        'form':forms_p,
        'blood':bloods,
        "rcp":rcp,
    }
    return render(request, 'user/index.html', context)





# def recipient_form(request):
#     forms=RecipientForm()
    
#     if request.method =="POST":
#         forms=RecipientForm(request.POST, request.FILES)
#         if forms.is_valid():
#             instance=forms.save(commit=False)
#             instance.recipient_name =request.user
#             instance.save()
#             messages.info(request, 'Success full recipeting')
#             return redirect('userpage')
#         else:
#             messages.warning(request, 'error in post data in recipete')
#             return redirect('userpage')
        
#     context={
#         'form':forms
#     }
#     return render(request, 'user/userindex.html', context)

def searchblood(request):

    if request.method == "GET":
        myqquery=request.GET.get('query')
        
        if myqquery:
            serchresult=Blood.objects.filter(blood_type__icontains=myqquery)
            context={
                'blood':serchresult,
            }
            return render(request, 'user/search.html', context)
        
        else:
            serchresult=Blood.objects.filter(blood_type__icontains=myqquery)
            context={
                'blood':serchresult,
            }
            return render(request, 'user/search.html', context)