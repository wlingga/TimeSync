# TimeSync
Devpost ULR: https://devpost.com/software/timesync-3tyfro

# Inspiration
The transition to online schooling has made it difficult for students to work with friends. The decrease in communications among students has left them feeling lost in this challenging time. Thus to solve the lack of emotional support, we have decided to create this web app that aids and encourages the planning of group-working.

# What it does
Timesync is a web app that connects you with different people, so you don’t have to be alone in your work. Once you sign up with your social media information, you will be able to add a daily to-do list. Using the to-do list, Timesync can search its database for other users doing similar activities with you, and provide you with a list of potential work-buddies. The site can provide other users’ names and instagram handles so that maybe a work together party call can be made.

# How we built it
Our team divided into two groups for the project: backend and frontend.

Using Flask and sqlalchemy, the backend team built 2 models for storing data for tasks and users. We began by creating a user authentication and validation system by using encrypted passwords. We also configured routes for different directories including different pages and the necessary actions, such as updating and deleting. We then configured it to appropriate html files, to wire the backend and the frontend of the web app to receive and store data properly. Once proper data input was established, we coded an algorithm to compare the tasks among users and their task data to match the result.

The frontend would design the overall visuals of Timesync using html and css, while creating forms to allow for the backend team to collect data. Multiple sites were created to guide the users, including the landing, todo-list additions, matchfinder, signup and login pages. Javascript and some flask was used for interactions with the user, such as adding new items that can be deleted to the site when a form is submitted.

# Challenges we ran into
We began our developing journey by struggling to understand the structure of Github. We were fortunate to get assistance by our lovely mentors who taught us the general standards for the use of branches, the use of merges, and the commands “push”, “pull”, “fetch” for efficient collaboration.

Although most of us were familiar with python, we were all newcomers to Web Development, starting from Flask, SQL, to CSS, so forming the general structure was challenging. This required all of us to learn different materials to be stitched together. This required every individual part to function successfully, and consequently there were long hours of debugging.

# Accomplishments that we're proud of
We learned and were able to utilize github, flask, sql and many more new tools and libraries to build a working web app.

# What we learned
We learned how to develop a web app with a user client from the ground up.

# What's next for TimeSync
We would like to improve our frontend aesthetics, more variety of input type.
