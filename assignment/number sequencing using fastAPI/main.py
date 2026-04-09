from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class Number(BaseModel):
    number: int

class Range(BaseModel):
    start: int
    end: int

@app.get("/")
def home():
    return {"message": "Number sequencing server running"}

@app.post("/factorial")
def factorial(data: Number):
    num = data.number
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return {"result": fact}

@app.post("/fibonacci")
def fibonacci(data: Number):
    n = data.number
    a, b = 0, 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return {"result": series}

@app.post("/odd_even")
def odd_even(data: Number):
    num = data.number

    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    return {"result": result}

@app.post("/armstrong")
def armstrong(data: Number):
    num = data.number

    digits = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == num:
        result = "Armstrong Number"

    else: 
        result = "Not an Armstrong number"

    return {"result": result}

@app.post("/prime_series")
def prime_series(data: Range):
    start = data.start
    end = data.end
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    
    return {"result": primes}