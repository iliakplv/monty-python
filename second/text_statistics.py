import operator

in_file_name = '../data/text.txt'


symbols_dict = {}
symbols_total = 0
symbols_types = 0


for line in open(in_file_name):
    for symbol in line:
        symbols_total += 1
        if symbol in symbols_dict:
            symbols_dict[symbol] += 1
        else:
            symbols_dict[symbol] = 1


sorted_count = reversed(sorted(symbols_dict.items(), key=operator.itemgetter(1)))


for symbol_count in sorted_count:
    symbols_types += 1
    symbol = symbol_count[0]
    if symbol == '\n':
        s = 'ret'
    elif symbol == '\t':
        s = 'tab'
    elif symbol == ' ':
        s = "' '"
    else:
        s = ' ' + symbol + ' '
    print("{number}.\t{symbol} : {count}".format(number=symbols_types, symbol=s, count=symbol_count[1]))


print("\nTotal symbols: {total}".format(total=symbols_total))
