import csv
tests = 7

def mean(a, b, c=None):
    if c is None:
        return (a + b) / 2
    else:
        return (a + b + c) / 3

def within_tolerance(a, b, tolerance):
    return abs(a - b) <= tolerance

def process_csv():
    with open('values.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = []
        for i in range(tests): # 7 tests
            for j in range(3): # 3 rows per test
                try:
                    row1 = [float(x) for x in next(reader)]
                    row2 = [float(x) for x in next(reader)]
                    row3 = [float(x) for x in next(reader)]
                except StopIteration:
                    break
                new_row = row1.copy() # copy the first row to preserve original data
                for k in range(2): # for each column in a row
                    col_k_row1 = row1[k]
                    col_k_row2 = row2[k]
                    col_k_row3 = row3[k]
                    if within_tolerance(col_k_row2, col_k_row1, col_k_row1 * 0.1) and within_tolerance(col_k_row3, col_k_row1, col_k_row1 * 0.1):
                        new_row.append(mean(col_k_row1, col_k_row2, col_k_row3))
                        row1[k] = str(row1[k]) + 'u'
                        row2[k] = str(row2[k]) + 'u'
                        row3[k] = str(row3[k]) + 'u'
                    elif within_tolerance(col_k_row2, col_k_row1, col_k_row1 * 0.1):
                        new_row.append(mean(col_k_row1, col_k_row2))
                        row1[k] = str(row1[k]) + 'u'
                        row2[k] = str(row2[k]) + 'u'
                    elif within_tolerance(col_k_row3, col_k_row1, col_k_row1 * 0.1):
                        new_row.append(mean(col_k_row1, col_k_row3))
                        row1[k] = str(row1[k]) + 'u'
                        row3[k] = str(row3[k]) + 'u'
                    elif within_tolerance(col_k_row3, col_k_row2, col_k_row2 * 0.1):
                        new_row.append(mean(col_k_row2, col_k_row3))
                        row2[k] = str(row2[k]) + 'u'
                        row3[k] = str(row3[k]) + 'u'
                    else:
                        new_row.append(mean(col_k_row1, col_k_row2, col_k_row3))
                        row1[k] = str(row1[k]) + 'u'
                        row2[k] = str(row2[k]) + 'u'
                        row3[k] = str(row3[k]) + 'u'
                    # Add 'u' to the values in row 1 that are used to calculate the mean
                    if k < len(new_row) - 2: # change here
                        new_row[k] = str(new_row[k]) + 'u'
                rows.append(new_row)
                rows.append([str(x) for x in row2])
                rows.append([str(x) for x in row3])
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

process_csv()
