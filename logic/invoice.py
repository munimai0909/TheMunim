from reportlab.pdfgen import canvas
import os

def generate_invoice(data, output_path):
    """
    data: dict with keys - customer_name, items (list of tuples), total_amount, invoice_no
    output_path: full path where to save PDF
    """
    c = canvas.Canvas(output_path)
    c.setFont("Helvetica", 14)
    c.drawString(50, 800, f"Invoice No: {data.get('invoice_no', '0001')}")
    c.drawString(50, 780, f"Customer: {data.get('customer_name')}")
    y = 750
    c.setFont("Helvetica", 12)
    for item in data.get('items', []):
        c.drawString(60, y, f"{item[0]} - Qty: {item[1]} - Rate: ₹{item[2]}")
        y -= 20
    c.drawString(50, y - 20, f"Total: ₹{data.get('total_amount', 0)}")
    c.save()
