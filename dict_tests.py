birthdays = {
    'Albert Einstein': '14/03/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
}


def get_person_birthday():
    person_name = input('>>> Who\'s birthday do you want to look up?\n ')
    if person_name in birthdays:
        print(f'>>> {person_name}\'s birthday is {birthdays[person_name]}.')
    else:
        print(f'>>> Sadly, we don\'t have {person_name}\'s birthday.')


def _welcome():
    print('\n>>> Welcome to the birthday dictionary. We know the birthdays of:')
    for key in birthdays.keys():
        print(key)


if __name__ == '__main__':
    _welcome()
    get_person_birthday()
