def first_task(postal1, postal2):
    first_postal = [int(postal1[:2]), int(postal1[3:])]
    second_postal = [int(postal2[:2]), int(postal2[3:])]

    while True:
        first_postal[1] += 1
        if first_postal[1] < 10:
            print(str(first_postal[0]) + '-00' + str(first_postal[1]))
        elif first_postal[1] < 100:
            print(str(first_postal[0]) + '-0' + str(first_postal[1]))
        else:
            print(str(first_postal[0]) + '-' + str(first_postal[1]))
        if first_postal[1] == 999:
            first_postal[0] += 1
            first_postal[1] = -1
        if first_postal[1] == second_postal[1] - 1:
            break


def second_task(array, n):
    output = []
    for number in range(1, n + 1):
        if number not in array:
            output.append(number)
    print(output)


def third_task(start, stop, step):
    array1 = [float(start)]
    buff = 0
    while array1[-1] != stop:
        array1.append(array1[buff] + step)
        buff += 1
    print(array1)


first_task("79-900", "80-155")
second_task([2, 3, 7, 4, 9], 10)
third_task(2, 5, 0.5)
