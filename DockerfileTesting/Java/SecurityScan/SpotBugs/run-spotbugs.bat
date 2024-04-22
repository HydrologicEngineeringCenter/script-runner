@echo off
set SPOTBUGS_HOME=app\spotbugs-4.8.3

rem Run SpotBugs with desired options
%SPOTBUGS_HOME%\bin\spotbugs -textui mapwindow-1.0-SNAPSHOT.jar > spotbugs-output.txt