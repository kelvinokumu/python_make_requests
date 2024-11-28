from fastapi import FastAPI
import requests

app = FastAPI()

REST_COUNTRIES_URL = "https://restcountries.com/v3.1/all"

@app.get("/")
def read_root():
    return {"message": "This is the root page / Endpoint"}

@app.get("/countries")
def get_countries():
    try:
        response = requests.get(REST_COUNTRIES_URL)
        response.raise_for_status()
        countries = response.json()
        
        result = [{"name":c["name"]["common"],
                   "region":c.get("region","uknown")} for c in countries]
        
        
        return {"Country name and Region": result}
            
    except requests.exceptions.RequestException as e:
        return {"Error ": str(e)}
        
        
@app.get("/countries/{name}")
def get_countries_by_name(name:str):
    try:
        url = f"https://restcountries.com/v3.1/name/{name}"
        response = requests.get(url)
        response.raise_for_status()
        country = response.json()[0]
        
        result = {"name":country["name"]["common"],
                   "region":country.get("region","uknown")}
        
        
        # return {"Country name and Region": result}
        return result
            
    except requests.exceptions.RequestException as e:
        return {"Error ": str(e)}
    
    