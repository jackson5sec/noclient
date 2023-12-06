# Use a base Linux image with Python 2.x and 32-bit compatibility libraries
FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python2 \
    lib32z1 \
    git \
    && ln -s /usr/bin/python2.7 /usr/bin/python

# Set the working directory
WORKDIR /opt

# Clone EQGRP repository from GitHub
RUN git clone https://github.com/jackson5sec/noclient

# Add EQGRP/Linux/bin folder to the PATH environment variable
ENV PATH="/opt/noclient/util:${PATH}"

# Copy the scanner binary to the proper location
RUN cp /opt/noclient/util/scanner /usr/local/bin/scanner

# Set the entry point
ENTRYPOINT ["/bin/bash"]