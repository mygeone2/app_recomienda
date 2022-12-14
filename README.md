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

# getProbability
This API allows users to retrieve the probability of being accepted into a particular school and level.

The API endpoint is /getProbability/{id_school}/{id_level}, and it expects two parameters:

id_school: an integer representing the ID of the school
id_level: an integer representing the ID of the level (e.g. high school)

The API returns a JSON object with a single key, probability, which represents the probability of being accepted into the specified school and level. If the probability cannot be calculated, the value of probability will be -1.

Example response:
```
{
    "probability": 0.75
}
```
The API uses the HTTP status code to indicate the success or failure of the request. A status code of 200 indicates success, while a status code of 404 indicates that the probability could not be calculated.

Example usage:

```
GET /getProbability/123/4

Response:
{
    "probability": 0.75
}
```
```
GET /getProbability/456/7

Response:
{
    "probability": -1
}
```
# getSimilarSchools
This API allows users to retrieve a list of similar schools to a specified school.

The API endpoint is /getSimilarSchools/{id_school}/{id_level}/{comuna}, and it expects three parameters:

id_school: an integer representing the ID of the school
id_level: an integer representing the ID of the level (e.g. high school)
comuna: an integer representing the ID of the comuna (i.e. district) in which the school is located

The API returns a JSON object with a single key, schools, which is an array of objects representing similar schools. Each school object contains the following keys:

id_school: an integer representing the ID of the school
name: a string representing the name of the school
street: strig representing the address of the school
probability: an float representing similarity between school requested and school in response

Example response:

```
{
    "schools": [
        {
            "rbd:' 123,
            "name": "School A",
            "street": "street A"
            "similarity" : 0.74
        },
        {
            "rbd:' 1234,
            "name": "School B",
            "street": "street B
            "similarity" : 0.89
        },
        ...
    ]
}
```
The API uses the HTTP status code to indicate the success or failure of the request. A status code of 200 indicates success, while a status code of 404 indicates that no similar schools could be found.

Example usage:
```
GET /getSimilarSchools/123/4/7

Response:
{
    "schools": [
        {
            "rbd:' 123,
            "name": "School A",
            "street": "street A"
            "similarity" : 0.74
        },
        {
            "rbd:' 1234,
            "name": "School B",
            "street": "street B
            "similarity" : 0.89
        },
        ...
    ]
}
```
```
GET /getSimilarSchools/123/7/9
Response
{
  "error": "id_colegio not found"
}
```
