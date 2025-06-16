@echo off
opencv_traincascade -data classifier -vec positive.vec -bg negative.txt -numPos 450 -numNeg 200 -numStages 10 -w 20 -h 20 -featureType LBP
pause
