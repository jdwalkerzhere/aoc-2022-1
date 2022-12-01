def populate_calorie_data(cal_list):
    elf_calories = {}
    ind = 0
    elf = 1
    
    while ind < len(cal_list):
        if cal_list[ind] == '': 
            elf += 1
            ind += 1
            continue
        if elf not in elf_calories:
            elf_calories[elf] = int(cal_list[ind])
            ind += 1
        else:
            elf_calories[elf] += int(cal_list[ind])
            ind += 1
    return elf_calories

def solutions(dictionary):
    sorted_elves = sorted(dictionary.values())
    return sorted_elves[-1], sum(sorted_elves[-3::])