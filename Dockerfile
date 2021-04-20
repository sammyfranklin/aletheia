FROM python:3.8.5

# Copy
WORKDIR /home
RUN apt-get update -y
RUN apt-get install -y octave octave-image octave-signal liboctave-dev imagemagick
COPY aletheialib aletheialib
COPY external external
COPY models models
COPY resources resources
COPY aletheia.py .
COPY effnetb0.py .
COPY server.py .
COPY setup.py .
COPY start.sh .
COPY requirements.txt .

# Build
RUN pip install --no-cache-dir -r requirements.txt
RUN make -C external/jpeg_toolbox
RUN make -C external/maxSRM

RUN mkdir uploads
ENV FLASK_APP=server.py
EXPOSE 5000

CMD ./start.sh
