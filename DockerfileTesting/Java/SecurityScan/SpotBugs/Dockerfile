FROM openjdk:11
# Install SpotBugs
RUN wget https://github.com/spotbugs/spotbugs/releases/download/4.8.3/spotbugs-4.8.3.zip
RUN unzip spotbugs-4.8.3.zip -d /app
COPY mapwindow-1.0-SNAPSHOT.jar /app/spotbugs-4.8.3/lib
COPY run-spotbugs.bat .
CMD run-spotbugs.bat
