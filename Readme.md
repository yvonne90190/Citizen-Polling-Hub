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
1. User（用戶表）：
  a. user_id：用戶唯一標識符。
  b. username：用戶名。
  c. email：用戶的電子郵件地址。
  d. password：用戶的加密密碼。
  e. registration_date：用戶註冊日期。
2. Poll （公投議題表）：
  a. poll_id：公投唯一標識符。
  b. title：公投的標題。
  c. description：公投的描述。
  d. creator_id*：創建公投的用戶ID（與User實體中的user_id相關聯）。
  e. start_date：公投開始日期。
  f. end_date：公投結束日期。
  g. is_approved：
3. Question（問題）：
  a. question_id：問題唯一標識符。
  b. poll_id：問題所屬公投的ID（與Poll實體中的poll_id相關聯）。
  c. text：問題的文字描述。
  d. question_type：問題類型（例如，單選、多選）。
4. Option（選項）：
  a. option_id：選項唯一標識符。
  b. question_id：選項所屬問題的ID（與Question實體中的question_id相關
  聯）。
  c. text：選項的文字描述。
  d. vote_count：選項收到的投票數。
5. Comment（評論）：
  a. comment_id：評論唯一標識符。
  b. user_id：發表評論的用戶ID（與User實體中的user_id相關聯）。
  c. content：評論的內容。
  d. target_type：評論針對的類型（例如，公投、問題或選項）。
Relationship:
  1. User 參與 Poll：用戶可以參與一個或多個公投。
  2. Poll 包含 Question：每個公投可以包含一個或多個問題。
  3. Question 提供 Option：每個問題可以有一個或多個選項供用戶選擇。
  4. User 選擇 Option：用戶可以在每個問題中選擇一個選項。
  5. User 發布 Comment：用戶可以對公投、問題或選項發表評論

### Relational Schema
![image](https://github.com/yvonne90190/Citizen-Polling-Hub/assets/74034659/a8a1eed2-7e77-4ab4-9279-cd4bcc2e33ff)

### ER Model
![image](https://github.com/yvonne90190/Citizen-Polling-Hub/assets/74034659/1a553cd4-73b4-478e-b985-f4166da95db2)

### system architecture
![Screenshot 2023-06-16 105254](https://github.com/dbmsFinal/documents/assets/64206644/5deec497-8428-4712-9ccd-07db158f6bc3)



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
