FROM debian

WORKDIR /app
RUN apt-get update && apt-get install -y jython

# Copy your Jython script (optional)
COPY hello_world.jy .

# Define command to run Jython
CMD ["jython", "hello_world.jy"] 