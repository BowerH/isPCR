#!/usr/bin/env python3
import subprocess


def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        header = ''
        sequence = []
        for i in file:
            if i.startswith('>'):
                if header:
                    sequences[header] = ''.join(sequence)
                header = i[1:]
                sequence = []
            else:
                sequence.append(i)
        if header:
            sequences[header] = ''.join(sequence)
    return sequences


def blastn(primer_file, assembly_file):
    blastsearch = [
        'blastn',
        '-task', 'blastn-short',
        '-query', primer_file,
        '-subject', assembly_file,
        '-outfmt', '6 std qlen',
        '-strand', 'both'
    ]
    result = subprocess.run(blastsearch, capture_output=True, text=True)
    return result.stdout


def blast_greater80(blast_output):
    final = []
    for j in blast_output.strip().split('\n'):
        column = j.split('\t')
        percent_identity = float(column[2])
        if percent_identity >= 80.0:
            final.append(column)
    return final


def step_one(primer_file: str, assembly_file: str) -> list[list[str]]:
    primers = read_fasta(primer_file)
    assembly_sequences = read_fasta(assembly_file)
    blastfinal = blastn(primer_file, assembly_file)
    filtered_results = blast_greater80(blastfinal)
    finalfiltered = []
    for f in filtered_results:
        temp = []
        for t in f:
            temp.append(str(t))
        finalfiltered.append(temp)
    return finalfiltered


p = '/Users/hannah/PycharmProjects/Exercise8/Hbower6/data/general_16S_515f_806r.fna'
a = '/Users/hannah/PycharmProjects/Exercise8/Hbower6/data/Vibrio_cholerae_N16961.fna'

looking = (step_one(p, a))
print()
