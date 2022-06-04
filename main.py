#!/usr/bin/env python3
import os
import shutil
'''Creates a folder structure for photos based on the year and month they were taken'''


def main():
    years_dir = set()
    file_types = ['.jpg', '.png', '.mov', 'jpeg']

    for i in os.listdir('.'):
        if i[-3:] == '.py':
            continue
        elif i[-4:] in file_types:
            year = i[:4]
            month = i[5:7]
            year_month = year + '/' + month
            if year not in years_dir:
                years_dir.add(year)
                os.mkdir(year)
            if not os.path.isdir(year_month):
                os.mkdir(year_month)
            src = './' + i
            final_path = year_month + '/' + i
            shutil.move(src, final_path)


if __name__ == '__main__':
    main()
