import argparse
from database import init_db, get_report
from data_export import export_json, export_xml

def main():
    init_db()
    parser = argparse.ArgumentParser(description="CLI для учета заказов")
    parser.add_argument('action', choices=['report', 'export', 'import'], help="Действие")
    parser.add_argument('--period', help="Период для отчета (day, week, month)")
    parser.add_argument('--file', help="Путь к файлу для экспорта/импорта")

    args = parser.parse_args()

    if args.action == 'report':
        print("=== Отчет по заказам ===")
        for status, count in get_report():
            print(f"Статус: {status} - Количество: {count}")
            
    elif args.action == 'export':
        if not args.file:
            print("Укажите файл: --file path.json")
            return
        if args.file.endswith('.json'):
            export_json(args.file)
            print("Успешно экспортировано в JSON")
        elif args.file.endswith('.xml'):
            export_xml(args.file)
            print("Успешно экспортировано в XML")
        else:
            print("Поддерживаются только .json и .xml")

if __name__ == '__main__':
    main()
