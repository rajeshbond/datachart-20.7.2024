import pandas as pd
from fastapi import Response, status, HTTPException, Depends, APIRouter , BackgroundTasks
from ..import schemas


router = APIRouter(
    prefix= '/fetchdata',
     tags=["Screener Data"]
)


@router.post("/api/fetchdata", status_code=status.HTTP_200_OK,response_model=list[schemas.DataFetchout])
def fetchdata(condition: schemas.DataFetch):
    try:
        # print(condition.conditionName)
        file_name = f"result_{condition.conditionName}.csv"
        print(file_name)
        data = pd.read_csv(file_name)
        result =  data.to_dict(orient='records')
        # print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Data Fetched Successfully"}