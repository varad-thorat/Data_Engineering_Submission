import sys

class Person:
    def __init__(self, name:str, gender:str ):
        self.name = name
        self.gender = gender
        self.spouse = None
        self.mother = None
        self.father = None
        self.children = []

class FamilyTree:
    def __init__(self):
        self.members = {}
        self.root = None

    def add_member(self, person:Person):
        self.members[person.name] = person

    def initialize(self):
        #Created Arthur and Margaret and added them
        Arthur = Person("Arthur","Male")
        Margaret = Person("Margaret","Female")
        Arthur.spouse = Margaret
        Margaret.spouse = Arthur
        self.add_member(Arthur)
        self.add_member(Margaret)
        #Set Arthur as root
        self.root = Arthur
        #Set Bill
        Bill = Person("Bill","Male")
        self._add_child(Margaret,Arthur,Bill)
        
        #Set Flora
        Flora = Person("Flora","Female")
        self.add_member(Flora)
        Flora.spouse = Bill
        Bill.spouse=Flora

        #Set Charlie,Percy,Ronald,Ginerva
        Charlie = Person("Charlie","Male")
       
        Percy = Person("Percy","Male")
       
        Ronald = Person("Ronald","Male")
       
        Ginerva = Person("Ginerva","Female")
       

        #Set Aurdrey as wife of Percy
        Audrey = Person("Audrey","Female")
        Audrey.spouse = Percy
        Percy.spouse = Audrey
        self.add_member(Audrey)
        #Set Children of Audrey and Percy
        Molly = Person("Molly","Female")
        Lucy = Person("Lucy","Female")
        self._add_child(Audrey,Percy,Molly)
        self._add_child(Audrey,Percy,Lucy)

        #Set Helen as wife Ronald
        Helen = Person("Helen","Female")
        self.add_member(Helen)
        Helen.spouse = Ronald
        Ronald.spouse = Helen
        #Set Rose and Hugo as Child
        Rose = Person("Rose","Female")
        Hugo = Person("Hugo","Male")
        self._add_child(Helen,Ronald,Rose)
        self._add_child(Helen,Ronald,Hugo)
        #Set Malfoy as husband of Rose
        Malfoy = Person("Malfoy","Male")
        Malfoy.spouse = Rose
        Rose.spouse = Malfoy
        self.add_member(Malfoy)
        #Set Draco and Aster as child
        Draco = Person("Draco","Male")
        Aster = Person("Aster","Female")
        self._add_child(Rose,Malfoy,Draco)
        self._add_child(Rose,Malfoy,Aster)

        

        #Set Harry as husband of Ginerva
        Harry = Person("Harry","Male")
        self.add_member(Harry)
        Harry.spouse = Ginerva
        Ginerva.spouse = Harry
        #Set James , Albus,Lily as child
        James = Person("James","Male")
        Albus = Person("Albus","Male")
        Lily = Person("Lily","Female")
        self._add_child(Ginerva,Harry,James)
        self._add_child(Ginerva,Harry,Albus)
        self._add_child(Ginerva,Harry,Lily)
        #Set Darcy as wife of James
        Darcy = Person("Darcy","Female")
        Darcy.spouse = James
        James.spouse = Darcy
        self.add_member(Darcy)
        #Set William as child
        William = Person("William","Male")
        self._add_child(Darcy,James,William)
        #Set alice as wife of albus
        Alice = Person("Alice","Female")
        self.add_member(Alice)
        Alice.spouse = Albus
        Albus.spouse = Alice
        #Set Ron and Ginny as children
        Ron = Person("Ron","Male")
        Ginny = Person("Ginny","Female")
        self._add_child(Alice,Albus,Ron)
        self._add_child(Alice,Albus,Ginny)
        
        
        

        #Set Victoire,Dominique and Louis as child
        Victoire = Person("Victoire","Female")
       
        Dominique = Person("Dominique","Female")
        
        Louis = Person("Louis","Male")
        
        self._add_child(Flora,Bill,Victoire)
        self._add_child(Flora,Bill,Dominique)
        self._add_child(Flora,Bill,Louis)

        #Set Ted as husband of Victoire
        Ted = Person("Ted","Male")
        self.add_member(Ted)
        Ted.spouse = Victoire
        Victoire.spouse = Ted

        #Set Remus as child of Victoire
        Remus = Person("Remus","Male")
        self._add_child(Victoire,Ted,Remus)

        self._add_child(Margaret, Arthur, Charlie)
        self._add_child(Margaret, Arthur, Percy)
        self._add_child(Margaret, Arthur, Ronald)
        self._add_child(Margaret, Arthur, Ginerva)
        
    def _add_child(self,mother:Person,father:Person,child:Person):
        child.father = father
        child.mother = mother
        mother.children.append(child)
        father.children.append(child)
        self.add_member(child) 
    
    def add_child(self,mother:str,child_name:str,gender:str):
        mother = self.members.get(mother)
        if mother is not None:
            if mother.gender == 'Female':
                if mother.spouse is not None:
                    child = Person(child_name,gender)
                    self._add_child(mother,mother.spouse,child)
                    print("CHILD_ADDED")
                else:
                    print("CHILD_ADDITION_FAILED")
            else:
                print("CHILD_ADDITION_FAILED")
        else:   
            print("PERSON_NOT_FOUND")
        
    def siblings(self,person:Person):
        if person.mother is None:
            print("NONE")
            return
        else:
            siblings = [child.name for child in person.mother.children if child != person]
            if not siblings:
                print("NONE")
            else:
                print(" ".join(siblings))

    def son(self,person:Person):
        if not person.children:
            print("NONE")
            return
        else:
            sons = [son.name for son in person.children if son.gender=="Male"]
            print(" ".join(sons))
            
    def daughter(self,person:Person):
        if not person.children:
            print("NONE")
            return
        else: 
            daughters = [daughter.name for daughter in person.children if daughter.gender=="Female"]
            print(" ".join(daughters))
    
    def maternal_aunt(self,person:Person):
        if person.mother is None or person.mother.mother is None: #(here we have used or because if and was there then python would crash if person.mother was none to evaludate person.mother.mother)
            print("NONE")
            return
        else:
            maternal_aunt = [m_aunt.name for m_aunt in person.mother.mother.children if m_aunt.gender =="Female" and m_aunt!=person.mother]
            if not maternal_aunt:
                print("None")
                return
            else:
                print(" ".join(maternal_aunt))

    def paternal_aunt(self,person:Person):
        if person.father is None or person.father.mother is None: #(here we have used or because if and was there then python would crash if person.mother was none to evaludate person.mother.mother)
            print("NONE")
            return
        else:
            paternal_aunt = [p_aunt.name for p_aunt in person.father.mother.children if p_aunt.gender =="Female" and p_aunt!=person.father]
            if not paternal_aunt:
                print("None")
                return
            else:
                print(" ".join(paternal_aunt))

    def maternal_uncle(self,person:Person):
        if person.mother is None or person.mother.mother is None: #(here we have used or because if and was there then python would crash if person.mother was none to evaludate person.mother.mother)
            print("NONE")
            return
        else:
            maternal_uncle = [m_uncle.name for m_uncle in person.mother.mother.children if m_uncle.gender =="Male" and m_uncle!=person.mother]
            if not maternal_uncle:
                print("None")
                return
            else:
                print(" ".join(maternal_uncle))

    def paternal_uncle(self,person:Person):
        if person.father is None or person.father.mother is None: #(here we have used or because if and was there then python would crash if person.mother was none to evaludate person.mother.mother)
            print("NONE")
            return
        else:
            paternal_uncle = [p_uncle.name for p_uncle in person.father.mother.children if p_uncle.gender =="Male" and p_uncle!=person.father]
            if not paternal_uncle:
                print("None")
                return
            else:
                print(" ".join(paternal_uncle))
                
    def sister_in_law(self, person: Person):
        sil = []  # always start empty
        
        # Part 1: spouse's sisters (only if spouse exists)
        if person.spouse and person.spouse.mother:
            sil += [s.name for s in person.spouse.mother.children 
                    if s.gender == "Female" and s != person.spouse]
        
        # Part 2: male siblings' wives (only if mother exists)
        if person.mother:
            for sib in person.mother.children:
                if sib.gender == "Male" and sib != person and sib.spouse is not None:
                    sil.append(sib.spouse.name)
        
        if not sil:
            print("NONE")
        else:
            print(" ".join(sil))


    def brother_in_law(self, person: Person):
        bil = []  # always start empty
        
        # Part 1: spouse's sisters (only if spouse exists)
        if person.spouse and person.spouse.mother:
            bil += [s.name for s in person.spouse.mother.children 
                    if s.gender == "Male" and s != person.spouse]
        
        # Part 2: male siblings' wives (only if mother exists)
        if person.mother:
            for sib in person.mother.children:
                if sib.gender == "Female" and sib != person and sib.spouse is not None:
                    bil.append(sib.spouse.name)
        
        if not bil:
            print("NONE")
        else:
            print(" ".join(bil))

    def get_relationship(self,person:str,relationship:str):
        person = self.members.get(person)
        if person is not None:
            if relationship == "Siblings":
                self.siblings(person)
            elif relationship == "Son":
                self.son(person)
            elif relationship == "Daughter":
                self.daughter(person)
            elif relationship == "Maternal-Aunt":
                self.maternal_aunt(person)
            elif relationship == "Paternal-Aunt":
                self.paternal_aunt(person)
            elif relationship == "Maternal-Uncle":
                self.maternal_uncle(person)
            elif relationship == "Paternal-Uncle":
                self.paternal_uncle(person)
            elif relationship == "Sister-In-Law":
                self.sister_in_law(person)
            elif relationship == "Brother-In-Law":
                self.brother_in_law(person)
        else:
            print("PERSON_NOT_FOUND")
    

def process_file(filename:str, tree:FamilyTree):

    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            if len(parts) > 2 :
                if parts[0] == "ADD_CHILD":
                    mother = parts[1]
                    child_name = parts[2]
                    gender = parts[3]
                    tree.add_child(mother,child_name,gender)
                
                elif parts[0] == "GET_RELATIONSHIP":
                    person = parts[1]
                    relationship = parts[2]
                    tree.get_relationship(person,relationship)
                else:
                    print("WRONG DETAILS")
        
        
if __name__ == "__main__":
    filename = sys.argv[1]
    tree = FamilyTree()
    tree.initialize()
    process_file(filename,tree)
    
    