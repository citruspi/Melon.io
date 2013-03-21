<<<<<<< HEAD
## Introduction

Melon.io provides an interface to retrieve information like:

- weather
- theater and movie locations
- translations
- etc.

from existing services.

## Usage

    import json
    from melonio import melonio

    response = json.loads(melonio.solve(query))

    if response['success']:

        print response['response']

    else:

        print response['error']

## Config

Some API's require API keys which should be defined in `config.py`. Simply fill out and rename the `sample-config.py` file included.

## Syntax

As of this point, the syntax for a query is formatted as such:

    service:options:input

Some samples queries and service definitions can be found below.

## Services

### Weather

_Weather data provided by [Weather Underground]()._

#### Current Weather

| | |
|:-----------|:------------|
| Options|None|
| Query Format:|`weather::zip code`|
| Sample Query |`weather::07726`|
| Sample `response` | Location: 07726 Condition: Overcast Temperature: 35.2 F (1.8 C) Feels Like: 35 F (2 C) Wind: Calm Humidity: 64% |
=======
