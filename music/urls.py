from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # music/
    url(r'^$', views.index, name='index'),

    # register/
    url(r'^register/$', views.register, name='register'),

    # login/
    url(r'^login/$', views.login_user, name='login'),

    url(r'^logout/$', views.logout_user, name='logout'),

    # music/<album-id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # favourite_song
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    # music/songs
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # /music/album/add_album
    url(r'album/add_album/$', views.create_album, name='add_album'),


    # /music/album/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.delete_album, name='delete_album'),

    # /music/album/favourite_album
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),

    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='add_song'),

    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
]

# urlpatterns = [
#     # music/
#     url(r'^$', views.index, name='index'),
#
#     # music/<album-id>/
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
#
#     # music/<album-id>/<song-id>/
#     url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
# ]