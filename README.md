
# Weblog

this is a project for exercise Django framework

#TODO

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


#TODO-API
- [x] Add api app and make serializer and a ListCreateAPIView   
- [x] Add view for single article in api app
- [x] Add User model to api
- [x] Add permissions for api/user/* views in views.py

#TODO-ACCOUNT
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