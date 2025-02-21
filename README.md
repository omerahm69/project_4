![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Project-4

This project is about restaurant management system built using Django framework.

Objective:
Is to develop a restaurant booking system where external users can reserve tables, and the site owner can manage bookings, ensuring smooth restaurant operations.

Wireframe below is the design I have chosen to build the site. The design is consistent throughout the site. The site has sex pages: Home, About Us, Menu, Booking, contact us and login.
![Wireframe](images/image.png)

User Stories and admin
All user stories entered as issues in GitHub in the
- As a user I want to book a table for one or more guets
- As a user I want to view the menu
- As a user I want a calender for booking

Admin requirements
- As an admin I want to view bookings
- As an admin I want to view bookings

Design:

ERD

Features:
Base
Navbar
- A logo image and brand name link to the home page
- A toggle button to expand or collapse the naviation links in dropdown menu.

Footer
- The footer contains
- The footer has a background color of 'footer-bg' and social media links.

a. External User Features (Guests)
1. Table Booking
- Users can select a date,time and numbers of guests.
- Available tables displayed based on capacity

2. Booking Confirmation
- Booking confirmed with date/time

3. Menu Preview
- Users can browse the restaurant menu while booking or independently.
Menu with categories (e.g., starters, mains, desserts).

4.User Registration and Login

- Guests can create accounts or book without registration.

B. Site Owner Features (Restaurant Staff)
1. Admin Dashboard
- View all bookings for any date and time.
- Manage incoming bookings (accept, reject, or modify).
- View booking details, including the number of guests and any special requests.
3. Menu Management

- Add or update menu items (dish name, description, price, category).

C. User-Friendly UI

- Mobile-responsive design for ease of use.
- Intuitive booking process (few steps).





Technologies Used
- HTML5
- CSS
-Bootstrap
- Python
- Javascript
-Cloudinary for images


Testing


Deployment

Fork
1. On Github.com, navigate to the omerahm69 Repository.
On GitHub.com, navigate to the dlhamilton/Route Me repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.
 
Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.


