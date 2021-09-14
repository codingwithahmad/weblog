
# Weblog

this is a project for exercise Django framework

# TODO

- [x] Make article model
- [x] Fix url patterns for artcles app
- [x] Set a template for home page
- [x] Set a base template model for templates
- [x] Change panel admin language to persian
- [x] Make single article page
- [x] Show all articles in databse in articles.html page
- [x] Make Category model
- [x] Add Category to admin pandel and Articles model
- [x] Show categoreis in frontend
- [x] link categories names in to articles that category contain
- [x] Make a page for showing each category articles
- [x] Make config.py for security items and add it to .gitignore
- [x] Make parent field for Category model
- [x] Change date from Gregorian date to Jalali
- [x] Make category_loop.file file and include that in navbar_category.html file with loop
- [x] Change fonts
- [x] Change the template
- [x] Make pagination and button for chanage the pages
- [x] Make a dropdown navigation bar for category with submenu
- [x] Add category hashtag for articles
- [x] Add action to Articles and Category modles
- [x] Add thumbnail to admin panel for Articles model
- [x] Put all static files in project into a dir name static
- [x] Change panel admin fonts to a farsi fonts like Sahel
- [x] Change Admin panel header from admin.py in articles app
- [x] Make list.html to handel all articles list how have a same structure
- [ ] Make view for user articles
- [ ] Change functional view to generic class


