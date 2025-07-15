import os
import json
import re
import itertools
from datetime import date

taskList = []
jsonFileName = './tasks.json'
id_generator = itertools.count()

def checkJSONFile():

    if os.path.exists(jsonFileName):
        print("Json File already exists")
        return True
    else:
        with open(jsonFileName, "w") as file:
            file.write("")
            return True
        
def checkCommand(inputCommand):
    if re.search("^add", inputCommand):
        addTask(inputCommand)
    elif re.search("^update", inputCommand):
        updateTask(inputCommand)
    elif re.search("^delete", inputCommand):
        deleteTask(inputCommand)
    elif re.search("^mark-in-progress", inputCommand):
        markInProgress(inputCommand)
    elif re.search("^mark-done", inputCommand):
        markDone(inputCommand)
    elif re.search("^list$", inputCommand):
        listAllTasks()
    elif re.search("^list done$", inputCommand):
        listAllDone()
    elif re.search("^list todo$", inputCommand):
        listToDo()
    elif re.search("^list in-progress$", inputCommand):
        listInProgress()
    elif re.search("^quit$", inputCommand) or re.search("^exit$", inputCommand):
        quit()
    else:
        print("invalid input")

def nextId():      
    return next(id_generator)

def addTask(inputCommand):

    with open(jsonFileName, 'r') as file:
        try:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
        except json.JSONDecodeError:
            existing_data = []

    taskId = nextId()
    
    parseCommand =  re.split("\"*\"", inputCommand)
    taskDescription = parseCommand[1]

    taskStatus = "new"

    createdDate = date.today().isoformat()
    lastUpdateDate = date.today().isoformat()


    newTask = {
        "taskId": taskId,
        "taskDescription": taskDescription,
        "taskStatus": taskStatus,
        "createdDate": createdDate,
        "lastUpdateDate": lastUpdateDate
    }

    existing_data.append(newTask)

    with open(jsonFileName, "w") as file:
        json.dump(existing_data, file)
        print(f"Task added successfully (ID: {taskId})")

        
def updateTask():
    print()

def deleteTask():
    print()

def markInProgress():
    print()

def markDone():
    print()

def listAllTasks():
    with open(jsonFileName, 'r') as file:
        try:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
        except json.JSONDecodeError:
            existing_data = []

    print(existing_data)

def listAllDone():
    with open(jsonFileName, 'r') as file:
        try:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
            else:
                for data in existing_data:
                    if data['taskStatus'] == "done":
                        print (data)
        except json.JSONDecodeError:
            existing_data = []

def listToDo():
    with open(jsonFileName, 'r') as file:
        try:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
            else:
                for data in existing_data:
                    if data['taskStatus'] != "done":
                        print (data)
        except json.JSONDecodeError:
            existing_data = []

def listInProgress():
    with open(jsonFileName, 'r') as file:
        try:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
            else:
                for data in existing_data:
                    if data['taskStatus'] == "in-progress":
                        print (data)
        except json.JSONDecodeError:
            existing_data = []

