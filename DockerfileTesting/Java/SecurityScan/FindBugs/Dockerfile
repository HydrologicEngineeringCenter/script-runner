FROM lokori/findbugs-sec
WORKDIR /app

COPY dockerTest.java .

# Run FindBugs with desired arguments (refer to image documentation)
RUN findbugs dockerTest.java 
