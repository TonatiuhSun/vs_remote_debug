from typing import Type
import json

import uvicorn

from fastapi import FastAPI, status, Body


app = FastAPI()


@app.get('/health', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    return {'healthcheck': 'Everything OK!'}


@app.post('/run', status_code=status.HTTP_200_OK)
# TODO add template to body parameters
def run_churn_prediction_pipeline(
        payload: dict = Body(...),
        bucket_name: str = "nextiva-tensorflow",
        location: str = "churn_data/churn_sample1.csv"
):
    print(payload)
    return payload 


if __name__ == '__main__':
    uvicorn.run("src.web.app:app",  host="0.0.0.0", reload=True)