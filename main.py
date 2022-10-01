from qparser import ScheduleParser
import sys


def main():
    group_name = input('Print group name to see schedule\nor -1 to exit: ')
    if group_name == str(-1):
        print('Bye!')
        sys.exit(0)
    else:
        print(ScheduleParser(group_name=group_name).build_dataframe())


if __name__ == '__main__':
    main()