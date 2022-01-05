# Program to Copy the Contents of One File into Another

with open("ASHI7.txt") as f:
    with open("ASHI4.txt", 'w') as f1:
        for line in f:
            f1.write(line)
        print("Content copied  ")