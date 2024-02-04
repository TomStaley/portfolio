This project was created for a unit in my Foundation Degree course. The goal of the unit (520CIT) was to create a program using Object Oriented Programming concepts.
We each came up with our own briefs to base our projects on. My brief was to create a door management system for Leamington college.


Detailed Brief:
At Leamington College, every room is protected by a keycard that only staff members can use. While this system is very secure, it can also be inconvenient for students, who need to wait for a staff member whenever they need to enter a room.
To solve this issue, this door management system expands who can access a certain room at a certain time. Users can book a room at a certain time and when a room is booked, all students in the class can access the room (but other students cannot). 
This maintains the security offered by the keycard locks (which prevents unauthorised access), while also being more convenient for students.
To facilitate this system, the program needs to do the following:
1. Manage student IDs, which includes adding new IDs and removing old IDs.
2. Manage classrooms, including adding/removing students to specific classrooms, and adding/removing classrooms themselves.
3. The user needs to be able to book a specific room at a specific time, for a specifc class.
4. All of the above data needs to be stored in an external file, which the keycards will use to grant or deny access.
5. Because I don't have access to the keycards, for security reasons, the program also needs to simulate how the keycards will use the data (demonstration mode).


Installation:
1. Download the entire folder to a location of your choice. Make sure to preserve the file structure.
2. Run 520cit - Tom Staley.exe to run the program.
3. The raw code is also included as 520cit - Tom Staley - code.py

Instructions:
1. Student Manager - this tab is used to manage Student IDs. You can add and remove student IDs into the list, where they can be used later.
2. Classroom Manager - along the left are the student IDs you entered above. On the right is the currently selected group. To select a group click "change group" and select from the list. Use the arrows to add/remove the selected IDs for the group.
3. Booking rooms - to book a room, first select the group you want to book, then click the open book symbol. Here you can input the classroom, along with the start/end times. NOTE: booking information is not displayed in the program itself.
4. DEMO mode - in demonstration mode, click "config". Enter the information as if you were a student trying to access a classroom, then confirm. Clicking "start" will display the result.