"""
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:

Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.
[execution time limit] 4 seconds (py3)

[input] array.string chords

[output] array.string
"""
def csMakeItJazzy(chords):
    # loop through chords
    for idx in range(len(chords)):  #idx is just a number
    # if chord does not end with 7, add a 7 to the end
        if not chords[idx].endswith("7"):
            # so get chords number and assign to chords to add 7 to the idx.
            chords[idx] = chords[idx] + "7"
    return chords
    print(chords)
