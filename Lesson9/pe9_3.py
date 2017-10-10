import csv

csv_path = 'scores.csv'
hi_score_row = ['', '', 0]

raw_csv_file = open(csv_path, 'r')
csv_file = csv.reader(raw_csv_file, delimiter=';')
csv_list = [row for row in csv_file]

for row in csv_list:
    if int(row[2]) > int(hi_score_row[2]):
        hi_score_row = row

print('De hoogste score is: {} op {} behaald door {}'.format(
    hi_score_row[2],
    hi_score_row[1],
    hi_score_row[0]
))