# TODO-API
- [x] Add api app and make serializer and a ListCreateAPIView   
- [x] Add view for single article in api app
- [x] Add User model to api
- [x] Add permissions for api/user/* views in views.py

# TODO-ACCOUNT
- [x] Create Account app
- [x] Create a urls.py file for account app
- [x] Set a route to account.urls in myweblog urls.py
- [x] Set a route for /account/login in account urls.py
- [x] Make registration folder and login.html in this folder for handel template of /account/login route
- [x] Make home page for logged in users
- [x] Set LOGIN_REDIRECT_URL and LOGIN_URL in settings.py 
- [x] Make a template name base.html for /account page and sidebar.html is include that
- [x] Edit template and fix sylesheet link
- [x] Clean the adminlte template at /account and fix some url for tags
- [x] Add articles list with a tabel in /account
- [x] Fix articles list table for showing our articles
- [x] Change ArticlesList view in account app to showing all articles just for superusers
- [x] Create ArticlesCreate view in account app and articles_create_update.html for its template
- [x] Beautify ArticlesCreate view by install and use django-crispy-forms
- [x] Add User model at account/models and customiz that for useing User model in project
- [x] Delete database and migrate again for useing custom User model
- [x] Add custom User model fields how placed in account app models to admin panel for update and create user
- [x] Add mixins.py file in account app and write two mixin for fields how user access them and an if condition in article_create_update.html for not showing that fields
- [x] Add ArticlesUpdate view and AuthorAccessMixin in account app and change home.html title for just showing draft articles link for author user
- [x] Added a ArticlesDelete view in account app and a mixin name SuperUserMixin and create articles_confirm_delete.html template for ArticlesDelete view 
- [x] Added LOGOUT_REDIRECT_URL to settings.py and a ul for showing logout icon than add a condition for just showing a message when the table is empty
# section 55
- [x] Add a templatetags of type inclusion in base_tags.py at articles app
- [x] Add a link.html file in registration/partials
- [x] Add a sample a link from sidebar to link.html and fix that with link inclusion template tag how add in base_tag.py
- [x] Add an if condition for showing a delete button when user is a superuser at the update article page
# section 56 
- [x] Add a ArticlePreview in views.py at articles app
- [x] Add AuthorAccessMixin in ArticlePreview
- [x] Add an a tag in if condition at home.html for showing preview
# section 57
- [x] Add two more status in Article model 
- [x] Change AuthorAccessMixin and replace " == 'd' " with "in ['b', 'd']"
- [x] Change conditions in home.html 
# section 58 
- [x] Add is_special field to Article model
- [x] Add is_special field to admin.py list_display in articles app and FieldMixin for author and superuser
- [x] Add some condition in articles_detail.html for showing description
- [x] Add a new column for is_special in home.html table
# section 59
- [x] Add Profile view in views.py at account app
- [x] Add new url for Profile view in urls.py at account app
- [x] Add profile.html template for Profile view 
# section 60
- [x] Add forms.py at account app
- [x] Create new form in the nam of ProfileForm in forms.py
- [x] Set ProfileForms for form_class attr in Profile view in views.py
# section 61
- [x] Add get_form_kwargs def to Profile view for send user to ProfileForm
- [x] Add an if not user.is_superuesr to ProfileForm init 
# section 62
- [x] Add Login view who inherit from LoginView in account app
- [x] Add an if condition for redirect normal user to profile after login
- [x] Add an if condition at sidebar.html for showing articles section just for author and superusers
# section 63
- [x] Add AuthorsAccessMixin in Mixins.py
- [x] Replace LoginRequireMixin with AuthorsAccessMixin
# section 64
- [x] Add an if condition next to title at list.html and article_create.html for showing special badge for is_special articles
- [x] Add 2 line of article.description over the p tag for normal user in article_detail.html 
- [x] add alert and alert-warning classes for p tag and alert-link class for a tag in it
# section 65
- [x] Add an if condtion in AuthorsAceessMixin for anonymous user bug
- [x] Add an else section for if condition refer to the superuser for status and author section and add a html part to author user can select between draft and send to admin for publish
- [x] Chanage FieldMixin and FieldValid mixin 
# section 66
- [x] Add two new url for password_chanage and password_chanage_done
- [x] Add PasswordChanage view who inherit of django.contrib.auth.views.PasswordChangeView and than change success_url
- [x] Add two html template for password_chanage and password_change_done
- [x] Add and div with col-12 class for change_password link in profile.html
# section 67
- [x] copy login url in urls.py at account app
- [x] delete all urlpatterns who from auth app in django 
- [x] import Login view form account.views to urls.py at myweblog app
- [x] delete PasswordChange view from account.views
- [x] Change 'account:login' in settengs.py to 'login' for LOGOUT_REDIRECT_URL and LOGOUT_URL
- [X] Change all url to password_chanage or login or other authenticatian link who have account: and delete account reference
- [x] Add EMAIL_BACKEND in settings.py
- [x] Add an a tag with link to 'password_reset' at profile.html 
- [x] Add an email field to User model in accoun.models this need to add a unique=True for email in 0001_initial.py in migrations dir at account app and then makemigrations and migrate
- [x] Chanage template for chanage password operation and add password_reset.html, password_reset_done.html, password_reset_confirm.html and password_reset_complete.html
- [x] in password rest confirm add an if condition for validlink 
# section 68
- [x] Install python-decouple library
- [x] Add .env file and write email security information
- [x] from decouple import config and config all security information need in settings.py
- [x] fix some issue from account url in Profiel view and AuthorsAccessMixin
# section 69
- [x] Make tokens.py - account app
- [x] TokenGenerator in tokens.py - account app
- [x] SignupForm in forms.py - account app 
- [x] Register view in views.py - account app 
- [x] Create account_active.html for sending email 
- [x] activate view in views.py - account app
- [x] set url for /activate/<uidb64>/<token> in myweblog/urls.py
- [x] set url for /register in myweblog/urls.py
- [x] Create create_account.html 
- [x] Add signup link to login view
# section 70 
- [x] Install package django-gravatar2
- [x] Add 'django_gravatar' to Installed_app in settings.py
- [x] Load gravatar in sidebar.html and {% gravatar_url user.email 150 %} in src of profile photo
# section 71
- [x] Install django-comments-dab 
- [x] Add "comment" to Installed_app
- [x] Add "/comment" url to urls in myweblog
- [x] import GenericRelation and Comment in models.py - articels app
- [x] Add comments field to Article app
- [x] Add {% load comment_tags %}, {% render_comments article request %} and {% include_bootstarp %} to articles_detail.html
# section 72
- [x] copy comments app from venv/lib/python/site-packages/ in my django-review3/myweblog
- [x] uninstll django-comments-dab by pip
- [x] edit templates/comment/comments html file for make custom comment section
# section 73
- [x] Start sending email for people who send comment to articles in comment/views/comments.py/ CreateComment class and form valid def
# section 74 
- [x] Install and setup star ratings app https://pypi.org/project/django-star-ratings/
# section 75
- [x] Create IPAddress model in articles/models.py
- [x] Add hits manytomany fields based on IPAdress model to Articles model in articles/models.py
- [x] Create middleware.py in articles app
- [x] Create IPAddressMiddleware in middleware.py at aritcles app
- [x] Add IPAddressMiddleware to other middleware at settings.py
- [x] Change ArticlesDetail view in articles/views.py to set ip in hits for article if is not added 
- [x] Finaly Add div tag like <div><small>بازدید ها: {{ article.hits.count }}</small></div> to articles_detail.html and list.html to showing views
# section 76 
- [x] Add through="ArticleHit" for hits field in Articles model 
- [x] Create ArticleHit model in models.py at articles app
# section 77 
- [x] Change article list view to generic class
- [x] Import Count and Q from django.db.models in articels/views.py
- [x] Change ArticlesList model queryset to showing articles order by count of hits 
# section 78
- [x] Make popular_articels at templates/articels/partials
- [x] Create an inclusion_tag in base_tags.py for popular_articels
- [x] Send popular_articels to popular_articels.html by inclusion_tag 
- [x] Set {% popular_articels %} block at articles_list.html and articles_detail.html
# section 79
- [x] Rename popular_articles.html to sidebar.html and change this template to make reuseable for another inclusion_tag
- [x] Make another inclusio_tag with hot_articles name 
- [x] hot articles inclusion_tag send most commented articels in month to sidebar.html template
- [x] for first time in project user contenttype framework 
# section 80
- [x] Create SearchList view in aritcles/views.py
- [x] Create search_list.html at templates/articles
- [x] Add search section to navbar_category at templates/articles/partials
- [x] Add url for SearchList view in urls.py at articles app
# section 81
- [x] Add humanize app to settings.py
- [x] Set naturaltime templatetag to list.html and articles_detail.html
- [x] https://simpleisbetterthancomplex.com/tips/2016/05/09/django-tip-2-humanize.html