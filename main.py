from utils import populate_calorie_data
from utils import solutions

if __name__ == '__main__':
    with open('data.txt', 'r') as data:
        data = [i.strip('\n') for i in data.readlines()]

    elf_cals = populate_calorie_data(data)
    part1, part2 = solutions(elf_cals)
    print(part1)
    print(part2)