student_data = {}

while True:
    print("1. Add student data")
    print("2. Read Data")
    print("3. Update data")
    print("4. Delete data")

    choose = input("Enter data from 1-4: ")

# ---------------- ADD DATA ----------------

    if choose == "1":

        n = int(input("Enter number of students: "))

        f = open("practicestdata.txt","a")

        for i in range(n):
            print("Student", i+1)

            Name = input("Enter student name: ")
            Class = input("Enter student class: ")
            Roll_no = input("Enter student Roll No: ")

            f.write(Name + "," + Class + "," + Roll_no + "\n")

        f.close()
        print("Student data added successfully")


# ---------------- READ DATA ----------------

    elif choose == "2":

        f = open("practicestdata.txt","r")

        data = f.readlines()

        if data:
            for line in data:

                Name, Class, Roll_no = line.strip().split(",")

                print("Name:", Name)
                print("Class:", Class)
                print("Roll No:", Roll_no)
                print()

        else:
            print("No data found")

        f.close()


# ---------------- UPDATE DATA ----------------

    elif choose == "3":

        Name = input("Enter name to update: ")
        new_class = input("Enter new class: ")

        f = open("practicestdata.txt","r")
        lines = f.readlines()
        f.close()

        f = open("practicestdata.txt","w")

        found = False

        for line in lines:

            if line.startswith(Name + ","):
                parts = line.strip().split(",")
                line = parts[0] + "," + new_class + "," + parts[2] + "\n"
                found = True

            f.write(line)

        f.close()

        if found:
            print("Data updated successfully")
        else:
            print("Data not found")


# ---------------- DELETE DATA ----------------

    elif choose == "4":

        Name = input("Enter name to delete: ")

        f = open("practicestdata.txt","r")
        lines = f.readlines()
        f.close()

        f = open("practicestdata.txt","w")

        found = False

        for line in lines:

            if line.startswith(Name + ","):
                found = True
            else:
                f.write(line)

        f.close()

        if found:
            print("Data removed successfully")
        else:
            print("Data not found")