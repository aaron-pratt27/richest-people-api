from fastapi import FastAPI


app = FastAPI()

richest_people_list = {
    "Elon Musk": "280 Billion USD",
    "Jeff Bazos": "250 Billion USD",
    "Bill Gates": "190 Billion USD",
    "Mark Zukerberg" :"150 Billion USD",
}

# new endpoint
@app.get("/richest-people")
def richest_people():
    return richest_people_list
