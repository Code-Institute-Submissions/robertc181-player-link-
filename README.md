# Player Link

# Contents

1. Summary
2. UX
    * Strategy
    * Scope
    * Structure
    * Skeleton
    * Surface
3. Features
    * Existing Features
    * Features left to implement
4. Bugs
5. Technologies used
6. Testing
7. Deployment
   * Github Pages
   * heroku
8. Credits
   * Content
   * Acknowledgements

# Summary

Player Link is an online platform that will link football players with scouts, So that scouts can watch a football player and find out when they will be playing there next football games and more information about that player, such as current team , position , preffered foot etc. This platform will also allow a player to view which scouts are watching them and which scouts will be going to thier games. A player will be able to create an account with Player Link and put up information about themselves, they can also create an event which they can set a time place and name. If a scout searches for a player on Player Link they will be allowed to view a players events and click on the ones that they wish to go to. 

A scout can also sign up with Player Link to find talented footballers and get more information about them and there football games. They will have a profile where they can search for players and view all players profiles and see thier events 

# UX

## App Goals

My objective with Player Link is to firstly allow scouts who are struggling to find players around thier area to scout and help them connect with players and hopefull come accross some talent, Player Link allows a scout to search for a players name then click to view that players profile. A scout can click to attend an event such as a game or tournament which will notify the player that the scout is going to thier event. As a player this allows many player with a chance to connect with more scouts and hopefully get a better chance to showcase thier talent and invite more scouts to thier games.

## Strategy

### New site user's goals:

1. As a new visitor to the website I want to navigate the site with ease and no confusion.

2. As a new visitor to the website I want to be able to easily find where to register.

3. As a new visitor to the website I want to be able to sign in.

4. As a new visitor to the website I want to be able to register as a scout or player with no confusion.

5. As a new visitor to the website I want to be able to create a profile.

6. As a new visitor to the website I want to be able to get around my profile with ease and no confusion.

7. As a new visitor to the website I want to be able to edit my profile.

8. As a new visitor to the website I want to be able to signout of my profile with no confusion.

9. As a new visitor to the website I want to be able to view the website on phone desktop and tablet

 
### player site user's goals:

1. As a player I want to be able to create an event.

2. As a player I want to be able to edit an event.

3. As a player I want to be able to delete an event.

3. As a player I want to be able to see if any scouts are attending my events.

### scout user's goals

1. As a scout I want to be able to search for a player.

2. As a scout I want to be able to view a players profile.

3. As a scout I want to be able to attend a players event.


## Scope

### Functional requirements:

### For ease of use:

* Navigation bar which is simple and easy to navigate

### To ensure the database is up to date and editable:

* Function to register
* Function to login
* Function to logout
* Function to create profile
* Function to edit profile
* Function to create event
* Function to edit event
* Function to delete event 
* Function to search player
* Function to open player profile display
* Function to watch event

### Content requirements:

### To ensure the site is visually appealing and to draw the user's eye:
* clear colours 
* vibrant cololours used fir flash messages and buttons

## Structure

### Interaction design:

* User friendly interface to ensure usability 

* Responsive and visible buttons which change on hover to provide user feedback as they navigate the site

### Information Architecture:

* Navigation bar at the top of the page
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive forms to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing


## Skeleton

### wireframe

