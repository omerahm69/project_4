![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Project-4

This project is about restaurant management system built using Django framework. It allows external users to book tables, view the menu, and interact with the restaurant, while site owners can manage bookings and ensure smooth restaurant operations.

Objective:
The goal of this project is to develop a restaurant booking system where:
. Users can reserve tables for one or more guests
. The site owner can manage bookings efficiently ensuring smooth restaurant operations.

Wireframe
 The design of the site follows a consistent theme throughout all pages.
 
 Pages in the Website
The site consists of sex pages:
1. Home
2. About Us
3. Menu
4. Booking
5. Contact Us
6. Login/Register

![Wireframe](images/image.png)

User Stories and admin requirements

All user stories and admin requirement entered as issues in GitHub. However Agile methodology was not implemented from the start.

User Stories & Admin Requirements

- As a user I want to book a table for one or more guets
- As a user I want to view the menu
- As a user I want a calender for booking

Admin Requirements
- As an admin I want to view bookings
- As an admin I want to view bookings

Database Design
The database design follows an Entity-Relationship Diagram (ERD) to define how data is structured and related.

ERD

Features:
A. Base Features
Navbar

- Displays logo image and brand name link to the home page
- Includes a toggle button to expand or collapse the naviation links in dropdown menu.

Footer
- The footer contains social media links and a consistent footer background color.

B. External User Features (Guests)
1. Table Booking
- Users can select a date,time and numbers of guests.
- Available tables displayed based on restaurant capacity

2. Booking Confirmation
- User recieve a confirmation of their booking with date and time details.

3. Menu Preview
- Users can browse the restaurant menu while booking or independently.
- The menu includes categories starters, mains, desserts.

4.User Registration and Login

- Guests can create accounts or book without registration.

C. Site Owner Features (Restaurant Staff)

1. Admin Dashboard
- View all bookings for any date and time.
- Manage incoming bookings (accept, reject, or modify).
- View booking details, including the number of guests and any special requests.

2. Menu Management

- Add or update menu items (dish name, description, price).

D. User-Friendly UI

- Mobile-responsive design for ease of use.
- Intuitive booking process with few steps.



Technologies Used
-Frontend: HTML5, CSS, Bootstrap, JavaScript

- Backend: Python, Django

- 

- Media Storage: Cloudinary (for images)

Testing
The system has undergone rigorous manual testing to ensure functionality, usability and responsiveness.

Deployment Instructions

Fork the Repository
1. On Github.com, navigate to the omerahm69 repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.
 
Clonning the Repository
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal or Command Prompt
4. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.




1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.


