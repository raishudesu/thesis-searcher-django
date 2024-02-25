# Thesis Searcher Project

This is a Django project for Application Development course.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python and pip installed on your local machine.

```
# Check Python version
python --version

# Check pip version
pip --version
```

### Installing

1. Clone the repository to your local machine:

```
git clone https://github.com/raishudesu/thesis-searcher-django
```

2. Navigate to the project directory:

```
cd thesis-searcher-django
```

3. Install project dependencies:

```
pip install -r requirements.txt
```

### Configuration

1. Rename `.env.example` to `.env` and update the configuration variables as needed.

### Running the Development Server

To run the development server, execute the following command:

```
python manage.py runserver
```

By default, the server will be available at `http://127.0.0.1:8000/`.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [SQLite](https://www.sqlite.org/) - The self-contained, serverless, zero-configuration, transactional SQL database engine.
- [Other dependencies...](https://pypi.org/)

### Loading database data

To load existing database data, execute the following command:

```
py manage.py loaddata db.xml
```

Make sure that the encoding is UTF-8.
