from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint that confirms the API is running."""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers together.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    JSON object containing the operation and result.
    """
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": a + b
    }


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: float, b: float):
    """
    Subtract the second number from the first.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    JSON object containing the operation and result.
    """
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": a - b
    }


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: float, b: float):
    """
    Multiply two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    JSON object containing the operation and result.
    """
    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": a * b
    }


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: float, b: float):
    """
    Divide the first number by the second.

    Parameters:
    a (float): Numerator
    b (float): Denominator

    Returns:
    JSON object containing the operation and result.

    Raises:
    422 error if division by zero occurs.
    """
    if b == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Division by zero is not allowed. Please provide a non-zero value for b."
        )

    return {
        "operation": "divide",
        "a": a,
        "b": b,
        "result": a / b
    }

@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: float, b: float, c: float):
    """
    Calculate the average of three numbers.

    Parameters:
    a (float): First number
    b (float): Second number
    c (float): Third number

    Returns:
    JSON object containing the average result.
    """
    result = (a + b + c) / 3

    return {
        "operation": "average",
        "a": a,
        "b": b,
        "c": c,
        "result": result
    }


@app.get("/percentage/{part}/{whole}", status_code=200)
def percentage(part: float, whole: float):
    """
    Calculate what percentage a number is of another number.

    Parameters:
    part (float): Portion value
    whole (float): Total value

    Returns:
    JSON object containing the percentage result.

    Raises:
    422 error if the whole value is zero.
    """
    if whole == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The whole value cannot be zero when calculating a percentage."
        )

    result = (part / whole) * 100

    return {
        "operation": "percentage",
        "part": part,
        "whole": whole,
        "result": result
    }


@app.get("/power/{base}/{exponent}", status_code=200)
def power(base: float, exponent: float):
    """
    Raise a number to a given power.

    Parameters:
    base (float): Base number
    exponent (float): Exponent value

    Returns:
    JSON object containing the calculated power.
    """
    result = base ** exponent

    return {
        "operation": "power",
        "base": base,
        "exponent": exponent,
        "result": result
    }