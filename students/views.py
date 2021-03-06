from django.shortcuts import render
from django.http import HttpResponse

#Vievs for Students

def students_list(request):
	return render(request, 'students/students_list.html', {})

def students_add(request):
	return HttpResponse('<h1>Student add Form<h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete student %s</h1>' % sid)

#Vies for Groups
def groups_list(request):
	return render(request, 'students/groups_list.html', {})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)


