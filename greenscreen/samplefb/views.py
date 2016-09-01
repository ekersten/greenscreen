import urllib
import json

from django.shortcuts import render

from social.apps.django_app.default.models import UserSocialAuth


# Create your views here.
def index(request):
    context = {
        'authenticated': False
    }

    user = request.user

    if user.is_authenticated:
        if user.social_auth.filter(provider='facebook'):
            facebook_data = user.social_auth.get(provider='facebook')
            url = "https://graph.facebook.com/v2.7/{0}/photos?fields=images&limit=100&access_token={1}".format(facebook_data.uid, facebook_data.extra_data['access_token'])
            json_obj = urllib.request.urlopen(url)
            facebook_photos = json.loads(json_obj.readall().decode('utf-8'))
            context['facebook_photos'] = facebook_photos
            print('user has facebook')
        else:
            print('user doesn\'t have facebook')

    return render(request, 'samplefb/index.html', context)
