from pathlib import Path
import os

def fileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")


def createfile():
    try:
        fileandfolder()
        name = input("Enter file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter content: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")

    except Exception as err:
        print(f"Error: {err}")


def readfile():
    try:
        fileandfolder()
        name = input("Enter file to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("\nFile Content:\n", data)
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")


def updatefile():
    try:
        fileandfolder()
        name = input("Enter file to update: ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("1: Rename file")
            print("2: Overwrite file")
            print("3: Append data")

            res = input("Enter choice: ")

            if res == "1":
                new_name = input("Enter new name: ")
                p.rename(Path(new_name))
                print("File renamed")

            elif res == "2":
                with open(p, 'w') as fs:
                    data = input("Enter new content: ")
                    fs.write(data)
                print("File overwritten")

            elif res == "3":
                with open(p, 'a') as fs:
                    data = input("Enter data to append: ")
                    fs.write(" " + data)
                print("Data appended")

            else:
                print("Invalid choice")

        else:
            print("File not found")

    except Exception as err:
        print(f"Error: {err}")


def deletefile():
    try:
        fileandfolder()
        name = input("Enter file to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted")
        else:
            print("File not found")

    except Exception as err:
        print(f"Error: {err}")


print("1: Create file")
print("2: Read file")
print("3: Update file")
print("4: Delete file")

check = input("Enter choice: ")

if check == "1":
    createfile()
elif check == "2":
    readfile()
elif check == "3":
    updatefile()
elif check == "4":
    deletefile()
else:
    print("Invalid input")