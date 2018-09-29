#-*- coding:utf-8 -*-
from flask_settings import CONFIG
import pymysql


def func():
    conn = pymysql.connect(**CONFIG)
    cursor = conn.cursor()
    sql1 = 'CREATE TABLE MeetingRoom(id int(10) NOT NULL AUTO_INCREMENT,name varchar(255) NOT NULL,PRIMARY KEY (id));'
    sql2 = 'CREATE TABLE UserInfo(id int(10) NOT NULL AUTO_INCREMENT,username varchar(255) NOT NULL,password varchar(255) NOT NULL,PRIMARY KEY (id));'
    sql3 = 'create table ReserveRecord(id int(10) NOT NULL AUTO_INCREMENT primary key,data date NULL,timeline integer(10) NULL,user int,room int,foreign key(user) references userinfo(id),foreign key(room) references meetingroom(id) );'
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    conn.commit()

if __name__ == '__main__':
    func()