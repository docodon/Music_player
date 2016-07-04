from django.shortcuts import render
from musicplayer.models import Tracks,Genre_id
from musicplayer.forms import Add_genre_form,Add_track_form,Search_track_form,Search_genre_form
from django.http import Http404
from dal import autocomplete
from django.shortcuts import redirect

# Create your views here.

def tracks(request):                                              		#home_page : gives list of tracks 
	track_list=Tracks.objects.all()
	return render(request,'tracks.html',{'track_list':track_list})


def track_detail(request,track_id):                                   #gives detail of a single track
	try :
		track=Tracks.objects.get(id=track_id)
		rating=track.Rating*20                                            #rating calculated
		try :
			genre_name=Genre_id.objects.get(Genre_id=track.Genre_id)
		except Genre_id.DoesNotExist :
			raise Http404("Something went wrong please contact geedymusic team !")
	except Tracks.DoesNotExist :
		track_list=Tracks.objects.all()
		return render(request,'tracks.html',{'track_list':track_list , 'message' : ' Track not found !! '})
	return render(request,'track_detail.html',{'track':track,'genre':genre_name , 'rating':rating \
		,'form': Add_track_form(instance=Tracks.objects.get(id=track_id))})

def add_track(request):
	if request.method=='POST':
		form=Add_track_form(request.POST,request.FILES)
		if form.is_valid():
			new_track=form.save(commit=False)
			new_track.Genre_id=form.cleaned_data['Genre'].Genre_id
			new_track.save()
			return render(request,'add_track.html',{'form':Add_track_form,'message':'  Track added ! '})
		else :
			return render(request,'add_track.html',{'form':Add_track_form,'message':form.errors})
	else:
		return render(request,'add_track.html',{'form':Add_track_form})


def edit_track(request,track_id):
	if request.method=='POST':
		instance=Tracks.objects.get(id=track_id)
		form = Add_track_form(request.POST, request.FILES,instance=instance)
		if form.is_valid():
			edited_track=form.save(commit=False)
			edited_track.Genre_id=form.cleaned_data['Genre'].Genre_id
			edited_track.save()
			return track_detail(request,track_id=track_id)
		else :
			track=Tracks.objects.get(id=track_id)
			rating=track.Rating*20                                            #rating calculated
			genre_name=Genre_id.objects.get(Genre_id=track.Genre_id)
			return render(request,'track_detail.html',{'track':track,'genre':genre_name ,'message':form.errors,\
			 'rating':rating ,'form': Add_track_form(instance=Tracks.objects.get(id=track_id))})
	else :
		return track_detail(request,track_id=track_id)

def genres(request):                                               #gives list of genres
	genres=Genre_id.objects.all()
	return render(request,'genres.html',{'genres':genres,'form':Add_genre_form})

 
def genre_detail(request,genre_id):											#all the tracks of genre
	if request.method=='POST':
		form=Add_genre_form(request.POST)
		if form.is_valid():
			genre_object = Genre_id.objects.get(Genre_id=genre_id)
			genre_object.Genre_name=form.cleaned_data['Genre_name']
			genre_object.save() 
			genre_name=Genre_id.objects.get(Genre_id=genre_id)                         
			track_list=Tracks.objects.filter(Genre_id=genre_id)     
			return render(request,'genre_detail.html',{'genre_id':genre_id,'genre_name':genre_name,'track_list':track_list,'form':Add_genre_form,'message':'Genre renamed !'})
		else :
			return render(request,'genre_detail.html',{'genre_id':genre_id,'genre_name':genre_name,\
				'track_list':track_list,'form':Add_genre_form,'message':form.errors})
	else:
		track_list=Tracks.objects.filter(Genre_id=genre_id)     
		genre_name=Genre_id.objects.get(Genre_id=genre_id)                         
		return render(request,'genre_detail.html',{'genre_id':genre_id,'genre_name':genre_name,'track_list':track_list,'form':Add_genre_form})


def add_genre(request):
	genres=Genre_id.objects.all()
	sz=len(genres)			
	if request.method == 'POST' :
		form=Add_genre_form(request.POST)
		if form.is_valid():
			addgen=form.cleaned_data['Genre_name']
			if Genre_id.objects.filter(Genre_name=addgen).count()>0 :
				return render(request,'genres.html',{'form':Add_genre_form,'message':'Genre exists !','genres':genres})
			else :
				Genre_id_obj=Genre_id(Genre_name=addgen,Genre_id=sz)
				Genre_id_obj.save()
				genres=Genre_id.objects.all()
				return render(request,'genres.html',{'genres':genres,'form':Add_genre_form,'message':' Genre added successfully !',})	
		else :
			return render(request,'genres.html',{'genres':genres,'form':Add_genre_form,'message':form.errors})
	else :
		return render(request,'genres.html',{'genres':genres,'form':Add_genre_form})
	

# search using autocomplete implemented for track and genre separaetly


class Autocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Tracks.objects.all()
		if self.q :
			qs=qs.filter(Track_title__istartswith=self.q)
		return qs

	
def search_redirect_track(request):
	if request.method == 'POST' :
		form=Search_track_form(request.POST)
		if form.is_valid():
			x=form.cleaned_data['Search_track']
			if type(x).__name__== 'Tracks' :
				return redirect(track_detail,track_id=x.id)	
	raise Http404("Something went wrong !")

	
class Autocomplete2(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Genre_id.objects.all()
		if self.q :
			qs=qs.filter(Genre_name__istartswith=self.q)
		return qs

		
def search_genre(request):
	return render(request,"search_genre.html",{'form':Search_genre_form})

	
def search_redirect_genre(request):
	if request.method == 'POST' :
		form=Search_genre_form(request.POST)
		if form.is_valid():
			x=form.cleaned_data['Search_genre']
			if type(x).__name__== 'Genre_id' :
				return redirect(genre_detail,genre_id=x.Genre_id)	
	raise Http404("Something went wrong !")

