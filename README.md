
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
cd symmetrical_cart/symmetrical_cart/
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

### Shop app urls
- **Home Page**: `/` - `main_views.index`
- **Product Detail Page**: `/product/<slug:slug>/` - `main_views.product_detail`
- **Cart**: `/cart/` - `main_views.cart`
- **Add to Cart**: `/add-to-cart/<slug:product_slug>` - `main_views.add_to_cart`
- **Remove from Cart**: `/remove-from-cart/<int:orderproduct_id>` - `main_views.remove_from_cart`
- **Checkout**: `/checkout/` - `main_views.checkout`
- **Category Page**: `/category/` - `main_views.category`
- **Category Detail Page**: `/category/<slug:category_slug>` - `main_views.category_detail`
- **Rate Delivery**: `/rate-delivery/<int:order_id>` - `main_views.rate_delivery`

### Password-related URLs
- **Change Password**: `/password-change` - `user_change_password`
- **Password Reset**: `/password-reset/` - `PasswordResetView`
- **Password Reset Done**: `/password-reset/done/` - `PasswordResetDoneView`
- **Password Reset Confirm**: `/password-reset-confirm/<uidb64>/<token>/` - `PasswordResetConfirmView`
- **Password Reset Complete**: `/password-reset-complete/` - `PasswordResetCompleteView`

### Email-related URLs
- **Initiate Email Change**: `/init-email-change/` - `init_email_change`
- **Verify Email Change**: `/verify-email-change/` - `verify_email_change`
- **Submit New Email**: `/submit-new-email/` - `submit_new_email`

### User Profile and Authentication
- **User Profile**: `/profile/` - `user_profile`
- **Register**: `/register/` - `user_register`
- **Login**: `/login/` - `user_login`
- **Logout**: `/logout/` - `user_logout`

### Delivery App
- **Delivery Index**: `/` - `views.delivery_index`
- **Accept Order**: `/accept-order/<int:order_id>` - `views.accept_order`
- **Decline Order**: `/decline-order/<int:order_id>` - `views.decline_order`
- **Complete Order**: `/complete-order/<int:order_id>` - `views.complete_order`
- **My Orders**: `/my-orders/` - `views.my_orders`

### Running Tests

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


