# Product Reviews API

This project is a backend implementation of a Product Review system using Django Rest Framework. The project is organized into two main apps: `reviews` and `user_auth`. The `reviews` app handles product reviews and product-related functionalities, while the `user_auth` app manages user authentication and authorization.

## Features

### User Authentication (user_auth app)

- User Registration: Users can create new accounts by providing basic information.
- User Login: Registered users can log in with their credentials.
- Token Authentication: The project uses JSON Web Tokens (JWT) for secure user authentication.
- Token Refresh: Users can refresh their tokens to maintain their sessions.
- Change Password: Users can update their passwords securely.
- Update Profile: Users can modify their profile information.
- Logout: Provides the ability for users to log out.

### Product Reviews (reviews app)

- List Products: Retrieve a list of products with their details including dynamic nested related data expansion and filtering by using Rest_flex_fields.
- Product Details: Get detailed information about a specific product.
- Custom Admin Interface: The project includes a customized admin interface for efficient management of data.


## Rest_flex_fields

- This project uses the rest_flex_fields package to provide dynamic field expansion and filtering for product reviews. This allows users to control which fields are included in the response to a request, and to expand nested resources.

```bash
For example, a user could request a list of product reviews with the following parameters:

?fields=id,name,category.name
This would return a list of product reviews, with each review containing the id, name, and category.name fields.

A user could also expand a nested resource, such as the comments field, by using the following parameter:

?expand=comments
This would return a list of product reviews, with each review containing the id, name, and comments fields. The comments field would contain a list of all of the comments for the product review.

Example Usage

To retrieve a list of product reviews with dynamic field expansion and filtering, you can send a GET request to the following endpoint:

http://localhost:8000/product/?fields=id,name,category.name&expand=comments
To retrieve a specific product review with dynamic field expansion and filtering, you can send a GET request to the following endpoint, replacing <id> with the ID of the review:

http://localhost:8000/product/<id>/fields=id,name,category.name&expand=comments

```
## Installation

1. Clone the repository:

```bash
git clone https://github.com/m-rakesh-kr/product-reviews-api.git
cd product-reviews-api
```

2. Install project dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. Create a superuser account for admin access:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the admin interface at `http://localhost:8000/admin/` and use the superuser account to log in.

## API Endpoints

### User Authentication Endpoints

- Register: `POST /auth/register/`
- Login: `POST /auth/login/`
- Token Refresh: `POST /auth/login/refresh/`
- Change Password: `PUT /auth/change-password/{user_id}/`
- Update Profile: `PUT /auth/update_profile/{user_id}/`
- Logout: `POST /auth/logout/`
- Logout All Devices: `POST /auth/logout_all/`

### Product Reviews Endpoints

- List Products: `GET /product/`
- Product Details: `GET /product/{product_id}/`

## Customization

You can customize and expand the project according to your specific needs. For instance, you can add additional user profile fields, more product features, or enhance the user interface.

## Dependencies

- Django
- Django Rest Framework
- Simple JWT
- Rest_flex_fields

## Rakesh Kumar

- [Linkedin](https://www.linkedin.com/in/m-rakesh-kr/)

Feel free to contribute or report issues in the project's [GitHub repository](https://github.com/yourusername/product-reviews-api).

Enjoy using the Product Reviews API!
