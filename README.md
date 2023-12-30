
# Symmetrical Cart

Simple e-commerce application build with Django, PostgreSQL and Docker.


## Installation

1. Clone repository
```bash
  git clone https://github.com/ddvuser/symmetrical-cart.git
  cd symmetrical-cart
```
2. Configure environment:
You have to create `.env.dev` and `.env.db.dev`:
```bash
cd symmetrical-cart
touch .env.dev .env.db.dev
```

Contents of `.env.dev` file:
```env
DEBUG=1
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DATABASE=postgres
CSRF_TRUSTED_ORIGINS=localhost:1337
```

Contents of `.env.db.dev` file:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
3. Running app:
```bash
cd ..
docker-compose -f docker-compose.dev.yml up -d --build
```
    
## Features

- Delivery app
- Shop app
## Running Tests

To run tests on whole project, run the following command

```bash
  python manage.py test
```

To test separate app:

```bash
  python manage.py test app_name
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are always welcome!


