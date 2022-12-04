# PrettyTable：コンソール上に表組み表示するためのモジュール
# ※列単位でデータを作成する。
# -*- coding: utf-8 -*-
from prettytable import PrettyTable


def main():
    table = PrettyTable()

    table.add_column('Serial Number', 
        ['P1214',  'E9545',  'N9545'])
    table.add_column('Product Name' , 
        ['Pencil', 'Eraser', 'Notebook'])
    table.add_column('Lot',           
        ['100',    '150',    '200'])

    table.sortby      = 'Lot'
    table.reversesort = Trueprint(table)


if __name__ == '__main__':
    main()








# PrettyTable：コンソール上に表組み表示するためのモジュール
# コンソール上に表組み表示するためのモジュール
# ※行単位でデータを作成する。
# -*- coding: utf-8 -*-
from prettytable import PrettyTable

def main():

    table = PrettyTable(
        ['Serial Number', 'Product Name', 'Lot'])

    table.add_row(['P1214', 'Pencil',   '100'])
    table.add_row(['E9545', 'Eraser',   '150'])
    table.add_row(['N7811', 'Notebook', '200'])

    table.align['Serial Number'] = 'l'
    table.padding_width = 2

    print(table)


if __name__ == '__main__':
    main()






# PrettyTable：コンソール上に表組み表示するためのモジュール
# ※CSVファイルからデータを作成する。
# -*- coding: utf-8 -*-
import prettytable

def main():

    with open('data.csv', 'r') as file:
        table = prettytable.from_csv(file)

        print(table)

    return

if __name__ == '__main__':

    main()






# PrettyTable：コンソール上に表組み表示するためのモジュール
# ※HTMLファイルからデータを作成する。
# -*- coding: utf-8 -*-
from prettytable import from_html_one


def main():

    with open("data.html", "r") as file:
        html = file.read()

    table = from_html_one(html)
    print(table)

    return

if __name__ == '__main__':
    main()






# PrettyTable：コンソール上に表組み表示するためのモジュール
# ※SQLiteからデータを作成する。

# -*- coding: utf-8 -*-
import sqlite3 as lite
from prettytable import from_db_cursor


if __name__ == '__main__':
    con = lite.connect('data.db')
    
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM product')
        table = from_db_cursor(cur) 
    
    print(table)