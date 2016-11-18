#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.views.generic import FormView, ListView
from .models import Comments,Enroll
from .form import CommentsForm,EnrollForm
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseServerError

from django.http import StreamingHttpResponse    #下载文件

import time

def index(requests):
    return render_to_response('index.html')

def about(requests):

    return render_to_response('about.html')

def acm(requests):
    return render_to_response('acm.html')

class ContactView(ListView):

    template_name = 'contact.html'

    model = Comments
    context_object_name = "demo"

    def get_queryset(self):
        demo = Comments.objects.all()
        return demo

    def get_context_data(self, **kwargs):
        kwargs['form'] = CommentsForm()
        return super(ContactView, self).get_context_data(**kwargs)
        
class EnrollView(ListView):

    template_name = 'enroll.html'

    model = Enroll
    context_object_name = "demo"

    def get_queryset(self):
        demo = Enroll.objects.all()
        return demo

    def get_context_data(self, **kwargs):
        kwargs['form'] = EnrollForm()
        return super(EnrollView, self).get_context_data(**kwargs)        

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
    
def enroll(requests):
    return render_to_response('enroll.html')

class CommentPostView(FormView):
    form_class = CommentsForm
    template_name = 'contact.html'

    def form_valid(self, form):
        """
            提交的数据合法
        """

        comment = form.save(commit=False)
        comment.save()
        
        #print "success comment"
        return HttpResponse("ok")

    def form_invalid(self, form):
        """
            提交的数据不合法
        """
        
        #print "fail comment"
        return HttpResponseServerError()

class EnrollPostView(FormView):

    form_class = EnrollForm
    template_name = 'enroll.html'

    def form_valid(self, form):
        """
            提交的数据合法
        """

        enroll = form.save(commit=False)
        enroll.save()
        
        #print "success comment"
        return HttpResponse("ok")

    def form_invalid(self, form):
        """
            提交的数据不合法
        """
        
        #print "fail comment"
        return HttpResponseServerError()        

def question(request):  
    # do something...  
 
    def file_iterator(file_name, chunk_size=512):  
        with open(file_name) as f:  
            while True:  
                c = f.read(chunk_size)  
                if c:  
                    yield c  
                else:  
                    break  
  
    the_file_name = "./sta-2016-test.pdf" 
    if time.time() > 1479902400 :
        response = StreamingHttpResponse(file_iterator(the_file_name))  
        response['Content-Type'] = 'application/octet-stream'  
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)  
  
        return response  
    
    else:
        return HttpResponse("<h1>未到开放时间，请于 2016-11-23 日 20 点后下载试题！</h1>")




