from django.shortcuts import render

# Create your views here

def post_list(request):
	return render(request, 'blogcontent/post_list.html')
