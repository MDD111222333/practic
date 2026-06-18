import json
import xml.etree.ElementTree as ET
from database import get_connection, logger

def export_json(filepath):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()

    data = []
    for o in orders:
        data.append({"id": o[0], "customer_id": o[1], "date": o[2], "status": o[3], "total": o[4]})
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info(f"Экспорт в {filepath} завершен")

def export_xml(filepath):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()

    root = ET.Element("Orders")
    for o in orders:
        order_xml = ET.SubElement(root, "Order")
        ET.SubElement(order_xml, "Id").text = str(o[0])
        ET.SubElement(order_xml, "CustomerId").text = str(o[1])
        ET.SubElement(order_xml, "Date").text = o[2]
        ET.SubElement(order_xml, "Status").text = o[3]
        ET.SubElement(order_xml, "Total").text = str(o[4])

    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    logger.info(f"Экспорт в XML {filepath} завершен")
