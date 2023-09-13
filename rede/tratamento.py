FILES_PREFIXS = [
    "osu_allgather",
    "osu_alltoall",
    "osu_alltoallv",
    "osu_barrier",
    "osu_bcast",
    "osu_gather",
    "osu_multi_lat",
    "osu_scatter"
]

FILES_BATTERIES = [
    4, 8, 12, 16, 20, 24, 28, 32,
]

CSV_PATH = "csvs"

NUM_ROUNDS = 5


def get_values(lines: list[str]) -> list[str]:
    values: list[str] = []

    for i in lines[2:]:
        i = i.replace("\n", "")
        i = i.split()

        values.append(i[1])

    return values


def get_header(lines: list[str]) -> list[str]:
    header: list[str] = []

    for i in lines[2:]:
        i = i.replace("\n", "")
        i = i.split()

        header.append(i[0])

    return header


for i in FILES_PREFIXS:
    for j in FILES_BATTERIES:
        csv_filename = f"{i}_{j}.csv"

        base_filename = f"{i}_{j}._"

        csv = open(CSV_PATH + "/" + csv_filename, "w")

        file = open(base_filename + "1.txt")

        header = get_header(file.readlines())

        csv.write(",".join(header)+"\n")

        file.close()

        for k in range(NUM_ROUNDS):
            file = open(base_filename + f"{k + 1}.txt")

            values = get_values(file.readlines())

            csv.write(",".join(values) + "\n")

            file.close()

        csv.close()