* - [Wireframes](https://github.com/robertc181/player-link-/tree/master/Wireframes)

## Surface

### The intention of the website is to be clean, crisp and clear

* The colour scheme is grey and white to let the purple used in the flash messages and buttons really stick out

# Plan

## initial plan

- [Flow Chart](https://github.com/robertc181/player-link-/blob/master/Plan/IMG_0679.jpg)
- [Routing plan](https://github.com/robertc181/player-link-/blob/master/Plan/IMG_0691.jpg)
- [Data Structure](https://github.com/robertc181/player-link-/blob/master/Plan/data-structure)

## Changes to plan

1. Instead of creating to diferent profile types for a scout and a player I am now using a generic users database to store a users data where a user has a user_type which will be a player or a scout

2. I have changed the data structure to have a users Db and a profiles db so a user registers and creates a user then can create profile to create thier profile


# Features

## Existing Features

| Feature        | Detailes           | 
| ------------- |:-------------:| 
| login     | The user can register and log into their own account with personalised features | 
| logout     | There is a log out functionality on the page | 
| register     | The user can register and create an account | 
| create profile     | After a user has registered they can then create a profile | 
| edit profile     | After a user has created a profile they can edit thier profile and change information | 
| create event     | A user can create an event for a game or tournament they are due to attend | 
| edit event     | A player can edit thier event after it has been created | 
| delete event     | A player can delete an event | 
| search player     | A scout can search for players | 
| open player profile account     | A scout can open a players account and see all of thier events | 
| watch event     | A scout can click to watch an event and the player will see that he is going | 


## Features left to implement

| Feature        | Detailes           | 
| ------------- |:-------------:| 
| follow player     |  | 
| see scouts     |  | 
| watched events     |  | 
| going events     |  | 

# Bugs

| Feature        | Detailes           | 
| ------------- |:-------------:| 
| follow player     |  | 
| see scouts     |  | 
| watched events     |  | 
| going events     |  | 

# Technologies Used

* HTML
* CSS
* Python
* Git
* github
* Google Chrome
* Flask
* MongoDb
* Heroku
* Jinja


## Testing

### New site user's testing:

1. As a new visitor to the website I want to navigate the site with ease and no confusion.
    * A navbar with links clearly labeled and working is present throughout the website.

2. As a new visitor to the website I want to be able to easily find where to register.
    * A button clearly labeled register is present in the header of the page.

3. As a new visitor to the website I want to be able to sign in.
    * A link clearly labeled sign in  is present in the navbarr on the page.

4. As a new visitor to the website I want to be able to register as a scout or player with no confusion.
    * After the register button has been clicked a register page opens where you can choose to register as a scout or a player.

5. As a new visitor to the website I want to be able to create a profile.
    * After you have registerd as a player or scout you are brought to the relevent create profile page for either a scout or player.

6. As a new visitor to the website I want to be able to get around my profile with ease and no confusion.
    * After you have created a profile you are brought to your profile all buttons to perform any actions are clearly visible and present.

7. As a new visitor to the website I want to be able to edit my profile.
    * When in your profile the edit button brings you to a form to edit your profile which after submitting updates your profile.

8. As a new visitor to the website I want to be able to signout of my profile with no confusion.
    * a sign out link is present in the navbar which after clicking brings you back to the home page.

9. As a new visitor to the website I want to be able to view the website on phone desktop and tablet
    * The website is readable and responsive in all screen sizes.


### player site user's testing:

1. As a player I want to be able to create an event.
    * A button create event brings you to a form that creates an event that visible bellow in the events table.

2. As a player I want to be able to edit an event.
    * An edit event button is visable in the events table with takes you to a form that after submitting your new info updates said event.

3. As a player I want to be able to delete an event.
    * A delete button is present in the events table and deletes the event.

4. As a player I want to be able to see if any scouts are attending my events.
    * A scouts section in the events table is present which allows you to see any scouts that have clicked to go to your event.

### scout user's testing:

1. As a scout I want to be able to search for a player.
    * A serch box allows you to search for any players by name and shows the players name and current team in a table below.

2. As a scout I want to be able to view a players profile.
    * A table showing all searched related players has a button to view that players profile which takes you to said players profile.

3. As a scout I want to be able to attend a players event.
    * in the events section of the players profile a scout can click to watch avent and will show up undr scouts in the players event table.

## Performance testing:

* Tested website responsiveness using http://www.responsinator.com/
    * Results: The website is basically responsive to all device sizes.
* I used the Google Dev Tools - Network
    * Results: The site loading time is grand

All HTML pages were tested using https://jigsaw.w3.org/css-validator/validator
All but the 'base' template resulted in errors that the Lang Doctype and Title were missing. This was to be expected as the details were being extended from the base template to did not need to be added
All HTML pages resulted in errors where the Jinja template language was used
None of these are actual errors within the code
Tested the CSS using http://www.css-validator.org/
No errors were found
Tested the website on the Google Chrome browser Version 87.0.4280.88 (Official Build) (64-bit)
Results: The website was responsive and the elements performed in the way they were intended to
Tested the website on the Microsoft Edge browser Version Version 87.0.664.66 (Official build) (64-bit)
Results: The website was responsive and the elements performed in the way they were intended to
Tested the website on the Firefox browser Version 82.0.3 (64-bit)
Results: The website was responsive and the elements performed in the way they were intended to
Tested the form validation worked correctly on each of the above browsers
Results: The form correctly sent when the fields were completed as they should have been and did not when the fields had not been completed

# Deployment

## Git hub pages

1. Create a new repository or access an existing repository
2. Click the green Gitpod button to launch the project in Gitpod
3. Create an index.html file
4. Add the file to the staging area using the git add Functional
5. Commit the file using the git commit function, adding an appropriate commentary
6. Push the file to GitHub using the git commit and git push functions
7. Refresh your GitHub repository and click the 'Settings' tab
8. Scroll to the GitHub Pages section and select a publishing source
9. Click 'Save'
10. Click the URL created within the Settings - GitHub Pages section

### To clone the repository for local deployment:

1. On the main page of the repository, click the down arrow Code button
2. Click the download icon under the relevant section to clone with either HTTPS, SSH or 3GitHub CLI
4. In Git Bash, change the current directory to the location you want the directory to be stored
5. Type git clone and then paste the URL you copied in step 2
6. An example for HTTPS: git clone https://github.com/robertc181/player-link-
7. Press enter - that's it, your clone has been completed!

### Fork repo

1. Navigate to the main page of the repository you wish to fork
2. Click the Fork button on the top right hand side of the page

## Heroku

To deploy the app to Heroku from its GitHub repository, the following steps were taken:

1. From the GitPod terminal, create requirements.txt and Procfile using these commands:

     ```pip3 freeze --local > requirements.txt
     echo web: python app.py > Procfile
     ```

2. Push these files to GitHub
3. Log In to Heroku
4. 4.Select Create new app from the dropdown in the Heroku dashboard
5. Choose a unique name ('player_link') for the app and the location nearest to you
6. Go to the Deploy tab and under Deployment method choose GitHub
7. In Connect to GitHub enter your GitHub repository details and once found, click Connect
8. Go to the Settings tab and under Config Vars choose Reveal Config Vars
9. Enter the following keys and values, which must match those in the env.py file created earlier:

| Key        | Value           | 
| ------------- |:-------------:| 
| IP   | 0.0.0.0 | 
| PORT     | 5000 | 
| SECRET_KEY     | app secret key  | 
| MONGO_URI     | mongodb+srv://root:dsxigyzwsao0sozm@myfirstcluster.n0en1.mongodb.net/player_link?retryWrites=true&w=majority | 
| MONGO_DBNAME     | player_link | 

10. Go back to the Deploy tab and under Automatic deploys choose Enable Automatic Deploys
11. Under Manual deploy, select master and click Deploy Branch
12. Once the app has finished building, click Open app from the header row of the dashboard

## Credits

### Acknowledgements

* My mentor Antonio Rodriguez who has been great help with guidance and support through the project

