from django.conf.urls import patterns, url
from musicplayer import views
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
        url(r'^tracks/$', views.tracks, name='tracks'),
        url(r'^tracks/(?P<track_id>[0-9]+)/$',views.track_detail,name='track_details'),
       	url(r'^genres/$',views.genres,name='genres'),
       	url(r'^genres/(?P<genre_id>[0-9]+)/$',views.genre_detail,name='genre_details'),
        url(r'^add_genre/$',views.add_genre,name='add_genre'),
       	url(r'^add_track/$',views.add_track,name='add_track'),
        url(r'^edit_track/(?P<track_id>[0-9]+)/$',views.edit_track,name='edit_track'),
        url(r'^auto-complete/$',views.Autocomplete.as_view(),name='auto-complete'),
       	url(r'^search_redirect_track/$',views.search_redirect_track,name='search_redirect_track'),
        url(r'^auto-complete-genre/$',views.Autocomplete2.as_view(),name='auto-complete-genre'),
        url(r'^search_redirect_genre/$',views.search_redirect_genre,name='search_redirect_genre'),
       )
