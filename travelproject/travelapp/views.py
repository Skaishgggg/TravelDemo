
from django.shortcuts import render
from . models import place
from . models import Team
# Create your views here.
def demo(request):
  obj=place.objects.all()
  res=Team.objects.all()
  return render(request,"index.html",{'result':obj,'resu':res})

