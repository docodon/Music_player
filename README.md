# Music_player
Requirements : 
	
	1. Django - 1.7

	2. Bootstrap loaded into your static files , Although I have added the files .
       Internet connection is required for now so as to load a jquery file .
       	
	3. Install django-autocomplete in order to get the autocomplete pluggin .

		links:  
			http://django-autocomplete-light.readthedocs.io/en/master/install.html     (installation)
			http://django-autocomplete-light.readthedocs.io/en/master/tutorial.html    (tutorial with a fine example)

	4. Install django-tweaks which are useful in rendering of django-forms in templates
		links :
			https://pypi.python.org/pypi/django-widget-tweaks


	Structure of project :

		1) Project has got one app .i.e. - musicplayer

		2) structure of musicplayer 

			urls :

					'/tracks/' - list of tracks 
					
					'/tracks/id/' - specific track
					
					'/genres' -list of genres
					
					'/genres/id/' - specific genre
					
					'/add_track/'  - form to add a track


			views : 

					tracks  (gives the home page)

					track_detail (gives the detail of specific track and functionality to edit track)

					add_track (add a new track)

					edit_track (edits the track )

					genres   (gives list of genres)			

					genre_detail (list of track of a genre)

					class Autocomplete :   (provides queryset to autocomplete autocomplete_track_functionality )

					search_redirect_track : (redirects track selected in autocomplete to track_detail/track/ )

					class Autocomplete2 : (provides queryset to autocomplete autocomplete_genre_functionality )

					search_redirect_genre : (redirects track selected in autocomplete to genre_detail/genre/ )
 		
 		    
 		    Models : 

 					Tracks [Track_name,Track_title,Rating,Genre_id,Track]

 					Genre_id [Genre_id , Genre_name]

 					Id_genre [Genre_id , Genre_name]  { empty one , never used }


 			 Forms : 

 					Add_genre_form   [ adding new genre ]

 					Add_track_form(Modelform)    [ adding new track ]

 					Search_track_form    [searching track ]

 					Search_genre_form [ searching genre ]

 		

 		3) templates :
 			
 			home.html    - base of templates .

 			tracks.html - renders list of tracks

 			add_track.html   - renders form for adding track 

 			track_detail.html - renders track details and Edit track form

			genres.html     - renders list of genres and Add_genre_form 
			
			genre_detail.html - renders list of songs of particular genre and form to rename genre				
