from os import environ
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Result


def _create_session():
    db_url = environ.get("DATABASE_URL")

    if not db_url:
        raise EnvironmentError('Need to set a Postgres DATABASE_URL')

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


def nqueens(r, n, p, save=False):
    s = len(p)
    cols = range(s)
    valid = s == len(set(p[i] + i for i in cols)) == len(set(p[i] - i for i in cols))

    count = 0

    if valid:
        if r == n:
            if save:
                session.add(Result(n=n, result=p))
            print(p)
            return 1

        for c in set(range(n)) - set(p):
            count += nqueens(r + 1, n, p + [c], save=save)

    if save:
        session.commit()
    return count


@click.command()
@click.option("--n", default=1, help="Number of queens.")
@click.option("--save", is_flag=True, help="Save results to database.")
def queens(n, save):
    print("Calculated: {} results".format(nqueens(0, n, [], save)))


if __name__ == "__main__":
    queens()
