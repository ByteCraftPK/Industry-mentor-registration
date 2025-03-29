from django.shortcuts import render, redirect
from .forms import IndustryMentorForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = IndustryMentorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = IndustryMentorForm()
    return render(request, 'industry_mentor/register.html', {'form': form})

