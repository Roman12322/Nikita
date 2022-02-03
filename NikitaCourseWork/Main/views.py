from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from .models import User, Messaging
from .forms import FormForFile
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.files import File
import os
from math import sqrt, ceil, pow

def Registr(request):
    return render(request, 'registr.html')

def General(request):
    return render(request, 'GeneralForm.html')

def Results(request):
    return render(request, 'results.html')

def ShowRes(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                data = Messaging.objects.filter(Username_Id=checkUserLogin.id)
                return render(request, "results.html", {"data": data})
            else:
                messages.error(request, "Неправильный логин или пароль")
                return HttpResponseRedirect("http://127.0.0.1:8000/results")
        except User.DoesNotExist:
            messages.error(request, "Неправильный логин или пароль")
            return HttpResponseRedirect("http://127.0.0.1:8000/results")
    return HttpResponseRedirect("http://127.0.0.1:8000/results")

def GetPrimeNumbers(request):
    form = FormForFile(request.POST, request.FILES or None)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        buffer = request.POST.get('getPrimes')
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                numbers = int(buffer)
                result = Primes(numbers)
                data = {
                    'username': username,
                    'password': password,
                    'amount': buffer,
                    'value': result
                }
                try:
                    ChosenFile = request.FILES['chosenFile']
                    chosenFile = ChosenFile.name
                    path = os.path.abspath(chosenFile)
                    chsFile = open(path, 'a')
                    myfile = File(chsFile)
                    myfile.write(f"\nYour  list of first {buffer} prime numbers: " + str(result))
                    myfile.closed
                    tmp = Messaging.objects.create(First_Prime_Numbers=buffer, List=result,
                                                   Username_Id=checkUserLogin.id)
                    messages.error(request, 'Данные успешно сохранены!')
                    return render(request, "GeneralForm.html", data)
                except MultiValueDictKeyError:
                    data = {
                        'username': username,
                        'password': password,
                        'amount': buffer,
                    }
                    messages.error(request, 'Вы не выбрали файл')
                    return render(request, "GeneralForm.html", data)
        except User.DoesNotExist:
            messages.error(request, "Неправильный логин или пароль")
            return HttpResponseRedirect("http://127.0.0.1:8000/GeneralForm")

def SignUp(request):
    try:
        if request.method == "POST":
            user = User()
            checkLogin = request.POST.get("username")
            checkPass = request.POST.get("pass")
            if len(checkLogin) > 4 or len(checkPass) > 4:
                user.Login = request.POST.get("username")
                user.Password = request.POST.get("pass")
                user.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/GeneralForm")
            else:
                messages.error(request, 'Логин и пароль должны быть больше 4 символов')
                return redirect('http://127.0.0.1:8000/')
    except IntegrityError:
        messages.error(request, 'Пользователь с таким логином уже есть')
        return redirect('http://127.0.0.1:8000/')

class SieveOfAtkin:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.sieve = [False] * (self.limit + 1)

    def flip(self, prime):
        try:
            self.sieve[prime] = True if self.sieve[prime] == False else False
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime] == True: self.sieve[prime] = False
        except KeyError:
            pass

    def isPrime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False

    def getPrimes(self):
        testingLimit = int(ceil(sqrt(self.limit)))

        for i in range(testingLimit):
            for j in range(testingLimit):
                # n = 4*i^2 + j^2
                n = 4 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.flip(n)

                # n = 3*i^2 + j^2
                n = 3 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and n % 12 == 7:
                    self.flip(n)

                # n = 3*i^2 - j^2
                n = 3 * int(pow(i, 2)) - int(pow(j, 2))
                if n <= self.limit and i > j and n % 12 == 11:
                    self.flip(n)

        for i in range(5, testingLimit):
            if self.isPrime(i):
                k = int(pow(i, 2))
                for j in range(k, self.limit, k):
                    self.invalidate(j)

        self.primes = [2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x >= 5]
        return self.primes

def Primes(value):
    sieve = SieveOfAtkin(400)
    buffer = sieve.getPrimes()
    res = []
    for i in range(value):
        res.append(buffer[i])
    return res