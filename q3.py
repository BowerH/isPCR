#!/usr/bin/env python3
import subprocess
import tempfile
import os

def bed_stuff(successful_amp_list):
    bed = []
    for i in successful_amp_list:
        name = i[0][1]  # Assuming contig name is in the same position for both primers
        start = int(i[0][9])  # End position of the forward primer
        end = int(i[1][8])  # Start position of the reverse primer
        bed.append(name + '\t' + str(start) + '\t' + str(end))
    return "\n".join(bed)


def step_three(hit_pairs: list[tuple[list[str]]], assembly_file: str) -> str:

    bed = bed_stuff(hit_pairs)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_bed:
        temp_bed.write(bed)
        bed_filepath = temp_bed.name

    result = subprocess.run(['seqtk', 'subseq', assembly_file, bed_filepath], capture_output=True, text=True, check=True)
    # Check for errors
    os.unlink(bed_filepath)

    return result.stdout
