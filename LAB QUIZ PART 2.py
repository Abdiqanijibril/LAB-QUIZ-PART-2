class Binusmaya:
    def __init__(self):
        self.lect = [{'name': 'Jude', 'subject': 'Algprog', 'lecturerID': 1234}]
        self.classes = ['L1AC', 'L1AB']
        self.schedules = ()

    def add_lecturer (self, name, subject, lecturerID):
        for lecturer in self.lect:
            if  lecturer['LecturerID'] == lecturerID:
                print ("Lecturer info already exists Please create a new one")
                return False
            elif lecturer['subject'] == subject:
                print ("Subject already exists Please create a new one")
                return False
            elif lecturer['name'] == name:
                print ("Name already exists Please create a new one")
                return False
    
        new_lecturer = {'name':name, 'subject':subject, 'lecturerID':lecturerID}
        self.lect.append(new_lecturer)
        return True

    def remove_lecturer (self, lecturerID):
        for lecturer in self.lect:
            if  lecturer['lecturerID'] == lecturerID:
                self.lect.remove(lecturer)
                return True
        print ("Lecturer not found")
        return False

    def add_class (self, class_name):
        if class_name in self.classes:
            print ("Class already exists")
            return False
        self.classes.append(class_name)
        return True

    def remove_class (self, class_name):
        if class_name in self.classes:
            self.classes.remove(class_name)
            return True
        print ("Class not found")
        return False

    def add_schedule (self, class_name, time, subject):
        for class_schedule in self.schedules:
            if  class_schedule[0] == class_name and class_schedule[2] == subject:
                print ("Schedule already exists for this class and subject")
                return False
        new_schedule = (class_name, time, subject)
        self.schedules += (new_schedule,)
        return True
    
Info = Binusmaya()

print("Lucture Info")
print(f"Name: {Info.lect[0]['name']}")
print (f'subject: {Info.lect[0]['subject']}')
print (f'Lecturer ID: {Info.lect[0]['lecturerID']}')


print("\nClass Schedule")
for class_name in Info.classes:
    print(class_name)
    
print ("\nSchedule")
print (Info.schedules)