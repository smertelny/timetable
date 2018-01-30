import requests

from django.contrib.auth.models import User



def user_is_teacher(backend, user, uid, social, *args, **kwargs):
    if backend.name == 'google-oauth2':
        response = requests.get(
            "https://www.googleapis.com/admin/directory/v1/users/{}".format(uid),
            params={'access_token': social.extra_data['access_token']}
        )
        if response.json().get('orgUnitPath', None) == '/Вчителі':
            teacher = user.selectedteacher
            teacher.is_teacher = True
            teacher.save()
