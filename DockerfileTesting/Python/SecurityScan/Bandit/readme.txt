clean.py is a python script that shouldn't produce any errors from the Bandit scan.
dirty.py has several issues that Bandit should catch.
dirty.txt is an example of the output file created by the Bandit scan.
Dockerfile_distroless builds but it throws errors when trying to run. I think that is because the distroless image doesn't know how to run the python file.