''' CUI to convert tsv files to csv files
A command line interface to convert tsv files to csv files.
'''

import os
import sys
import csv
import argparse
import chardet


def convert(src_file, dst_file, src_delimiter, dst_delimiter):
    with open(src_file, 'rb') as f:
        enc = chardet.detect(f.read())
    tsv_f = open(src_file, 'r', encoding=enc['encoding'])
    tsv = csv.reader(tsv_f, delimiter=src_delimiter)
    with open(dst_file, 'w', newline="", encoding=enc['encoding']) as csv_f:
        writer = csv.writer(csv_f, delimiter=dst_delimiter)
        for row in tsv:
            writer.writerow(row)
        csv_f.close()
    tsv_f.close()


def tsv_to_csv(src_file, dst_file):
    convert(src_file, dst_file, '\t', ',')


def csv_to_tsv(src_file, dst_file):
    convert(src_file, dst_file, ',', '\t')


parser = argparse.ArgumentParser(
    description='convert tsv file to csv file.', 
    usage='%(prog)s [options]')
parser.add_argument('--i', '--input', required=True, help='-o : Please input file name.')
parser.add_argument('--o', '--output', required=True, help='-i : Please output file name.')
args = parser.parse_args()

src_file = args.i
dst_file = args.o

if src_file is None:
    print('ERROR: Please specify the input file.')
    sys.exit()
if dst_file is None:
    print('ERROR: Please specify the output file.')
    sys.exit()

ext = os.path.splitext(src_file)
print(ext)

if ext[1] == '.tsv':
    tsv_to_csv(src_file, dst_file)
else:
    csv_to_tsv(src_file, dst_file)

print('Successfully converted.')
