from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import HttpResponse
import json


## MODEL VIEW
from .forms import userinput_form
from .models import User_input
from django.core import serializers
import reco_app.recommendation as rec

"""
def userinput_create_view(request):
	form = userinput_form(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "userinput_page.html", context)
	#the slash is the folder, after the file we want to render
"""

def userinput_create_view(request):
	my_form = userinput_form()
	if request.method == "POST":
		my_form = userinput_form(request.POST or None) #create instance of a class
		if my_form.is_valid():
			User_input.objects.create(**my_form.cleaned_data) #if the form is valid create an instance in the database\
			request.session['locations'] = request.POST.getlist('locations')
			request.session['services'] = request.POST.getlist('services')
			request.session['organizations'] = request.POST.getlist('organizations')
			request.session['roles'] = request.POST.getlist('roles')
			return redirect('/recommendation')
		#now the data is good
		else: 
			print(my_form.errors) #print the error (missing field etc. -- this is detected automatically by django)

	context = {
		"form": my_form
	}
	return render(request, "userinput_page.html", context)

def rec_create_view(request):
	data = request.session.get('locations', None) + request.session.get('services', None) + request.session.get('organizations', None) + request.session.get('roles', None)
	print(data)
	names, names_adress, descriptions, links = rec.predict(data)
	return render(request, 'reco_output_page.html', {'names': names, 'names_adress': names_adress, 'descriptions': descriptions, 'links': links, 'range_top': [0, 1, 2], 'range_bottom': [3, 4]})

