tasks = []
   
class Task:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.status = "not done"
        
    def addTask(self):
        global tasks
        self.title = input("Enter title: ")
        self.description = input("Enter Description: ")
        tasks.append(self)
        print("Task added successfully..!!")
        input("Press Enter key to continue...")

    def removeTask(self):
        global tasks
        if len(tasks) == 0:
            print("You are having no task to remove, Please add some first..!!")
        else:   
            print("You have tasks: ")
            taskNo = 1
            for task in tasks:
                print(f"Task{taskNo} => Title : {task.title} - Status : {task.status}")
                taskNo += 1
            
            isValidTaskNo = False
            while not isValidTaskNo:
                try:
                    removedTaskNo = int(input("Choose the task no, you want to remove: "))
                    if removedTaskNo <= 0 or removedTaskNo > len(tasks):
                        raise IndexError("⚠️ You've entered a task no out of range, Please provide a valid task no: ")
                except IndexError as e:
                    print(e)
                    isValidTaskNo = False
                    continue
                except ValueError:
                    print("⚠️ Only integer values are allowed for task no..!")
                    isValidTaskNo = False
                    continue
                
                del tasks[removedTaskNo-1]
                print("Task removed successfully..!!")
                isValidTaskNo = True
        input("Press Enter key to continue...")
        
    def showTasks(self):
        global tasks
        if len(tasks) == 0:
            print("You are having no task todo..!!")
        else:
            print("You have todo tasks:")
            taskNo = 1
            for task in tasks:
                print(f"Task{taskNo} => [ Title : {task.title}\nDescription : {task.description}\nStatus : {task.status}\n]")
                taskNo += 1
        input("Press Enter key to continue...")
        
    def updateTask(self):
        global tasks
        if len(tasks) == 0:
            print("You are not having any task to update..!!")
        else:
            self.showTasks()
            isValidTaskNo = False
            while not isValidTaskNo:
                try:
                    updatedTaskNo = int(input("Choose the task no, you want to remove: "))
                    if updatedTaskNo <= 0 or updatedTaskNo > len(tasks):
                        raise IndexError("⚠️ You've entered a task no out of range, Please provide a valid task no: ")
                except IndexError as e:
                    print(e)
                    isValidTaskNo = False
                    continue
                except ValueError:
                    print("⚠️ Only integer values are allowed for task no..!")
                    isValidTaskNo = False
                    continue
                isValidTaskNo = True
            
            tasks[updatedTaskNo-1].title = input("Enter updated title: ")
            tasks[updatedTaskNo-1].description = input("Enter updated description: ")
            status = input("Enter updated status:('done' or 'not done' allowed only): ")
            while status not in ["done", "not done"]:
                print("⚠️ You have entered an invalid status string..!!")
                status = input("Enter updated status:('done' or 'not done' allowed only): ")
          
            tasks[updatedTaskNo-1].status = status
            print("Task updated successfully..!!")
        input("Press Enter key to continue...")
                    
    def markStatus(self):
        global tasks
        if len(tasks) == 0:
            print("Currently you are not having any task..!!")
        else:
            taskNo = 1
            for task in tasks:
                print(f"Task{taskNo} => Title : {task.title} - Status : {task.status}")
                taskNo += 1
                
            isValidTaskNo = False
            while not isValidTaskNo: 
                try:
                    statusTaskNo = int(input("Choose task no to update status: "))
                    if statusTaskNo <= 0 or statusTaskNo > len(tasks):
                        raise IndexError("⚠️ You've entered a task no out of range, Please provide a valid task no: ")
                except IndexError as e:
                    print(e)
                    isValidTaskNo = False
                    continue
                except ValueError:
                    print("⚠️ Only integer values are allowed for task no..!")
                    isValidTaskNo = False
                    continue
                isValidTaskNo = True
                
            status = input("Enter updated status:('done' or 'not done' allowed only): ")
            while status not in ["done", "not done"]:
                print("⚠️ You have entered an invalid status string..!!")
                status = input("Enter updated status:('done' or 'not done' allowed only): ")
         
            tasks[statusTaskNo] = status
            print("Status marked successfully..!!")
            input("Press Enter key to continue...")

        
              
if __name__ == "__main__":
    
    while True:
        print("\n","#"*30,sep='')
        print("What do you want to do..!")
        print("1. Add Todo Task")
        print("2. Remove Task")
        print("3. Update Existing Task")
        print("4. Show Your Tasks")
        print("5. Mark Status('done' or 'not done')")
        print("6. Exit The Program")

        try:
            option = int(input("Select the number: "))
        except ValueError:
            print("⚠️ Please provide integer values only..!!")
            continue
            
        task = Task()
        if option == 1:
            task.addTask()
            
        elif option == 2:
            task.removeTask()
            
        elif option == 3:
            task.updateTask()
            
        elif option == 4:
            task.showTasks()
        
        elif option == 5:
            task.markStatus()
            
        elif option == 6:
            import sys, time
            print("Exiting program",end="")
            for i in range(5):
                time.sleep(0.5)
                print(".",end="")
            sys.exit(0)
            
        else:
            print("⚠️ You have selected a wrong no..!!")
