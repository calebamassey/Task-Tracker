import os
import json
import re
import itertools
import shlex
from datetime import date
from operator import itemgetter

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
    used_ids = set()

    if os.path.exists(jsonFileName):
        with open(jsonFileName, 'r') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    used_ids = {int(task["taskId"]) for task in data if "taskId" in task}
            except json.JSONDecodeError:
                pass

    for i in itertools.count():
        if i not in used_ids:
            return i
        
def sortList(existingList):
    newList = sorted(existingList, key=itemgetter('taskId'))
    return newList

def addTask(inputCommand):
    with open(jsonFileName, 'r') as file:
        try:
            existingData = json.load(file)
            if not isinstance(existingData, list):
                existingData = []
        except json.JSONDecodeError:
            existingData = []

    taskId = nextId()
    
    parseCommand =  shlex.split(inputCommand)

    if len(parseCommand) != 2:
        print("Incorrect number of arguments: command must be \"add task_description\"")
    else:
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

        existingData.append(newTask)

        with open(jsonFileName, "w") as file:
            json.dump(sortList(existingData), file)
            print(f"Task added successfully (ID: {taskId})")
        
        
def updateTask(inputCommand):
    parseCommand = shlex.split(inputCommand)
    if len(parseCommand) != 3:
        print("Incorrect number of arguments: command must be \"update taskId taskDescription\"")
    else:
        with open(jsonFileName, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
                else:
                    try:
                        updated = False
                        for data in existingData:
                            if int(data['taskId']) == int(parseCommand[1]):
                                data['taskDescription'] = parseCommand[2]
                                data['lastUpdateDate'] = date.today().isoformat()
                                with open(jsonFileName, "w") as file:
                                    json.dump(existingData, file)
                                    print(f"Task has updated successfully (ID: {data['taskId']})")      
                                    updated = True
                        if updated == False:
                            print(f"{parseCommand[1]} is an invalid ID")
                    except(ValueError):
                            print(f"{parseCommand[1]} is an invalid ID")
            except json.JSONDecodeError:
                existingData = []

def deleteTask(inputCommand):
    parseCommand = shlex.split(inputCommand)
    if len(parseCommand) != 2:
        print("Incorrect number of arguments: command must be \"delete taskId\"")
    else:
        with open(jsonFileName, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
                else:
                    try:
                        updated = False
                        newData = []
                        for data in existingData:
                            if int(data['taskId']) != int(parseCommand[1]):
                                newData.append(data)
                            else:
                                updated = True
                                print(f"Task has been deleted (ID: {data['taskId']})") 
                        if updated == False:
                            print(f"{parseCommand[1]} is an invalid ID")
                        with open(jsonFileName, "w") as file:
                            json.dump(sortList(newData), file)
                    except(ValueError):
                            print(f"{parseCommand[1]} is an invalid ID")
            except json.JSONDecodeError:
                existingData = []

def markInProgress(inputCommand):
    parseCommand = shlex.split(inputCommand)
    if len(parseCommand) != 2:
        print("Incorrect number of arguments: command must be \"mark-in-progress taskId\"")
    else:
        with open(jsonFileName, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
                else:
                    try:
                        updated = False
                        for data in existingData:
                            if int(data['taskId']) == int(parseCommand[1]):
                                data['taskStatus'] = 'in-progress'
                                data['lastUpdateDate'] = date.today().isoformat()
                                with open(jsonFileName, "w") as file:
                                    json.dump(existingData, file)
                                    print(f"Task Status has been updated to In Progress (ID: {data['taskId']})") 
                                    updated = True     
                        if updated == False:
                            print(f"{parseCommand[1]} is an invalid ID")
                    except(ValueError):
                            print(f"{parseCommand[1]} is an invalid ID")
            except json.JSONDecodeError:
                existingData = []

def markDone(inputCommand):
    parseCommand = shlex.split(inputCommand)
    if len(parseCommand) != 2:
        print("Incorrect number of arguments: command must be \"mark-done taskId\"")
    else:
        with open(jsonFileName, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
                else:
                    try:
                        updated = False
                        for data in existingData:
                            if int(data['taskId']) == int(parseCommand[1]):
                                data['taskStatus'] = 'done'
                                data['lastUpdateDate'] = date.today().isoformat()
                                with open(jsonFileName, "w") as file:
                                    json.dump(existingData, file)
                                    print(f"Task Status has been updated to Done (ID: {data['taskId']})") 
                                    updated = True     
                        if updated == False:
                            print(f"{parseCommand[1]} is an invalid ID")
                    except(ValueError):
                            print(f"{parseCommand[1]} is an invalid ID")
            except json.JSONDecodeError:
                existingData = []

def listAllTasks():
    with open(jsonFileName, 'r') as file:
        try:
            existingData = json.load(file)
            if not isinstance(existingData, list):
                existingData = []
        except json.JSONDecodeError:
            existingData = []
    for data in existingData:
        print(data)

def listAllDone():
    with open(jsonFileName, 'r') as file:
        try:
            existingData = json.load(file)
            if not isinstance(existingData, list):
                existingData = []
            else:
                for data in existingData:
                    if data['taskStatus'] == "done":
                        print (data)
        except json.JSONDecodeError:
            existingData = []

def listToDo():
    with open(jsonFileName, 'r') as file:
        try:
            existingData = json.load(file)
            if not isinstance(existingData, list):
                existingData = []
            else:
                for data in existingData:
                    if data['taskStatus'] != "done":
                        print (data)
        except json.JSONDecodeError:
            existingData = []

def listInProgress():
    with open(jsonFileName, 'r') as file:
        try:
            existingData = json.load(file)
            if not isinstance(existingData, list):
                existingData = []
            else:
                for data in existingData:
                    if data['taskStatus'] == "in-progress":
                        print (data)
        except json.JSONDecodeError:
            existingData = []

