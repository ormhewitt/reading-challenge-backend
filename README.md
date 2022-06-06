# ReadingChallenge app for 2022 Dev Week Hackathon

Mission Statement

To develop an app that allows admins to create and track reading challenges. Users will be able to upload their book choices and track their progress. 
 
Features

MVP
* One user type (reader)
* User can register, login, logout, join the Book Riot Reading Challenge
* User can input a book for each completed challenge task. 
* User can track their progress by marking challenge tasks as completed
* Count on how many users have joined the challenge
* User can see their progress on the challenge
Stretch features
* Two user types (user and admin)
* User can register, login, logout, update and delete profile
* User can view/join reading challenges
* User can search for books for each challenge task. This will connect to Google Books API to display full title information & book cover with autocomplete search.
* User can track their progress by marking challenge tasks as completed
* Count on how many users have joined a challenge/completed a challenge task
* User can see progress on the challenge
* Suggestions on popular books for each task
* Suggestions on popular books for the whole challenge
* Admin can create/edit/delete challenges
* FAQ about the app and the reading challenges

Technical Implementation
* Python
* Django
* React
* PostgreSQL
* Javascript
* HTML
* CSS / Bootstrap 5
* Heroku deployment
* Insomnia
* Github

Target Audience
Book clubs, book stores, Meetups, individuals participating in or developing book challenges
 
Backend Implementation
Backend was developed utilizing Django and PostgreSQL. Local testing for database completed with Insomnia. Deployed on Heroku.
 
Frontend Implementation
HTML, CSS/Boostrap, Javascript and React were utilized to develop the front-end; deployed on Github. 

Developer Week Hackathon Submission - 

## Inspiration
Our book challenge app was developed to help independent book stores, book clubs and meetups design book challenges and promote participation. The idea stemmed from a desire to develop an app to track personal progress in Book Riot's Read Harder Challenge. Book Riot currently offers a downloadable PDF for individual tracking of progress and participants submit the form at the completion of the challenge. Our team believed a book challenge app could make this challenge more accessible for participants, improve progress tracking and be made available to other organizations.

## What it does
The app allows organizations to develop a challenge and participants to track their progress towards completion of each challenge they join. It allows for two different types of users (Admins and Participants). Once logged in, admins are from the hosting organization and can update the book challenge directly (topics of books) and view data for each challenge topic. Participants can join a challenge and track their progress by entering the title chosen to complete each topic of the challenge. Participant input is connected to the Google Books API and displays the book cover on their progress page. Participants also have the ability to update book title's if entered in error or a different book is chosen.

## How we built it
For frontend development, we utilized Figma for planning, HTML, CSS, Javascript and React for product development and Github for deployment. It is also connected to the Google Books API to display covers of books through a search option. For backend development, we utilized Python, Django and Insomnia for local testing of the database. Our database was initially hosted with SQLite however we transitioned it to PostgreSQL and the backend product is deployed on Heroku. In regards to product and team planning, we utilized Agile methodologies with zoom meetings, check-ins via Slack and progress tracking via Trello. The working repositories are hosted on Github.

## Challenges we ran into
Throughout the hackathon, due to significant time zone differences of teammates scheduling progress updates and planning sessions via Zoom was difficult. Most of our communication occurred through Slack and comments throughout the code itself. We also had varying levels of experience amongst teammates therefore aspects of the project often took longer than expected. User authentication was one of the most difficult aspects of the product and there were several issues with producing an authentication token, updating the backend and ultimately displaying the user's progress page. Fortunately, we were able to overcome this challenge, it did push all members of the team to learn more about the primary technologies utilized such as Bootstrap, React, and Django. We also struggled with the development of the permissions in Python for the backend. Additional research, question asking and problem solving allowed us to address and overcome this challenge.

## Accomplishments that we're proud of
Overall, I think we are most proud of the ability to work together as team despite time zone differences and varying abilities. Most of our team members were learning new libraries and frameworks as we developed the app therefore production took longer than expected. Within the app, our goal for the hackathon was to have the Book Riot challenge active and we were able to achieve this. Authentication and permissions were the most difficult aspects of the challenge and one team member in particular worked diligently to solve the issues. Despite a relative short period of time, all members of the team increased their knowledge, improved coding and development capabilities and learned how to effectively communicate in a virtual setting.

## What we learned
During this process, we increased our individual resourcefulness. Many aspects of the project were new to each of us and this was the first coding hackathon for all individual members of our team. There was a significant learning curve regarding bridging the front-end and back-end products and each member of the team provided feedback and assistance with problem solving and support. As each team member had previous experience with different technologies, all members increased their knowledge of Bootstrap, Javascript, Python, Django and React. We also learned about the implementation of the app, deploying on separate resources, and the development of an app from scratch. Time management was also put to test during this challenge and improved our ability to ask direct and helpful questions, review resources and implement unfamiliar processes within the project.

## What's next for Reading Challenge App
While we were able to achieve most of our goals for this hackathon, our team would like to add additional features such as activating the other reading challenges, developing a process for additional challenges to be added, and provide aggregated data regarding books utilized to complete the challenge, number of participants and topics of challenge completed. We would also like to add an additional color schema and possible design to improve the admin and user experience.
