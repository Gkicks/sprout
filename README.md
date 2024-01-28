# Sprout

Sprout is a recipe sharing website where users can view recipes. Logged in users can post recipes and comment on posted recipes

Visit the deployed site here: [Sprout](https://sprout-p4-ffedffefc60e.herokuapp.com/)

![landing-page](static/images/amiresponsive.png)

## Contents

- [Sprout](#sprout)
- [Contents](#contents)
- [User Experience (UX)](#user-experience-ux)
  - [Initial Discussion](#initial-discussion)
  - [Agile Planning](#agile-planning)
    - [Epics](#epics)
    - [User Stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagary](#imagary)
    - [Hero Image](#hero-image)
    - [Favicon](#favicon)
    - [Recipe Images](#recipe-images)
  - [Wireframes](#wireframes)
    - [Home Page](#home-page)
    - [Recipe Detail](#recipe-detail)
    - [User Recipes](#user-recipes)
    - [Create Recipe](#create-recipe)
    - [Edit Recipe](#edit-recipe)
- [Database Design](#data-base-design)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Home Page](#home-page)
    - [Recipe Detail](#recipe-detail-1)
    - [User Recipes](#user-recipes-1)
    - [Create Recipe](#create-recipe-1)
    - [Edit Recipe](#edit-recipe-1)
    - [Delete Recipe](#delete-recipe)
    - [Sign In](#sign-in)
    - [Sign Up](#sign-up)
    - [Log Out](#log-out)
    - [404.html](#404)
    - [403.html](#403)
    - [500.html](#500)
  - [Future Implementations](#future-implementations)
  - [Assesibility](#accessibility)
  - [Wave Validator](#wave-validator)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, libraries and programs used](#frameworks-libraries-and-programs-used)
- [Deployment and Local Development](#deployment)
  - [Heroku](#heroku)
  - [How to Fork](#how-to-fork)
  - [How to Clone](#how-to-clone)
- [Testing](#testing)
- [Bugs](#bugs)
  - [Resolved Bugs](#resolved-bugs)
  - [Unresolved Bugs](#unresolved-bugs)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Other](#other)
  - [Acknowledgements](#acknowledgements)

[Back to top](#sprout)

# User Experience (UX)

## Initial Discussion

Sprout is a recipe sharing website which allows users to post recipes, rate recipes and leave comments on the recipe.

The site is designed to be intuitive and provide a enjoyable user experience.

Security is an important part of the site – ensuring user data is kept secure and, unauthorised users aren’t able to access or change parts of the site if they are not authorised to do so.

## Agile Planning

This site was produced using Agile Methodologies. The project was designed in 6 sprints with use sprint planned each half week. I used Github’s Project Board to plan this project.

Projects were broken down in the following ways:

Priorities – Tasks were labelled must-have, should-have or nice-to-have. The must-have tasks were prioritized.

Estimates – These were assigned on the expected complexity of a task and how long I expected it to take to complete. The simplest tasks in the project were assigned an estimate of 1 and, the task I thought was most complex was assigned an estimate of 8. The estimates are shown in the light grey label on the project board. In total there were 101 estimates. 40 of these were must-haves (39.5%), 22 were should-haves (22%) and 39 were nice-to-haves (38.5%)

All cards on the project board can be opened to see the full critea that needs to be met in order to close the task. The full project board can be found here: [Project Board](#<https://github.com/users/Gkicks/projects/6/views/1)>

![Project Board](static/images/project-board.png)

### Epics

The project was broken down into 7 Epics. These were:

#### Epic 1 – Initial Setup

Setting up the coding environment, installing necessary libraries, creating the project and app, creating a superuser and creating the databases

#### Epic 2 – Create Pages

Creating the structure of the website and the individual pages that make up this project

#### Epic 3 – Recipes

Functionality to create, view, edit and delete a recipe

#### Epic 4 – Comments

Functionality to create, view, edit and delete comments relating to a specific recipe

#### Epic 5 – Authentication

Allows the user to register an account, login, logout and delete an account

#### Epic 6 – Deployment

The website to be deployed to Heroku

#### Epic 7 – Testing and Documentation

Testing the website to ensure it is working as it should. Completing README documentation

### User Stories

Each Epic was further broken down into User Stories:

#### Epic 1 – Initial Setup

• As a developer I need to create a PostgresSQL instance, using ElephantSQL, so I can set up models – estimate 1 – must-have
• As a developer I need to set up the developing environment so that I can implement the necessary features – estimate 1 – must-have
• As a developer I need to create a superuser so I can have admin access to the database – estimate 1 – must have
• As a developer I need to create static resources to contain my css and js files and images – estimate 1 - must have

#### Epic 2 – Create Pages

• As a developer I need to create the base.html page to give the structure that other page layouts are b estimate ased on – estimate 2 – must have
• As a developer I need to create a navbar so that the user can navigate throughout the site – 2 – must have
• As a developer I need to create a footer so that the user can link to the social media accounts - estimate 2 – must have
• As a developer I need to create a home / landing page where the user can easily see the recipe posts – estimate 3 – must have
• As a user I want to see a list of my current recipes so I can see the recipes I've published and choose which to edit or delete – estimate 5 – must have
• As a developer I want to create a 404 error page so that users are alerted if they have accessed a page that doesn’t exist – estimate 2 – should have
• As a developer I want to create a 403 error page so that users are alerted if they have accessed a page they don't have permission to view – estimate 2 – should have
• As a developer I want to create a 500 error page so that users are alerted if an internal error occurs – estimate 2 – should have

#### Epic 3 – Recipes

- As a user I want to create a recipe post so that I can share my recipe with other users – estimate 5 – must have
- As a user I want to click on a recipe post which will open in a new page so I can see the full recipe – estimate 3 – must have
- As a user I want to edit a recipe so I can correct any errors or make updates – estimate 3 – must have
- As a user I want to delete a recipe so I can stop sharing it with other users – estimate 3 – must have
- As a user I want to filter by type of recipe (main, sides, etc) so I can just see the recipes for want I am planning to make – estimate 5 – should have
- As a user I want to like or dislike a recipe to help other users make a decision about making a recipe – estimate 5 – should have
- As a user I want to search for a recipe to find a recipe if I already have an idea of what I’m looking for – estimate 5 – nice to have
- As a user I am able to rate a recipe to inform others how much I liked the recipe – estimate 5 – nice to have

#### Epic 4 – Comments

- As a user I want to comment on a recipe so I can give feedback to the author and share my views with other users – estimate 3 – should have
- As a user I want to view comments that all users have left so that I can see feedback on a recipe – estimate 2 – should have
- As a user I want to edit a comment so I can correct any errors or make updates – estimate 3 – should have
- As a user I want to delete a comment so I can stop sharing it with other users – estimate 3 – should have
- As a user I want to like comments to help other users make a decision how helpful that comment is – estimate 5 – nice to have

#### Epic 5 – Authentication

- As a developer I need to install allauth so the user can register an account, login and logout – estimate 2 - must have
- As a site owner I want the allauth forms to be customised so they fit in with the style of the rest of the site – estimate 5 – should have
- As a user I want to delete my account so it no longer exists – estimate 3 – should have

#### Epic 6 – Deployment

- As a developer I need to deploy the project, to Heroku, so that customers are able to access the website – estimate 1 – must-have

#### Epic 7 – Testing and Documentation

- As a developer I want to complete automated testing so I can make sure all area of the website are working as they should be – estimate 8 – must have
- As a developer I need to write a README so that all information regarding the project is easily understood by those who need to – estimate 5 – must have
- As a developer I would like to get feedback from other users so I can see if my project is commercially viable – estimate 3 - nice to have

[Back to top](#sprout)
