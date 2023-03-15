import requests
import json
import pytest


def test_is_correct_name():
    url = "https://reqres.in/api/users/2"
    expected_name = 'Janet'
    expected_last_name = 'Weaver'
    response = requests.get(url)
    response_body = response.text
    body_json_obj = json.loads(response_body)
    user_data = dict.get(body_json_obj, 'data')
    first_name = 'first_name'
    last_name = 'last_name'
    assert first_name in user_data, f'Ключ {first_name} не существует'
    assert last_name in user_data, f'Ключ {last_name} не существует'
    actual_name = user_data[first_name]
    actual_last_name = user_data[last_name]
    assert actual_name == expected_name, f'Имя {user_data[first_name]} не соответствует ожидаемому'
    assert actual_last_name == expected_last_name, f'Фамилия {user_data[last_name]} не соответствует ожидаемой'


def test_is_unique_email():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    response_body = response.text
    body_json_obj = json.loads(response_body)
    user_data_dictionary = dict.get(body_json_obj, 'data')
    #data = {"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"michael.lawson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}
    email = 'email'
    duplicates = []
    for user in user_data_dictionary:
        count_of_emails = 0
        current_email = user[email]
        for checkUser in user_data_dictionary:
            if current_email == checkUser[email]:
                count_of_emails += 1
        if count_of_emails > 1:
            duplicates.append(current_email)
    assert len(duplicates) == 0, "Email не уникальны"


if __name__ == '__main__':
    pytest.main()
