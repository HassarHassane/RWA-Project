## Project title
This project comes within the context of the course Programming Paradigms & Python Algorithms. I collaborated with my classmates to realize it. We chose as title of our project 'RWA-Python'.

## Introduction
<p> Welcome to our application RWA(Routing Wavelenght Assignment). As you know the general objective of the RWA problem is to maximize
the number of established connections. Each connection request must be given a route and wavelength. The wavelength must be consistent for the entire path, unless the usage of wavelength converters is assumed. Two connections requests can share the same optical link, provided a different wavelength is used.
</p>

## Getting started
<p>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
</p>

## Prerequisities
<p>
If you want develop or test the code we invite you to install Anaconda on Windows. You find in this following link explicated details:
</p>
<ul>
<li>
https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/
</li>
</ul>

## How to interact with the GUI
<p>The zip folder contains everything you need, we advise you to read these following steps carefully:
</p>
<ul>
<th>
To start you must input three matrices : 
</th>
<li>
A is the matrix of the graph
</li>
  <li>
B is the matrix of the connection requests
    </li>
<li>
X is the matrix of Time
</li>
</ul>
<ul>
<th>
To input a matrix you must open the excel file and modify the matrix:
</th>
<li>
To add matrix A: 
Put 1 if you have a path between two edges and 0 otherwise.
</li>
  <li>
To add matrix B 
Each line contains a connection request, 1 on aij means that we want a connection between i and j and 0 otherwise.

</li>
<li>
To add matrix X
Each line time for a connection request, in evrey line we have two 1,
which forms a time segment, starting with the first 1 until the second, 
for example if we have in the first line of the matrix X (1 0 0 1 0) 
it means the time of the first request is from 0 to 3 it means 3 second.
</li>
</ul>
<p>When you run the code press START and a new window appears in which:
you should enter :</p>
<ul>
<li>
The algorithm’s choice
</li>
<li>
The number of colors
</li>
<li>
The number of MaxIterations
</li>
<li>
The number of k-shortest path if you choose k-shortest path algorithm
</li>
</ul>
<p>
Then clik in the start button to start. If everything is going well a message is displayed to you.
After you need just to click in these button to visualize in new window:
</p>
<ul>
<li>The origin graph</li>
<li>The time graph</li>
<li>The generated paths</li>
<li>The optimize solution of the problem</li>
</ul>

## acknowledgement
<p>Finally, thank you for choosing our application!</p>
