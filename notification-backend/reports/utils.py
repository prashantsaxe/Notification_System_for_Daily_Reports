def generate_mock_data(date):
    # This function generates mock data for the daily report.
    return {
        "date": date,
        "summary": f"Daily Summary for {date}",
        "data": {
            "sales": 100 + (date.day * 10),  # Mock sales data
            "users": 50 + (date.day * 2),    # Mock user data
        }
    }

def create_pdf_report(data):
    # This function generates a PDF report from the provided data.
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from io import BytesIO
    import matplotlib.pyplot as plt

    # Create a buffer to hold the PDF data
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 750, data['summary'])

    # Generate a bar chart
    plt.bar(['Sales', 'Users'], [data['data']['sales'], data['data']['users']])
    plt.title(data['summary'])
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.savefig('chart.png')  # Save the chart as an image
    plt.close()

    # Draw the chart on the PDF
    pdf.drawImage('chart.png', 100, 500, width=400, height=200)
    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer.getvalue()

def create_html_report(data):
    # This function generates an HTML report from the provided data.
    html_content = f"""
    <html>
    <head><title>{data['summary']}</title></head>
    <body>
        <h1>{data['summary']}</h1>
        <p>Sales: {data['data']['sales']}</p>
        <p>Users: {data['data']['users']}</p>
    </body>
    </html>
    """
    return html_content