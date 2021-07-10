

# Instructions For Use


## Prerequisites

First of all, you need python interpret.
you can download it ftom Microsoft Store at [https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab](https://example.com)

After that, you will need pip in Windows Commend Prompt for installing requirements.

1. run the following command to download the get-pip.py file:
    ```sh
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```
2. Then, to install PIP type in the following:
    ```sh
    python get-pip.py
    ```

## Virtualenv

#### Install Virtualenv
```sh
pip install virtualenv
```

#### Create your enviremant
```sh
cd PATH_TO_PROJECT 

python3 -m venv YOUR_ENVIREMENT_NAME ( example : python3 -m venv env )
```

#### Enviremant activation
```sh
\YOUR_ENVIREMENT_NAME\Scripts\activate ( example : env\Scripts\activate)
```

## Requirements

#### Install requirements


>pip install django

>pip install djangorestframework

>Pip install Python-dotenv

>pip install pillow

>pip install django-cors-headers

>pip install django-allauth



##

#### Migrate your project
```sh
python manage.py migrate
```

#### make Migrations project
```sh
python manage.py makemigrations
```

#### Create your super user
```sh
python manage.py createsuperuser
```

#### Start project
```sh
python manage.py runserver
```

Login with your created super http://localhost:8000/admin/

Check http://localhost:8000/admin/ for Database Management
