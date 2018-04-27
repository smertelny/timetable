import requests

def user_is_teacher(backend, user, uid, social, *args, **kwargs):
    if backend.name == 'google-oauth2':
        response = requests.get(
            "https://www.googleapis.com/admin/directory/v1/users/{}".format(uid),
            params={'access_token': social.extra_data['access_token']}
        )
        if response.json().get('orgUnitPath', None) == '/Вчителі':
            user.is_teacher = True
        else:
            user.is_student = True
        user.save()
