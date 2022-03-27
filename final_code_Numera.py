import random
class Player:
    lives = 3
    def __init__(self, name, status):
        self.name = name
        self.status = status
    def level1(self):
        print('Level1')
        print("Choose action:1.Stay in classroom,2.Go out of classroom")
        move=int(input())
        if move==1:
	        self.choice1()
        else:
	        self.choice2()
	    
    def choice1(self):
        self.studyinroomstudents()
        self.findProfessorJune()
        self.level2()
    def choice2(self):
        self.studyoutsideroomstudents()
        self.findProfessorJune()
        self.level2()
    def studyinroomstudents(self):
        print('Gathering in room students information')
    def studyoutsideroomstudents(self):
        print('Gathering outside classrooms')
    def findProfessorJune(self):
	    print('Professor June Found')
    def level2(self):
        print('Enter Level2')
        print('Player come across infected students')
        print('Want to talk with infected student?1.Yes,2.No')
        ch=int(input())
        if ch==1:
            print("Zombie pissed the player.Player dies")
            self.lives = self.lives - 1
            if self.lives == 0:
                print("All lives finished. You loose!!")
                exit()
            else:
                print("Lives Remaining: " + str(self.lives))
                self.level2()
        else:
            self.level3()
    def level3(self):
		    print("Enter Level3")
    def level3(self):
        print('Enter Level3')
        print('Player fights security guard')
        print('Player wants to use camera?1.No,2.Yes')
        ch=int(input())
        if ch==1:
            print("Professor dies by zombie attack")
            print("You loose!!")
            exit()
        else:
            print("Good work Player! You created distraction which helped professor get away from the zombies.")
            print("Player finds professor and asks him to meet in science lab.")
            self.level4()
    def level4(self):
        print("Enter level4")
        print("Player needs to head to Science Lab to meet the professor.")
        print("Reminder!! Don't kill the infected student as zombies can't seem to avoid getting in contact with them.")
        print("Chhose: \n1. Hide from infected Students. \n2. Save friend and move to science lab.")
        ch=int(input())
        if ch==1:
            print("Player saves his best friend Jane.")
            print("Player and Jane meets the Professor")
            self.level5()
        else:
            print("Player caught and dies.")
            self.lives = self.lives - 1
            if self.lives == 0:
                print("All lives finished. You loose!!")
                exit()
            else:
                print("Lives remaining: "+ str(self.lives))
                self.level4()    


    def level5(self):
        print("Enter level5")
        print("Well Done Player! Welcome to the final level")
        print("Player and Professor discussing the Treatment")
        print("Cure is developed but need to be tested")
        print("Chhose: \n1. Let Zombies In to test the cure on them. \n2. Spread the cure in air vents.")
        ch=int(input())
        if ch==2:
            print("Player and Jane spread the cure in air")
            print("Thank you Player! You have saved the school.")
            exit()
        else:
            print("Player give cure to two zombie but it affected late")
            print("zombie kill the player.")
            self.lives = self.lives - 1
            if self.lives == 0:
                print("All lives finished. You loose!!")
                exit()
            else:
                print("Lives remaining: "+ str(self.lives))
                self.level5()



if __name__ == "__main__":
	print("Enter the Name")
	name = input()
	p1= Player(name,1)
	students=[[random.randint(0,1),random.randint(0,1)] for i in range(100)]
	p1.level1()
	"""print("Choose action:1.Stay in classroom,2.Go out of classroom")
	move=int(input())
	if move==1:
	    p1.choice1()
	else:
	    p1.choice2()"""
	    
	
	
	