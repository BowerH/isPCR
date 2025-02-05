#!/usr/bin/env python3

def step_two(sorted_hits: list[str], max_amplicon_size: int) -> list[tuple[list[str]]]:
    successful_amp =[]
    for i in range(len(sorted_hits)):
        for j in range(i+1, len(sorted_hits)):
            primer1 = sorted_hits[i]
            primer2 = sorted_hits[j]

            # Ensure they are different primer types
            #if primer1[0] == primer2[0]:
                #continue

            start1= int(primer1[8])
            end1 = int(primer1[9])
            start2 = int(primer2[8])
            end2 = int(primer2[9])

            if primer1[0] == '515F' and primer2[0] == '806R':
                if (end1 > start1) and (end2 < start2) and (start1 < start2):
                    dist = end2 - start1
                    if dist < max_amplicon_size:
                        successful_amp.append((primer1, primer2))
            elif primer1[0] == '806R' and primer2[0] == '515F':
                if (end1 < start1) and end2 > start2 and start2 < start1:
                    dist = end1 - start2
                    if dist < max_amplicon_size:
                        successful_amp.append((primer2, primer1))

    return successful_amp

print()