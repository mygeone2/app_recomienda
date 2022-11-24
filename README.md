## :sparkles: Helping community to choose school using ML :sparkles:

Recomienda Colegios is a web that determinate the probability to get accepted in certain schools making easier to order [SAE](https://www.sistemadeadmisionescolar.cl) applying list based on predicted acceptance probability. It scans tons of schools data to ingest a ML model described further. It model predicts your probability acceptance for nearest schools in your town. With this data, you can make a better applying list for SAE.


### What is the problem with SAE list?
SAE perform a excellent job selecting students for schools. It replaced a full-randomly method for selecting last year. With SAE each student a assures:
- Getting accepted in at least one school, not necessarily one of applied
- Higher probability to get accepted if some conditions are present
So nice, isnt? The problem begins when you don't 

## Usage
To run backend services:

```
docker-compose up
```
Several services will be running:
  - A postgres database server will be running in ``` 172.20.1.2:5432```
  - A Jupyter Notebook server will be running in ``` 172.20.1.3```
  - A NodeJS server will be running in ``` 172.20.1.4:80```. Endpoints will be describer further.
