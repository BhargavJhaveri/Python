import sys


def print_lol(the_list, indent=False, num=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, num + 1, fh)
        else:
            if indent:
                for number in range(num):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)
