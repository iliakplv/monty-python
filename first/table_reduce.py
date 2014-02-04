in_file_name = '../data/table_data.txt'
out_file_name = 'table_result.txt'
round_to_digits = 1

sums_dict = {}
total_sum_initial = 0


# counting
for line in open(in_file_name):
    if not len(line.strip()) == 0:

        entry = line.split()
        if not len(entry) == 2:
            raise Exception('unknown data in line')

        number = int(entry[0])
        amount = float(entry[1])

        if number in sums_dict.keys():
            sums_dict[number] += amount
        else:
            sums_dict[number] = amount

        total_sum_initial += amount


# erase out file
temp = open(out_file_name, 'w')
temp.write('')
temp.close()


# output
total_sum_counted = 0
out_file = open(out_file_name, 'a')

for number in sorted(sums_dict.keys()):
    amount = round(sums_dict[number], round_to_digits)
    entry = "{n}\t{a}\n".format(n=number, a=amount)

    print(entry, end='')
    out_file.write(entry)

    total_sum_counted += amount

out_file.close()
print('\nDone!',
      "Initial sum is {tsi}".format(tsi=total_sum_initial),
      "Counted sum is {tsc}".format(tsc=total_sum_counted), sep='\n')
