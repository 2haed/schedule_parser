from qparser import ScheduleParser
import sys


def main():
    group_name = input('Print group name to see schedule\nor -1 to exit: ')
    if group_name == str(-1):
        print('Bye!')
        sys.exit(0)
    else:
        with ScheduleParser(driver=None, schedule=None) as parser:
            parser.get_schedule(group_name.lower())
            df = parser.build_dataframe()
            print(df)


if __name__ == '__main__':
    main()
