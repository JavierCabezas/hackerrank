def person_lister(original_function):
    def sort_by_age(people_list):
        return map(original_function, sorted(people_list, key=lambda x: int(x[2])))
    return sort_by_age

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')