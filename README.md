# Civil Engineer Labs

<img src="https://i.imgur.com/9nERKAE.png" width="500">

## Project Description

**What it does?** 💡 It's a Web Application for Testing Services at a Civil Engineering Laboratory. **Why did you build this project?** 💡 It will be used not only to put together the business's logistics but also to automate in real-time the logic behind some of the most used lab tests in the civil engineering career.

**What was my motivation?** 💡 This is built on top of my thesis project, so I'll implement some new UX/UI features and make an upgrade to the project architecture. I will create a package for extending and scaling the implemented tests, this will be updated and maintained on a different repo. **What did you learn?** 💡 The focus of this project is to create a Data-WareHouse to extract and create some nice Dashboards to give some insides about the characteristics of the tests and business financials.

## Table of Contents

<!--ts-->
* [Civil Engineer Labs](#civil-engineer-labs)
   * [Project Description](#project-description)
   * [Table of Contents](#table-of-contents)
   * [Parts of the Project](#parts-of-the-project)
      * [1. Price Quotations](#1-price-quotations)
      * [2. Testing Implementation](#2-testing-implementation)
      * [3. Monitoring Orders](#3-monitoring-orders)
      * [4. Global Monitoring Reports](#4-global-monitoring-reports)
   * [How to Install and Run the Project](#how-to-install-and-run-the-project)
      * [1. Localy](#1-localy)
      * [2. Deploy](#2-deploy)
   * [How to Contribute](#how-to-contribute)
   * [How to Use the Project](#how-to-use-the-project)
   * [Tests](#tests)
   * [Licence GNU GPLv3](#licence-gnu-gplv3)
      * [+ Info](#-info)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: jorgeav527, at: Wed 16 Nov 23:36:58 -05 2022 -->

<!--te-->

## Parts of the Project

### 1. Price Quotations
### 2. Testing Implementation
### 3. Monitoring Orders
### 4. Global Monitoring Reports

## How to Install and Run the Project

### 1. Localy

* Build and up the conteirner

    ```bash
    docker compose -f docker-compose-dev.yml build
    docker compose -f docker-compose-dev.yml up -d
    ```

* If you want to verify the content of the staticfiles
    
    ```bash
    mkdir data/web
    docker compose -f docker-compose-dev.yml run --rm app sh -c "python manage.py collectstatic --no-input"
    ```

* Make migrations or get inside the docker postgres 

    ```bash
    docker compose -f docker-compose-dev.yml run --rm app python manage.py makemigrations
    docker compose -f docker-compose-dev.yml run --rm app python manage.py migrate
    docker compose -f docker-compose-dev.yml exec db psql --username=devuser --dbname=devddb
    ```

* Create a superuser or enter to the shell
    ```bash
    docker compose -f docker-compose-dev.yml run --rm app python manage.py createsuperuser
    docker compose -f docker-compose-dev.yml run --rm app python manage.py shell
    ```

### 2. Deploy

## How to Contribute

## How to Use the Project

## Tests

## Licence GNU GPLv3

### +Info

- https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django
- https://forum.djangoproject.com/t/items-are-not-being-added-in-the-cart/10564/26
- https://stackoverflow.com/questions/1194737/how-to-update-manytomany-field-in-django
- https://pythonspeed.com/articles/alpine-docker-python/
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ ***
- https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
- https://computingforgeeks.com/dockerize-django-application-with-postgresql/
- https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
