import os

examples = {
    "1": "examples/example_01_read_csv.py",
    "2": "examples/example_02_dataframe.py",
    "3": "examples/example_03_head.py",
    "4": "examples/example_04_tail.py",
    "5": "examples/example_05_info.py",
    "6": "examples/example_06_describe.py",
    "7": "examples/example_07_sort.py",
    "8": "examples/example_08_filter.py",
    "9": "examples/example_09_groupby.py",
    "10": "examples/example_10_merge.py",
    "11": "examples/example_11_fillna.py",
    "12": "examples/example_12_dropna.py",
    "13": "examples/example_13_apply.py",
    "14": "examples/example_14_to_csv.py",
    "15": "examples/example_15_plot.py"
}

print("=== Pandas piemēri ===")

for key in examples:
    print(f"{key} - {examples[key]}")

choice = input("Izvēlies piemēru: ")

if choice in examples:
    os.system(f"python {examples[choice]}")
else:
    print("Nepareiza izvēle")