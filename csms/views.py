from django.shortcuts import render, redirect, get_object_or_404
from .models import Inmate
from .forms import InmateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def inmate_list(request):
    inmates = Inmate.objects.all()
    total_inmates = inmates.count()  # Calculate the total number of inmates
    return render(request, 'inmate_list.html', {'inmates': inmates, 'total_inmates': total_inmates})

@login_required
def inmate_detail(request, inmate_id):
    inmate = get_object_or_404(Inmate, pk=inmate_id)
    return render(request, 'inmate_detail.html', {'inmate': inmate})

@login_required
def inmate_new(request):
    if request.POST:
        form = InmateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmate was successfully created.')
            return redirect('home')
        else:
            messages.error(request, 'Form is not valid')
            # Print form errors to the console for debugging
            print(form.errors)
    else:
        form = InmateForm()
    return render(request, 'inmate_new.html', {'form': form})

@login_required
def inmate_edit(request, inmate_id):
    inmate = get_object_or_404(Inmate, pk=inmate_id)
    
    if request.method == 'POST':
        form = InmateForm(request.POST, instance=inmate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmate was successfully updated.', 'alert-success')
            return redirect('home')  # Redirect to the appropriate URL
        else:
            messages.error(request, 'Form is not valid', 'alert-danger')
    
    else:
        form = InmateForm(instance=inmate)
    
    return render(request, 'inmate_edit.html', {'form': form})

@login_required
def inmate_destroy(request, inmate_id):
    inmate = get_object_or_404(Inmate, pk=inmate_id)
    inmate.delete()
    return redirect('home', messages.success(request, 'Inmate was successfully deleted.', 'alert-success'))



# @login_required
# def officer_list(request):
#     officers = CorrectionalOfficer.objects.all()
#     return render(request, 'officer_list.html', {'officers': officers})

# @login_required
# def officer_detail(request, officer_id):
#     officer = get_object_or_404(CorrectionalOfficer, pk=officer_id)
#     return render(request, 'officer_detail.html', {'officer': officer})

# @login_required
# def officer_new(request):
#     if request.POST:
#         form = CorrectionalOfficerForm(request.POST)
#         if form.is_valid():
#             if form.save():
#                 return redirect('officer_list', messages.success(request, 'Correctional officer was successfully created.', 'alert-success'))
#             else:
#                 return redirect('officer_list', messages.error(request, 'Data is not saved', 'alert-danger'))
#         else:
#             return redirect('officer_list', messages.error(request, 'Form is not valid', 'alert-danger'))
#     else:
#         form = CorrectionalOfficerForm()
#         return render(request, 'officer_new.html', {'form': form})

# @login_required
# def officer_edit(request, officer_id):
#     officer = get_object_or_404(CorrectionalOfficer, pk=officer_id)
#     if request.POST:
#         form = CorrectionalOfficerForm(request.POST, instance=officer)
#         if form.is_valid():
#             if form.save():
#                 return redirect('officer_list', messages.success(request, 'Correctional officer was successfully updated.', 'alert-success'))
#             else:
#                 return redirect('officer_list', messages.error(request, 'Data is not saved', 'alert-danger'))
#         else:
#             return redirect('officer_list', messages.error(request, 'Form is not valid', 'alert-danger'))
#     else:
#         form = CorrectionalOfficerForm(instance=officer)
#         return render(request, 'officer_edit.html', {'form': form})

# @login_required
# def officer_destroy(request, officer_id):
#     officer = get_object_or_404(CorrectionalOfficer, pk=officer_id)
#     officer.delete()
#     return redirect('officer_list', messages.success(request, 'Correctional officer was successfully deleted.', 'alert-success'))