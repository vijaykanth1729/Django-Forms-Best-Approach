# Django-Forms-Best-Approach
This is all about django forms and also using django-axes..

It gives a better reprsentation of forms, and talks about the logging in users , loggingout users and registering the new
Users..

It also able to restrict the users to authenticate multiple times..(Locks the account if you type your password wrong for 5 times..)

It uses djang-axes to lockout the users back as follows..

If account is locked you can reset using this command: python manage.py axes_reset_username [username..]

It also uses a custom session middleware which make sures that at any point of time only one browser can access the site..(Automatically logs out if we try to login from multiple devices/browsers)

It handles session-time-out mechanism, so after 5 minutes of time your session will be automatically destroyed and you need to login again..(Implemented for Security reasons.)

Finally this web site also disallows the right click functionality (Similar like bank applications.. you can not right click on this site..)


