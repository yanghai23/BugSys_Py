#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pullFileUtils
import updateBugFlagUtils
# import deleteLocalFile
import insertUtils

def main():
    while True:
        type = input("please input type:")
        if type == "help":
            help()
        elif type == "autoPull":
            pullFile()
        elif type == "delete":
            delete()
        elif type == "update":
            update()
        elif type == "insert":
            insert()
        elif type == "insertAll":
            insertAll()
        elif type == "exit":
            print("exit")
        else:
            help()

def help():
    print("autoPull: auto pull error file from aws\n")
    print("delete:Manually delete automatic files\n")
    print("update: Update the automatic file to the database\n")
    print("insert:Put the specified file into the database\n")
    print("insertAll:parse  the local all file to the database\n")
    print("exit:exit system\n")

def pullFile():
    print("current dates= %s" % pullFileUtils.generateTime())
    day = input("please input day = ")
    package = input("please input package name =")
    pullFileUtils.pullErrFile(day, package, pullFileUtils.generateFileName(package, day))

def delete():
    print("current dates= %s" % pullFileUtils.generateTime())
    date = input("please input date:")
    # deleteLocalFile.deleteFile("",date)
    os.system("ls")

def update():
    updateBugFlagUtils.read_config()
    print("update")


def insert():
    date = input("please insert date:")
    packageName = input("please input packageName:")
    insertUtils.insert_to_db(date,packageName)
    print("insert date = %s   packageName = %s"%(date,packageName))

def insertAll():
    date = input("please insert date:")
    insertUtils.mysql_insert(date)
    print("insert date = %s"%(date))

main()
