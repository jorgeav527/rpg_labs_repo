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
         * [UX/UI design](#uxui-design)
         * [Adding test for the quotations](#adding-test-for-the-quotations)
         * [Company registrations](#company-registrations)
         * [Enployee and Project registrations](#enployee-and-project-registrations)
         * [Generate the requirements](#generate-the-requirements)
      * [2. Test Implementation](#2-test-implementation)
      * [3. Monitoring Orders](#3-monitoring-orders)
      * [4. Global Monitoring Reports](#4-global-monitoring-reports)
   * [How to Install and Run the Project](#how-to-install-and-run-the-project)
      * [1. Localy](#1-localy)
      * [2. Deploy](#2-deploy)
   * [How to Contribute](#how-to-contribute)
   * [How to Use the Project](#how-to-use-the-project)
   * [Tests](#tests)
   * [Licence GNU GPLv3](#licence-gnu-gplv3)
      * [+Info](#info)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: jorgeav527, at: Thu 17 Nov 17:14:23 -05 2022 -->

<!--te-->

## Parts of the Project

### 1. Price Quotations

#### **UX/UI design**

The design of this Web Application is made with [NiceAdmin v2.2.2](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/) for a beautiful, simple, and responsive UI. I'm using [HTMX](https://htmx.org/) and [django-htmx](https://github.com/adamchainz/django-htmx) because there is no need to add a full React or Vue for the UX frontend. The final product is what the company expected and more. 

#### **Adding test for the quotations**

First, I design a logic in Django's backend admin to introduce the cost of each test and implement a way to add to the price the related tests, like if a parent main test could have many children tests. For an easy and fast CSV data import, I use [django-import-export](https://django-import-export.readthedocs.io/en/latest/).

This is how to add child test:
    
<img src="https://i.imgur.com/Be5Po2O.png" width="400">

And this a parent test:

<img src="https://i.imgur.com/CtW3DiT.png" width="400">

And how to add child test to a parent test:

<img src="https://i.imgur.com/qtO8EyU.png" width="800">

Notice that when you save the parent test, the total price will be automatically calculated:

<img src="https://i.imgur.com/txqqpUW.png" width="800">

#### **Company registrations**

This is where an admin user will enroll companies by filling out the following form: 

<img src="https://i.imgur.com/dVJJRBF.png" width="400">

Because it is made with HTMX the experience is full responsive:

<img src="https://i.imgur.com/7HgqPlr.png" width="800">

#### **Enployee and Project registrations**

Someone of the staff of the company must be enrolled:

<img src="https://i.imgur.com/RbGuMis.png" width="400">

And it is also required to provide the name and location of the project:

<img src="https://i.imgur.com/WbK5FsA.png" width="500">

#### **Generate the requirements**

The pre-requirement order has the primary data. We can fill the company with all of its employees and projects. We can input a discount, the type of service, and the documents it will generate; by default, it will create the quotation and the requirement:

<img src="https://i.imgur.com/AJUTnJ8.png" width="600">

In the next part, the app is capable to add as many tests as we want; we just have to introduce the lab and the test.  It will pull the data from the admin panel and be ready for use.

<img src="https://i.imgur.com/Z6Rgauu.png" width="600">

The last part of the form is to add the payment conditions, which indicates how the total cost will be divided into parts.

<img src="https://i.imgur.com/P1aM5RS.png" width="200">

As soon as we save the form. A detailed total bill will be calculated and there are two documents to be found. As we advance into the order requirement it will show 4 documents.

<img src="https://i.imgur.com/DF1qHcY.png" width="600">

* The order quotation (pdf)

    <img src="https://i.imgur.com/Mbb3YjR.png" width="400">

* The requirements for the order (pdf)

    <img src="https://i.imgur.com/d7m8CHj.png" width="400"><img src="https://i.imgur.com/LtK56WS.png" width="400">

* The execution order (pdf)

    <img src="https://i.imgur.com/7Um7SpK.png" width="400">

* The liquidation sheet for the order (pdf)

    <img src="https://i.imgur.com/Wo1xm6N.png" width="400">

**The content is private has CR**

### 2. Test Implementation
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

* I'm going to use an instance in Linode
* For deploy just pull the code to Linode instance
* Run the docker-compose-prod.yml file

## How to Contribute

## How to Use the Project

## Tests

## Licence GNU GPLv3

### +Info

- [helper link](https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django)
- [helper link](https://forum.djangoproject.com/t/items-are-not-being-added-in-the-cart/10564/26)
- [helper link](https://stackoverflow.com/questions/1194737/how-to-update-manytomany-field-in-django)
- [helper link](https://pythonspeed.com/articles/alpine-docker-python/)
- [helper link](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
- [helper link](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial)
- [helper link](https://computingforgeeks.com/dockerize-django-application-with-postgresql/)
- [helper link](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
