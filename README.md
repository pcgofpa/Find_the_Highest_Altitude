<h1>1732. Find the Highest Altitude</h1>
<h2>Thought process</h2>
<ul>
    <li>n + 1 points at different altitudes</li>
    <li>Trip always starts at 0</li>
    <li>gain[i] = net change between i and i + 1</li>
    <li>Return highest altitude point.</li>
</ul>

Looking at the example the biker starts at point [0] goes to point at -5. 
[0:-5] = -5, [1:1] = -4, [2:5] = 1, [3:0] = 1, [4:-7] = -6
highest altitude = 1


<h2>Instructions</h2> 
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

<h3>Example 1:</h3>

Input: gain = [-5,1,5,0,-7]<br>
Output: 1<br>
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

<h3>Example 2:</h3>

Input: gain = [-4,-3,-2,-1,4,3,2]<br>
Output: 0<br>
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

<h3>Constraints:</h3>

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100