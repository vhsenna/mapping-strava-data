# Mapping Strava Data

![](strava-mapping-data.gif)

Have you ever wondered about all the activities you've recorded over the years on Strava? As a 10-year Strava user with over 21,000km logged, I was curious to see all my bike rides in one place. That's when I realized that I could do this using the Strava API. I'm excited to share this tool with others, so that they too can see their biking (or running) journey on Strava in a new and exciting way.

This project consists in a web application that provides a interactive and user-friendly way to visualize Strava activities on a map. It is built with Python and Django and connects to Strava API to log users in and collect their activities.

## Features
- User login with Strava API
- Display of user's activities on a interactive map
- Collection of user's activities from Strava API

## Requirements
- Python 3.10
- Django 4.1
- Strava API access (sign up at https://developers.strava.com/)

## Setup
1. Clone this repository
2. Create a virtual environment and activate it
3. Install the required packages with `pip install -r requirements.txt`
4. Add Strava API access credentials to the environment variables or settings.py file
5. Run the server with `python manage.py runserver`
6. Access the application at http://localhost:8000/

## Contributions
This is an open-source project and any contributions are welcome! If you have an idea for a new feature, report a bug, or have any other suggestions, feel free to submit a pull request or report the issue.
