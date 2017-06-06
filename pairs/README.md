This folder contains all pairs of the SICK corpus separated in their entailment relations. For each entailment relation there is a zip folder and a csv file. The csv file contains all pairs of this relation and the zip folder contains each pair in a separate txt file. The pair is parsed with the Stanford enhanced dependencies and mapped to PWN and SUMO senses.
The short_stats.txt holds some basic stats about the occurrences of each relation.
The csv files and the stats were generated with the script split_SICK_to_pairs.py.
The zip folders were generanted with the script map_parses_to_pairs.py.
