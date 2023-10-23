from person import Person

my_friends = [
    Person('Aleksey Smirnov', 32, 'M'),
    Person('Anna Volkova', 25, 'F'),
    Person('Ivan Petrov', 22, 'M'),
    Person('Alisa Kovalchuk', 28, 'F'),
]

def get_oldest_person(friends):
    oldest_friend = max(friends, key=lambda friend: friend.age)
    return oldest_friend

for friend in my_friends:
    friend.print_person_info()

