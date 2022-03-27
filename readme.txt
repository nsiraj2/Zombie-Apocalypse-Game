Introduction:

The project is a playable game about a zombie apocalypse. As a player, you are a high school student where one of your professors has made a virus to test on a mouse. The mice bit one of the students and now the virus has spread to multiple students infecting each other in a chain reaction. Only you can save the school now from this virus.

The player will have 5 levels to clear before finishing the game and saving the school.
The player also must save the professor who has the cure to the virus.
The player starts the game with 3 lives. Every time a zombie bites the player, player loses a life.
The professor only has 1 life.

The Game starts with an option to choose a name for their character. Once a name is entered from your keyboard, the game resumes and enters level 1.

Level 1:
There’s an announcement in the school to stay in the classrooms, lock the doors. Students get to know about the pandemic in the school. Some of your mates have already been infected and are dangerous to be around. 
You are presented with 2 choices:
1.	Stay inside the classroom
2.	Go outside and gather non-infected students.

Player must type ‘1’ or ‘2’ from their keyboard into the console to select choice. Based on the player’s choice, the game carries on.
If the player selects 1, the player is instructed to find the professor by going out.
If the player selects 2, the player is instructed to remain outdoors and look for the professor.
Both choices lead the player to level 2.

Level 2:
The player is headed to the security room and encounters some infected students on the way.
The player is prompted with 2 choices again:
1.	Talk to the infected students.
2.	Dodge the infected students.

Player must type ‘1’ or ‘2’ from their keyboard into the console to select choice. Based on the player’s choice, the game carries on.
If the player selects 1, one of the zombies bites the player and the player dies (loses a life). After it’s death, if the player still has lives remaining, the player is presented to begin the level 2 again. If there are no lives remaining, the game exits and the player lose.
If the player selects 2, the player is instructed to open the security room door and look for the professor. This choice leads the player to level 3.


Level 3:
Player needs to locate the professor and help other students here. The security guards try to stop the player from entering security room, but the player over-powers them and enters the room. 
Now, the player is prompted with 2 choices:
1.	Find the professor and leave the security room with her.
2.	Use security room’s cameras to help move students to a safer place.

Player must type ‘1’ or ‘2’ from their keyboard into the console to select choice. Based on the player’s choice, the game carries on.
If the player selects 1, one of the zombies bites the professor and the professor dies (loses a life). As the professor has only 1 life, the game exits here and the player loses.
If the player selects 2, the player is instructed to create distraction which helps professor to get away from zombies. Player takes the mic and makes announce to create this distraction. Player asks professor to meet them in the science lab later. This choice leads the player to level 4.


Level 4:
Player is headed to science lab to meet the professor. Player is instructed not to kill the infected students on the way. While heading on its way, player is given 2 choices:
1.	Save their best friend Jane.
2.	Hide from zombies in a corner.

Player must type ‘1’ or ‘2’ from their keyboard into the console to select choice. Based on the player’s choice, the game carries on.
If the player selects 1, the player is instructed to take Jane with them to Science Lab. This choice leads the player to level 5.
If the player selects 2, zombies start looking for the player and find them. They bite the player, and the player dies (loses a life). After it’s death, if the player still has lives remaining, the player is presented to begin the level 4 again. If there are no lives remaining, the game exits and the player lose.

Level 5:
This is the final level of the game! Professor June has the formula for the cure but needs some time to develop it. Meanwhile, the pandemic has turned into an apocalypse. Professor manages to develop the cure. Now the cure needs to reach the infected students to eliminate the virus.
Player is prompted with the final 2 choices:
1.	Let a few zombies in the Science lab to test the cure on them.
2.	Spread the cure into the air vents of the school for a wider reach.
Player must type ‘1’ or ‘2’ from their keyboard into the console to select choice. Based on the player’s choice, the game carries on.
If the player selects 1, zombies over-power the player and a lot of them enter the Lab. The cure took time to start working, and the zombies inside kill the player. After it’s death, if the player still has lives remaining, the player is presented to begin the level 5 again. If there are no lives remaining, the game exits and the player lose.
If the player selects 2, the cure reached to every infected student. After some time, they start feeling better and the school is saved by the player. Player wins and the game finishes with a victory.

GitHub Link:
https://github.com/nsiraj2/Zombie-Apocalypse-Game

The code contains a python file named final_code_Numera.py.
The GitHub repository also contains a readme file to understand the overview and running steps for the project.

Languages:
The project is developed on python 3.9 kernel. The code is also compatible with python 36 and 3.7 versions.

Technologies:
•	VS Code: The code the be viewed/edited/run on a VS Code terminal with python 3 and above plug-ins.
•	Bash: The python file can also be run on a bash terminal.

Minimum System Requirements:
•	Modern Operating System:
•	Windows 7 or 10
•	Mac OS X 10.11 or higher, 64-bit
•	Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
•	x86 64-bit CPU (Intel / AMD architecture)
•	4 GB RAM

Supported Applications:
Python is often used as a support language for software developers, for build control and management, testing, and in many other ways.

Coding/Naming Conventions:
•	The file name consists of all small alphabets followed by the developer’s first name at the end.
•	The class name starts with a Capital letter.
•	The function names follow camel casing.
•	Object oriented coding principle is followed throughout the code with an object being created for every player. The objects have 2 properties – name and status of the player, which are assigned at the initialization.

Build Steps:
You don't need to compile a .py file to run it. Python is an interpreted language, and you can run the scripts directly, either using:
python final_code_Numera.py

Make sure to give executable permission to the .py file before running it using chmod.

Run Steps:
•	VS Code: The code run on a VS Code terminal with python 3 and above plug-ins. Just open the file in your Code editor and click “Run without Debugging” to directly start playing the game.
•	Bash: The python file can also be run on a bash terminal.
python final_code_Numera.py
Any other editor can also be used to run the code.

Overview of architecture:
The code contains a class “Player” which is assigned properties on object initialization. 
Each of the 5 levels of the game corresponds to 5 different functions, called sequentially to proceed the game. The following 5 functions are made:
•	level1()
•	level2()
•	level3()
•	level4()
•	level5()
Whenever the player is prompted with choices, an if-else condition handles the decision and calls below functions based on choices:
•	choice1()
•	choice2()
A global variable is made to track the lives remaining of each player. 

Start the program:
Use either the editor or bash command below to start running game in the terminal:
python final_code_Numera.py


