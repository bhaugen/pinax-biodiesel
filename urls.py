from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template

from wiki import models as wiki_models

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    
    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', "signup_codes.views.signup", name="acct_signup"),
    
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^profiles/', include('basic_profiles.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^announcements/', include('announcements.urls')),
    (r'^tags/', include('tag_app.urls')),
    (r'^tagging_utils/', include('tagging_utils.urls')),
    (r'^attachments/', include('attachments.urls')),
    (r'^bookmarks/', include('bookmarks.urls')),
    (r'^tasks/', include('tasks.urls')),
    (r'^topics/', include('topics.urls')),
    (r'^comments/', include('threadedcomments.urls')),
    (r'^wiki/', include('wiki.urls')),
    (r'^photos/', include('photos.urls')),
    (r'^flag/', include('flag.urls')),

    # emails
    url(r'^sendemail/$', 'emails.views.send_email', name="send_email"),
    url(r'^email_sent/$', direct_to_template, 
        {"template": "emails/email_sent.html"}, name="email_sent"),
    
    (r'^admin/(.*)', admin.site.root),
)

from photos.models import Image

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/', include('staticfiles.urls')),
    )
