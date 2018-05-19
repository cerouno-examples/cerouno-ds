#!/usr/bin/env python3

from faker import Faker
from sys import argv, exit
import csv


def data_row(gen):
    """Generate a row of fake data.

    Arguments
    ---------
    gen : faker.Faker
        A generator for fake data.

    Returns
    -------
    list
        A list with fake data.

    """
    return [
        gen.uuid4(),
        gen.date_this_year().isoformat(),
        gen.name().replace(",", " "),
        gen.phone_number(),
        gen.company_email(),
        gen.street_name().replace(",", " "),
        gen.city(),
        gen.postcode(),
        gen.state(),
        gen.random.randint(1e4, 1e7) / 100.0,
        gen.random.randint(1e3, 1e6) / 100.0
    ]


if __name__ == "__main__":
    if len(argv) != 2:
        print("Need exactly one argument, the number of records!")
        exit(1)

    nr = int(argv[1])
    batch = max(nr // 10000, 1)
    gen = Faker("es_MX")
    data = [data_row(gen) for i in range(nr // batch)]

    with open("retail_logs.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        [writer.writerows(data) for i in range(batch)]

    print("Wrote", nr, "records.")
