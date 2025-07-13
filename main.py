import tracker_app

def main():
    tracker_app.checkJSONFile()
    i=0
    
    while i != -1:
        tracker_app.checkCommand(input("task-cli: "))



if __name__ == "__main__":
    main()