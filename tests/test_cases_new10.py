from api import PetFriends
from settings import valid_password, valid_email

pf = PetFriends()


def test_case1_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Case #1'''

    status, result = pf.get_api_key(password, email)
    assert status == 200
    assert 'key' in result


def test_case2_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Case #2'''

    status, result = pf.get_api_key(password, email)
    assert status == 403
    assert 'key' not in result


def test_case3_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Case #3'''

    status, result = pf.get_api_key(email, password)
    assert status == 200
    if 'key' not in result:
        assert 'No key'
    else:
        raise Exception('Key get')


def test_case4_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Case #4'''

    try:
        status, result = pf.get_api_key(password, email)
        assert status == 200
    except:
        raise AssertionError('Incorrect status')


def test_case5_get_all_pets(filter=''):
    '''Case #5'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pets(auth_key, filter)
    try:
        assert auth_key
    except:
        raise TypeError('Incorrect key')


def test_case6_post_new_pet(name='Yoda', animal_type='Jedi', age=977, pet_photo='images/images.jpeg'):
    '''Case #6'''

    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_new_simple_pets(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
        assert len(result) != 0
    except TypeError as e:
        print(f"Caught a TypeError: {e}")


def test_case7_post_new_photo(pet_photo='images/public.jpeg'):
    '''Case #7'''

    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        pf.post_new_simple_pets(auth_key, name='Obi-Wan', animal_type='Jedi', age=40)
        _, my_pets = pf.get_pets(auth_key, 'my_pets')

        pet_id = my_pets['pets'][0]['id']
        status, result = pf.post_new_photo(auth_key, pet_id)
        assert status == 200
        assert result['pet_photo']
    except TypeError as e:
        print(f"Caught a TypeError: {e}")


def test_case8_delete_pet():
    '''Case #8'''
    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_pets(auth_key, filter='')

        if len(my_pets['pets']) == 0:
            pf.post_new_pets(auth_key, name='Yoda', animal_type='Jedi', age=977, pet_photo='images/images.jpeg')
            _, my_pets = pf.get_pets(auth_key, 'my_pets')

        pet_id = my_pets['pets'][0]['id']
        status, result = pf.delete_pets(auth_key)
        assert status == 200
        assert pet_id not in my_pets.values()
    except TypeError as e:
        print(f"Caught a TypeError: {e}")


def test_case9_delete_pet():
    '''Case #9'''
    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_pets(auth_key, filter='')

        if len(my_pets['pets']) == 0:
            pf.post_new_pets(auth_key, name='Yoda', animal_type='Jedi', age=977, pet_photo='images/images.jpeg')
            _, my_pets = pf.get_pets(auth_key, 'my_pets')

        pet_id = my_pets['pets'][0]['id']
        status, result = pf.delete_pets()
        assert status == 200
        assert pet_id not in my_pets.values()
    except TypeError as e:
        print(f"Caught a TypeError: {e}")


def test_case10_delete_pet():
    '''Case #10'''
    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_pets(auth_key, filter='')

        if len(my_pets['pets']) == 0:
            pf.post_new_pets(auth_key, name='Yoda', animal_type='Jedi', age=977, pet_photo='images/images.jpeg')
            _, my_pets = pf.get_pets(auth_key)

        pet_id = my_pets['pets'][0]['id']
        status, result = pf.delete_pets(auth_key, pet_id)
        assert status == 200
        assert pet_id not in my_pets.values()
    except TypeError as e:
        print(f"Caught a TypeError: {e}")