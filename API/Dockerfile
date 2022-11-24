# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
#COPY ./app /code/app

# 
#COPY ./ML_model /code/ML_model

# 
CMD ["uvicorn", "app.main:app","--reload","--reload-include","*.py","--host", "0.0.0.0", "--port", "80"]
