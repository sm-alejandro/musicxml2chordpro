chord_type_mapping = {
    "augmented": "+",
    "diminished": "dim",
    "diminished-seventh": "dim7",
    "dominant": "7",
    "dominant-ninth": "9",
    "half-diminished": "m7b5",
    "major": "",
    "major-seventh": "M7",
    "minor": "m",
    "minor-seventh": "m7",
    "minor-sixth": "m6",
    "other": "",
    "none": "none",
}

key_mapping = {
    -7: ("Cb", "Abmin"),
    -6: ("Gb", "Ebmin"),
    -5: ("Db", "Bbmin"),
    -4: ("Ab", "Fmin"),
    -3: ("Eb", "Cmin"),
    -2: ("Bb", "Gmin"),
    -1: ("F", "Dmin"),
    0: ("C", "Amin"),
    1: ("G", "Emin"),
    2: ("D", "Bmin"),
    3: ("A", "Fmin"),
    4: ("E", "C#min"),
    5: ("B", "G#min"),
    6: ("F#", "D#min"),
    7: ("C#", "A#min"),
}


accidental_mapping = {
    -2: "bb",
    -1: "b",
    0: "",
    1: "#",
    2: "##",
}
