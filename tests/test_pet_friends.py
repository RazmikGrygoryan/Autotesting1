from api import PetFriends
from settings import valid_password, valid_email


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) != 0

def test_post_new_pet(name = 'Yoda', animal_type = 'Jedi', age = 977, pet_photo = 'images/images.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) != 0

def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pets(auth_key, filter='')

    if len(my_pets['pets']) == 0:
        pf.post_new_pets(auth_key, name = 'Yoda', animal_type = 'Jedi', age = 977, pet_photo = 'images/images.jpeg')
        _, my_pets = pf.get_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.delete_pets(auth_key, pet_id)
    assert status == 200
    assert pet_id not in my_pets.values()

def test_put_info_to_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.put_new_pets(auth_key, pet_id, name='Anakin', animal_type='Sith', age=25)

        assert status == 200
        assert result['name'] == 'Anakin'
    else:
        raise Exception('There is no my pet')

def test_post_new_simple_pet(name = 'Obi-wan', animal_type = 'Jedi', age = 40):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_simple_pets(auth_key, name, animal_type, age)
    assert status == 200
    assert len(result) != 0

def test_post_new_photo(pet_photo = 'images/public.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pf.post_new_simple_pets(auth_key, name='Obi-Wan', animal_type='Jedi', age=40)
    _, my_pets = pf.get_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.post_new_photo(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo']
