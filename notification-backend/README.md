# Notification Feature Project

This project implements a notification feature that allows users to subscribe to daily reports. Users can select a date range for which they want to receive these reports in both PDF and HTML formats. The system sends the reports to the user's email daily, only for the selected date range.

## Project Structure

```
notification-backend
├── manage.py
├── requirements.txt
├── notification_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── reports
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tasks.py
│   ├── utils.py
│   ├── migrations
│   │   └── __init__.py
│   └── templates
│       └── reports
│           └── daily_report.html
├── static
│   └── reports
└── README.md
```

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Libraries for PDF generation (e.g., ReportLab, WeasyPrint)
- Libraries for graph generation (e.g., Matplotlib)

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd notification-backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

## API Endpoints

- **POST /subscribe/**: Subscribe to daily reports.
- **POST /unsubscribe/**: Cancel the subscription.
- **GET /subscriptions/**: List current subscriptions.
- **GET /reports/history/**: Return sent reports.

## Scheduled Tasks

The project includes a scheduled task that runs daily to check for active subscriptions and generates reports accordingly.

## Report Generation

- **PDF Reports**: Generated using libraries like ReportLab or WeasyPrint, including graphs created with Matplotlib.
- **HTML Reports**: Rendered using Django's templating engine.

## Email Sending

The project simulates email sending using Django's console backend for development purposes. 

## Usage

After setting up the project, users can interact with the API to manage their subscriptions and receive daily reports based on their preferences.

## License

This project is licensed under the MIT License.