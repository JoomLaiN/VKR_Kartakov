from django.shortcuts import render

def my_test(request):
    return render(request, 'test/my_test.html')
