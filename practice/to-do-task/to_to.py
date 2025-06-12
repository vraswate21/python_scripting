task = input("enter a task to add")

with open("todo.txt", "a") as f:
    f.write(task + "\n")


print( "task added")
