from django.shortcuts import render,render_to_response


def index(requests):
    return render_to_response('index.html')

def about(requests):
    return render_to_response('about.html')

def acm(requests):
    return render_to_response('acm.html')

def contact(requests):
    return render_to_response('contact.html')

def hulianwang(requests):
    return render_to_response('hulianwang.html')

def lanqiao(requests):
    return render_to_response('lanqiao.html')

def portfolio(requests):
    return render_to_response('portfolio.html')

def portfolio1(requests):
    return render_to_response('portfolio1.html')

def portfolio2(requests):
    return render_to_response('portfolio2.html')

def portfolio3(requests):
    return render_to_response('portfolio3.html')  

def pricing(requests):
    return render_to_response('pricing.html')    

def services(requests):
    return render_to_response('services.html')        




