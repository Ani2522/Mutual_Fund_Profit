from fastapi import FastAPI, HTTPException, Query
from utils import calculate_profit

app = FastAPI()

@app.get("/profit")
def calculate_mutual_fund_profit(
    scheme_code: str=Query(...),
    start_date: str=Query(...),
    end_date: str=Query(...),
    capital: float=Query(1000000.0)
):
    try:
        profit = calculate_profit(scheme_code, start_date, end_date, capital)
        return {"net_profit": profit}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
