Project Introduction:

Hello !!
 Welcome to our application RWA(Routing Wavelenght Assignment).
As you know the general objective of the RWA problem is to maximize
the number of established connections.
Each connection request must be given a route and wavelength.
 The wavelength must be consistent for the entire path, 
unless the usage of wavelength converters is assumed.
 Two connections requests can share the same optical link, 
provided a different wavelength is used.
 Getting Started

These instructions will get you a copy of the project up and running 
on your local machine for development and testing purposes.

Prerequisites:

•if you want develop or test the code we invite you to install Anaconda 
on Windows. You find in this following link explicated details:
https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/

How to interact with our GUI:

The zip folder contains everything you need,
We advise you to read these following steps carefully:
•	To start you must input three matrices : 
•	A is the matrix of the graph
•	B is the matrix of the connection requests
•	X is the matrix of Time

•	To input a matrix you must open the excel file and modify the matrix:
 
-	To add matrix A 
            -put 1 if you have a path between two edges and 0 otherwise.
-	To add matrix B 
            -each line contains a connection request,
             1 on aij means that we want a connection between i and j and 0 otherwise.
-	To add matrix X
            -each line time for a connection request,in evrey line we have two 1,
             which forms a time segment, starting with the first 1 until the second, 
             for example if we have in the first line of the matrix X (1 0 0 1 0) 
             it means the time of the first request is from 0 to 3 it means 3 second.

When you run the code press START and a new window appears in which:
you should enter :
•	The algorithm’s choice
•	The number of colors
•	The number of MaxIterations
•	The number o k-shortest path if you choose k-shortest path algorithm


Then clik in the start button to start 
.If everything is going well a message is displayed to you.
After you need just to click in these button to visualize in new window:
-The origin graph
-The time graph
-The generated paths
-The optimize solution of the problem
 

Finally,thank you for choosing our application and we hope that you enjoy with using it!
