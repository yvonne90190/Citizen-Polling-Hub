# Citizen Polling Hub

***
### System Description
The main purpose of our referendum website is to allow users to create and participate in various referendums, thereby collecting opinions and views, and conducting public opinion polls on specific issues. This website can have many applications, such as political issues, product evaluations, community activities, and more.

***

### frontend repo portal: 
https://github.com/dbmsFinal/frontend
### backend repo portal:
https://github.com/dbmsFinal/backend

***
### Demo video
https://youtu.be/7V72-Nncm68

***
### User Requirements
#### Entity type:
- User Table:
  - user_id: Unique identifier for the user.
  - username: User's username.
  - email: User's email address.
  - password: Encrypted password for the user.
  - registration_date: User's registration date.
- Poll Table:
  - poll_id: Unique identifier for the poll.
  - title: Title of the poll.
  - description: Description of the poll.
  - creator_id*: User ID of the creator of the poll (associated with user_id in the User entity).
  - start_date: Start date of the poll.
  - end_date: End date of the poll.
  - is_approved:
- Question Table:
  - question_id: Unique identifier for the question.
  - poll_id: ID of the poll to which the question belongs (associated with poll_id in the Poll entity).
  - text: Textual description of the question.
  - question_type: Type of the question (e.g., single-choice, multiple-choice).
- Option Table:
  - option_id: Unique identifier for the option.
  - question_id: ID of the question to which the option belongs (associated with question_id in the Question entity).
  - text: Textual description of the option.
  - vote_count: Number of votes received by the option.
- Comment Table:
  - comment_id: Unique identifier for the comment.
  - user_id: User ID of the commenter (associated with user_id in the User entity).
  - content: Content of the comment.
  - target_type: Type of entity the comment is targeting (e.g., poll, question, or option).


#### Relationship:
- User participates in Poll: Users can participate in one or more polls.
- Poll contains Question: Each poll can contain one or more questions.
- Question provides Option: Each question can have one or more options for users to choose from.
- User selects Option: Users can choose one option for each question.
- User publishes Comment: Users can comment on polls, questions, or options.

***

### Relational Schema
![image](https://github.com/yvonne90190/Citizen-Polling-Hub/assets/74034659/a8a1eed2-7e77-4ab4-9279-cd4bcc2e33ff)

### ER Model
![image](https://github.com/yvonne90190/Citizen-Polling-Hub/assets/74034659/1a553cd4-73b4-478e-b985-f4166da95db2)


### system architecture
![Screenshot 2023-06-16 105254](https://github.com/dbmsFinal/documents/assets/64206644/5deec497-8428-4712-9ccd-07db158f6bc3)

***

## How to use

### Backend

#### 1. Install python3 and pip3
```
sudo apt-get install python3

```
#### 2. Install dependency
```
python3 install -r requirements.txt
```
#### 3. Run server
```
python3 main.py
```
### Frontend

#### dependencies install

```sh
npm install
```

##### Compile and Hot-Reload for Development

```sh
npm run dev
```
