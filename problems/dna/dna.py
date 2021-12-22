import sys
import csv

# STR checker (the style50 made me to make this space :( its uglay AF)


def checker(str, dna):
    i = 0
    while str*(i + 1) in dna:
        i += 1
    return i

# matcher


def matcher(main, DNA, row):
    for str in main:
        if DNA[str] != int(row[str]):
            return False
    return True


# Make sure theres only 3 argument vector.
def main():
    while(len(sys.argv) != 3):
        print("wrong input")
        sys.exit(1)

    # open databases and sequences files
    data_base = open(sys.argv[1])
    data_base_reader = csv.DictReader(data_base)
    main = data_base_reader.fieldnames[1:]

    dna = open(sys.argv[2])
    dna_reader = csv.reader(dna)
    dna = dna.read()

    # count number of each STR
    DNA = {}
    for str in main:
        DNA[str] = checker(str, dna)

    # search till find a match
    for row in data_base_reader:
        if matcher(main, DNA, row):
            print(f"{row['name']}")
            data_base.close()
            return
    # if couldnt find any match for it, print an error and close file
    print('No match')
    data_base.close()
    sys.exit(2)


main()