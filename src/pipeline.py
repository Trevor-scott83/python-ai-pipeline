# pipeline.py
# Stage 1 - Read structed data and print each row

filename = "data/sample.csv"

with open(filename) as f:
    for line in f:
        print(line.strip())