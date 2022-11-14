FROM devashishupadhyay/scikit-learn-docker as ml_model
COPY ds_ml.py /app/ds_ml.py 
COPY summary.csv /app/summary.csv
WORKDIR /app
ENTRYPOINT [ "python3", "ds_ml.py"]

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as fastapi

# COPY ./app /app
# COPY --from=ml_model /app/ /app/ml_model
