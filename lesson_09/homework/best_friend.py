from person import Person

my_best_friend = Person('Ivan Ivanov', 20, 'M')
my_best_friend.print_person_info()

birth_year = my_best_friend.get_birth_year()
print(f"Birth Year: {birth_year}")