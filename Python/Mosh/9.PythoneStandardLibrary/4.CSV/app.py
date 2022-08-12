import csv


# with open("data.csv", "w") as File:
#     write = csv.writer(File)
#     write.writerow(["transaction_id", "product_id", "Price"])
#     write.writerow([1, 100, 10])
#     write.writerow([2, 101, 10243])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))

    for row in reader:
        print(row)
