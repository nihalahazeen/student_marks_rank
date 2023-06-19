from fastapi import APIRouter

from src.database.database import *
from src.models.student import *

router = APIRouter()

@router.get("/", response_description="Students rank retrieved", response_model=Response)
async def get_rank():
    rank = await calculate_rank()
    i = 1
    for item in rank[0]['students']:
        item['rank'] = i
        i+=1
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Rank list retrieved successfully",
        "data": rank[0]['students']
    }
