from django.shortcuts import render

def saludo(request):
   data = request.POST.get('name')
   print(data)
   return render(request,'index.html',{'data':data})

