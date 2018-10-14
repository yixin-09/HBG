# HBG
Herbgrind and Herbie

We have already collect the floating-point expressions
that output by Herbgrind runs on the 20 function.
Files store those expressions are named "High_level.fpcore", "Middle_level.fpcore" and "Low_level.fpcore".
We put those files in the root of directory "HBG".

You can run the following commend to using Herbie to improving those floating-point expressions:

$ ./HBG_herbie_test.sh

After few hours (more than 10 hours), results for each file are stored in three directories:
"graphsHigh", "graphsMiddle", "graphsLow", and you can open the file "report.html"
in each directory to view the results reported by Herbie.

Experimental results in our host machine are store in directory "resultsOfHBG".

Note: Due to the different random seed and the changes in newest Herbie,
the outputs of Herbie are not the same as we show in our paper,
while the slightly differece will not influence the conclusion in our paper.
