[![Build Status](https://travis-ci.org/netoxico/nqueens.svg?branch=master)](https://travis-ci.org/netoxico/nqueens)
# nqueens

Set required environment variables in a `.env` file

```
DATABASE_URL=postgres://nqueen:nqueen@postgres:5432/nqueen
POSTGRES_PASSWORD=postgres
```

Build docker images

```.bash
docker-compose up --build
```

nqueens cli
```
Usage: nqueens.py [OPTIONS]

Options:
  --n INTEGER  Number of queens.
  --save       Save results to database.
  --help       Show this message and exit.
```

Execute nqueens for n = 8
```.bash
docker-compose exec app python nqueens.py --n 8
```

Execuote nqueen and store each result in postgres
```.bash
docker-compose exec app python nqueens.py --n 8 --save
```

Run tests
```
docker-compose exec app pytest
```