# MyMo

#### A commercial e-commerce website built to advertise property for sale and rent on the irish marketplace

<p align="center">
  <img width="40%" src="media/mymo.png">
</p>
 
<p align="center"><a href="https://mymo.ie/" target = "_blank">MyMo.ie</a></p>
 
## Table of Contents
 
- [**About**](#About)
- [**Clients Brief**](#clients-brief)
- [**UX/UI**](#ux-ui)
- [**Features**](#features)
- [**Technologies used**](#technologies-used)

## About

The purpose of this project was to build a functioning e-commerce site to advertise property for sale or rent on the irish market with payments via [Stripe](https://stripe.com/).

The site allows users to create an account, and advertise a property or browse available properties. It is not necessary that users register to browse the site, however they do gain access to the ability to save properties they like if they do deicde to register. The site also allows social logins from two popular vendors for a convenient way to create an account.

## Clients Brief

-   An attractive, fully responsive website to advertise property for sale or rent.
-   Allow users to create an account and give insentive to do so. (Ability to save listings)
-   Have the ability for the website to process payments.
-   Allow registered users to upload properties.
-   Have an easy to use admin panel.
-   Have the ability to mark a user as an agent.
-   Have a page to show all agents registered on the site, and a link to their page to display their current listings.
-   Allow users to mark a property as sold.
-   Have a property price register to display the price of recently sold properties.
-   Automatically handle expiring listings.
-   Have multiple tiers of advertising packages, e.g Standard and Premium.

## UX UI

-   Everything in the Client Brief was implemented, but not limited to just the brief, other features include

    -   There are filters in place which allows the user to filter properties to find one that matches their preferences easily. Coupled with a paginator which allows for a neat viewing experience.
    -   There is a contact form on the estate agents profile page which allows the user to send a message direct to an agents email which lets the agent know that the interest in the listing came from the mymo website. This page also displays the relevent information about the agent and their listings.
    -   The site allows users to save listings if registered and logged in.
    -   A signup/login form with social logins from two popular vendors.
    -   A loading page was implemented due to a lot of images being used on the website to stop poor impressions from unloaded images. There is also a loading buffer when processing payments.
    -   The site makes use of messages to give users real-time feedback on their actions.
    -   Users can see their order history, listing information, saved listings on their profile page, here they can also edit certain parts of their information, such as company logo if they are an agent.
    -   Users recieve emails informing them of the status of their listing.

## Features

-   Ability to Signup/login.
-   Ability to browse listings, with optional filtering.
-   Ability to place a listing, payments handled with custom [stripe](https://stripe.com) payment flow.
-   Ability to edit listings if owned by the user.
-   Ability to delete listings, and set listings as sold.
-   Ability to save listings if logged in.
-   Ability to view all agents registered on the site.
-   A loading page.
-   Customised 404 and 500 error pages.
-   The project contains a few security features, such as:

    -   validating login.
    -   hashing passwords.
    -   environment variables are hidden.
    -   debug is turned off in the production version.
    -   secure payments via [Stripe](https://stripe.com/)
    -   SSL certificate.

-   User Profiles
    -   Access Order History.
    -   Access information about current listings.
    -   View saved listings.
    -   Change user info, such as email address and company info.
    -   Change password.

## Technologies used

Below I have listed the programming languages, technologies, frameworks and resources used for this project.

-   **HTML5**
-   **CSS3**
-   **[SASS](https://sass-lang.com/)**
-   **Vanilla JS**
-   **J Query**
-   **Markdown**
-   **Python**
-   **Redis**
-   **Celery / Celery Beat**
-   **Git** for version control.
-   **[Github](https://github.com/)** to hold my project.
-   **[Heroku](https://heroku.com/)** to deploy my project to the web.
-   **[Django](https://www.djangoproject.com/)**
-   **[FontAwesome](https://fontawesome.com/)** for icons.
-   **[AWS S3](https://aws.amazon.com/)**
-   **SQLite3/Postgres**
-   **Google Chrome/FireFox/Edge/Safari**
-   **Developer tools for Chrome/FireFox/Edge**
-   **[Amiresponsive](http://ami.responsivedesign.is/)**
-   **[Balsamiq](https://balsamiq.com/)** to create wireframes.
-   **[W3Schools](https://www.w3schools.com/)** for help with some issues i ran into
-   **[StackOverFlow](https://stackoverflow.com/)** for help with some issues i ran into
-   **[Grammarly](https://www.grammarly.com/)** to correct grammar and spelling mistakes.
-   **[MySQL Workbench](https://www.mysql.com/products/workbench/)** to design and visualize my database.

[Back to top ↑](#mymo)
