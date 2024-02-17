from django.shortcuts import render,redirect


def calculator(request):
    try:
        c=''
        data={}
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            elif opr=='/':
                c=n1/n2
            data={
                'n1':n1,
                'n2':n2,
                'output':c
            }
    except:
       c='Invalid opr.....'
    return render(request,"calculator.html",data)