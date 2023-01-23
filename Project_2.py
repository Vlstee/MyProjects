def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increase_person_age(person_one)
print(new_person['age'])
print(person_one['age'])
