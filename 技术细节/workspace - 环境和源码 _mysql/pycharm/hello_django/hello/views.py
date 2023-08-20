from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader, Template
from hello.forms import PublisherForm
from hello.models import Publisher, Author, AuthorDetail,Book,Device,TermInfo,School,Team,suggest
import datetime
# Create your views here.
user_list = []
def begin(request):
	return render(request, 'begin.html')
def MyPublisher(request):
	Contracts = School.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Publisher.html', {'user_list':user_list})

def MyAuthor(request):
	Contracts = Device.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Author.html', {'user_list':user_list})

def MyAuthorDetail(request):
	Contracts = suggest.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request,'AuthorDetail.html',{'user_list':user_list})

def MyBook(request):
	Contracts = Team.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Book.html', {'user_list': user_list})

def MyTermInfo(request):
	Contracts = Device.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Terminfo.html', {'user_list': user_list})

def MyDevice(request):
	global user_list
	Contracts = Device.objects.all()
	paginator = Paginator(Contracts, 20)  # Show 25 User per page

	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Device.html', {'user_list': user_list})

def query_Publisher(request):
	if request.method == "POST":
		title = request.POST['name']
		print(title)
		# print(city)
		print("query_Publisher")
		user_list = School.objects.filter(university=title)
		return render(request, 'Publisher.html', {'user_list': user_list})
	else:
		user_list = School.objects.all()
		return render(request, 'Publisher.html', {'user_list': user_list})

def query_Author(request):
	if request.method == "POST":
		people = request.POST['people']
		print(people)
		# print(city)
		print("query_Author")
		user_list = Device.objects.filter( people = people)
		return render(request, 'Author.html', {'user_list': user_list})
	else:
		user_list = Device.objects.all()
		return render(request, 'Author.html', {'user_list': user_list})

def query_AuthorDetail(request):
	if request.method == "POST":
		u = request.POST.get("title", None)
		s = request.POST.get("people", None)
		# ---------表中插入数据方式一
		# info={"username":u,"sex":e,"email":e}
		# models.UserInfor.objects.create(**info)

		# ---------表中插入数据方式二
		suggest.objects.create(
			score=u,
			advice=s,
		)

		info_list = suggest.objects.all()

		return render(request, "AuthorDetail.html", {"user_list": info_list})

	return render(request, "AuthorDetail.html")

def query_Book(request):
	if request.method == "POST":
		title = request.POST['title']
		price = request.POST.get('price')
		print(title)
		print(price)
		print("query_Book")
		user_list = Book.objects.filter( title = title,price = price)
		return render(request, 'Book.html', {'user_list': user_list})
	else:
		user_list = Book.objects.all()
		return render(request, 'Book.html', {'user_list': user_list})

def query_TermInfo(request):
	if request.method == "POST":
		title = request.POST['title']
		print(title)
		# print(city)
		print("query_TermInfo")
		#user_list = Device.objects.raw("select *from hello_device where title like '%'+%s+'%'",[title])
		user_list = Device.objects.filter(title = title)
		return render(request, 'Terminfo.html', {'user_list': user_list})
	else:
		user_list = Device.objects.all()
		return render(request, 'Terminfo.html', {'user_list': user_list})

def query_Device(request):
	global user_list
	if request.method == "POST":
		title = request.POST['title']
		people = request.POST.get('people')
		print(title)
		print(people)
		print("query_Device")
		user_list = Device.objects.all()
		if people !=  "":
			user_list = user_list.filter(people = people)
		elif title !=  "":
			user_list = user_list.filter(title = title)
	else:
		user_list = user_list

	Contracts = user_list
	paginator = Paginator(Contracts, 20)  # Show 25 User per page
	page = request.GET.get('page')
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list = paginator.page(paginator.num_pages)

	return render(request, 'Device.html', {'user_list': user_list})

def query_Device1(request):
	if request.method == "POST":
		university = request.POST['university']
		sort = request.POST['sort']
		topic = request.POST['topic']
		print(sort)
		print(university)
		print(topic)
		global user_list
		if university == "全部显示":
			user_list = Device.objects.all()
		else:
		    user_list = Device.objects.filter(university = university)
		if topic == "全部显示":
			user_list = user_list
		else:
			user_list = Device.objects.filter(theme=topic)
		if sort == "通知时间升序":
			user_list = user_list.order_by("release_time")
		elif sort == "通知时间降序":
		    user_list = user_list.order_by("-release_time")
		elif sort == "报告时间升序":
			user_list = user_list.order_by("time")
		elif sort == "报告时间降序":
			user_list = user_list.order_by("-time")
	Contracts = user_list
	paginator = Paginator(Contracts, 20)  # Show 25 User per page
	page = request.GET.get('page')
	try:
		user_list1 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list1 = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list1 = paginator.page(paginator.num_pages)

	return render(request, 'Device.html', {'user_list': user_list1})

def query_time(request):
	global user_list
	if request.method == "POST":
		begin_time = request.POST['datepicker']
		end_time = request.POST.get('datepicker1')
		print(begin_time)
		print(end_time)
		print("query_Device")
		user_list = Device.objects.all()
		user_list = Device.objects.raw("select *from hello_device where time < %s and time > %s", [end_time,begin_time])

	Contracts = user_list
	paginator = Paginator(Contracts, 20)  # Show 25 User per page
	page = request.GET.get('page')
	try:
		user_list1 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		user_list1 = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		user_list1 = paginator.page(paginator.num_pages)

	return render(request, 'Device.html', {'user_list': user_list1})

def add_publisher(request):
	if request.method == "POST":
		publisher_form = PublisherForm(request.POST)
		if publisher_form.is_valid():
			publisher_form.save()

			contact_list = User.objects.all()
			paginator = Paginator(contact_list, 10)  # Show 25 User per page
			page = request.GET.get('page')
			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				contacts = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				contacts = paginator.page(paginator.num_pages)
			return render(request, 'AuthorDetail.html', {'user_list': contacts})
	else:
		publisher_form = PublisherForm()
	return render(request, 'add_publisher.html', locals())

