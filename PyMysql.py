#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql
import cryptography


# In[2]:


analysis_db = pymysql.connect(
    user='root', 
    password='jslove0130!', 
    host='127.0.0.1', 
    db='analysis', 
    charset='utf8'
)


# In[3]:


curs = analysis_db.cursor()


# In[5]:


analysis = "create table job_ability("\
"id int(255) not null auto_increment, "\
"user_id varchar(15) not null,"\
"cv_id bigint not null,"\
"created datetime not null,"\
"answer varchar(60) not null,"\
"relationship float(4,2) not null,"\
"analysis float(4,2) not null, "\
"sincerity float(4,2) not null, "\
"passion float(4,2) not null, "\
"communication float(4,2) not null,"\
"tactical float(4,2) not null,"\
"professional float(4,2) not null,"\
"ownership float(4,2) not null, "\
"self_development float(4,2) not null, "\
"leadership float(4,2) not null,"\
"primary key(id))"

try:
    with analysis_db.cursor() as cursor:
        cursor.execute(analysis)
    analysis_db.commit()
    
finally:
    analysis_db.close()
    


# In[6]:


def drop_table():
    
    conn = pymysql.connect(user='root', 
    password='jslove0130!', 
    host='127.0.0.1', 
    db='analysis', 
    charset='utf8')
    
    try:
        with conn.cursor() as cursor:
            sql = 'DROP THE TABLE job_ability'
            cursor.execute(sql)
            conn.commit()
        
    finally:
        conn.close()


# In[8]:


analysis_db.commit()


# In[12]:


conn = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password ='jslove0130!',
                      charset='utf8')

cursor = conn.cursor()

sql = '''create database developer'''

cursor.execute(sql)
conn.close()


# In[13]:


conn = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password ='jslove0130!',
                      db='developer',
                      charset='utf8')

cursor = conn.cursor()

sql = ''' create table user(
id int(11) not null auto_increment primary key,
email varchar(255),
department varchar(255)
)'''

cursor.execute(sql)
conn.close()


# In[14]:


conn = pymysql.connect(user='root', 
    password='jslove0130!', 
    host='127.0.0.1', 
    db='developer', 
    charset='utf8')

cursor = conn.cursor()

sql = "insert into user (email, department) values(%s, %s)"

cursor.execute(sql, ("hr_lim@sunandmoon.com", "HR"))
cursor.execute(sql, ("hr_cho@sunandmoon.com", "HR"))
cursor.execute(sql, ("dev_choi@sunandmoon.com", "DEV"))
cursor.execute(sql, ("ops_bae@sunandmoon.com", "OPS"))

conn.commit()
conn.close()


# In[15]:


# 위의 error는 이미 이전에 설치했던 것이기에 뜬 것이며, 확인 결과 mysql에 생성된 database에서 table이 잘 생성되었음을 알 수 있었다

