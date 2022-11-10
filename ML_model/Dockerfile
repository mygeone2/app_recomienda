FROM devashishupadhyay/scikit-learn-docker
# Copy the current directory contents into the container at /app
COPY ds_ml.py /app/ds_ml.py
COPY summary.csv /app/summary.csv

# Set the working directory to /app
WORKDIR /app
ENTRYPOINT [ "python3", "ds_ml.py"]