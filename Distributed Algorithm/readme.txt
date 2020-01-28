HOW TO EXECUTE THE PROGRAM
	The program is written in python3, so install python3 and then simply double tap
	or
	add python to path(default in mac and linux) use cmd(terminal) to run

HOW THE ALGORITHM IS WRITTEN AND COMPROMIZATIONS
	- Processes call other processes' functions as a form of sending messages
	- We assume the timestamps are corrected using lamports algorithm which is a prerequisite for distributed algorithm for distributed mutual exclusion
	- Since this is only a single computer and might produce same timestamps precautions have been made to make all the processes create different timestamps
	- The time processes request for critical region is randomized to create the same effect processes under distributed system create
	- critical region uses atleast 7 seconds to clearly show how it'll send the "OK" message to requesting processes

HOW THE DISPLAY SHOWS CLEARLY THE ONGOING PROCESS WAITS AND CURRENT RUNNING STATUS
	- Different processes have been shown in this form
	- CR stands for critical region
-----------------------------------------------------------------------------------------
|   Process1     |     Process2     |    Process3     |        Process4                 |
|                |                  |                 |                                 |
|  under requst  |                  |                 |                                 |
|                |   under CR       |                 |                                 |
|                |   left CR        |                 |                                 |
|  underCR	     |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
|                |                  |                 |                                 |
-----------------------------------------------------------------------------------------
and more are displayed like this.... 
	- It shows what the processes are going through as they are going through it... 
	- So its advisable to Signal (ctrl+c) the process and see what has happend in the time line
