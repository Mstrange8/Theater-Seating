"""
    Name: Matthew Strange
    Date: 03/01/21
    Title: Movie Theater Seating Challenge
"""

dic = {'B': list(range(1, 21)), 'D': list(range(1, 21)), 'F': list(range(1, 21)),
       'H': list(range(1, 21)), 'J': list(range(1, 21))}

d = {0: 'D', 1: 'F', 2: 'H', 3: 'J', 4: 'B'}

rows_file = open('output_rows', 'w')


def seats_left(res):
    """
    For each row, checks if enough seats are available.
    Writes seat numbers to file.
    Removes seats from dictionary.
    Moves current row to the end of the dictionary.
    """
    for i in d.keys():
        if len(dic[d[i]]) >= res:
            print(res)
            print(dic[d[i]][:res])
            rows_file.write(('R{} ' + '{}\n').format(str(n + 1), ','.join([d[i] + str(a) for a in dic[d[i]][:res]])))
            dic[d[i]] = dic[d[i]][res + 3:]
            d[i] = d.pop(i)
            return
    rows_file.write('Number of seats requested are not available.\n')


def seats_right(res):
    """
    For each row, check if enough seats are available.
    Writes seat numbers to file.
    Removes seats from dictionary.
    Moves current row to the end of the dictionary.
    """
    for i in d.keys():
        if len(dic[d[i]]) >= res:
            rows_file.write(('R{} ' + '{}\n').format(str(n + 1), ','.join([d[i] + str(a) for a in dic[d[i]][-1 * res:]])))
            dic[d[i]] = dic[d[i]][:-1 * res - 3]
            d[i] = d.pop(i)
            return
    rows_file.write('Number of seats requested are not available.\n')


def main():
    """
    Loops through input file.
    Assigns seats to left side of theater.
    Starts filing in seats starting from the right side of theater.
    """
    with open('Input_Rows', 'r') as f:
        reservation_list = f.readlines()
        res_list = [int(res[5]) for res in reservation_list]

    global n
    n = 0
    for res in res_list:
        if n % 2 == 0:
            seats_left(res)
        else:
            seats_right(res)
        n += 1


if __name__ == "__main__":
    main()
