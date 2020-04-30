import random

class Cleaner:
    def __init__(self):
        self.member_l = ["정민", "동수", "어진", "용순", "강혁", "민희", "지우", "민지"]
        self.clean_member_l = []
        self.selected_person = None
        self.iter_num = len(self.member_l)
        

    def select_person(self):
        self.selected_person = random.choice(self.member_l)

    def remove_list(self):
        self.member_l.remove(self.selected_person)

    def append_list(self):
        self.clean_member_l.append(self.selected_person)

    def iter_operation(self):
        for i in range(self.iter_num):
            self.select_person()
            self.remove_list()
            self.append_list()

if __name__== "__main__":
    random.seed(11)
    cleaner = Cleaner()
    cleaner.iter_operation()
    print(cleaner.clean_member_l)

        
    
