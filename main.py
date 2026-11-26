"""One line of earned pride, for make.fun.

The brief: a quiet, earned moment of pride for someone in a scene, at most
240 characters, landing in one read. A small person doing something hard, a
long effort finally landing. Forty years of night shifts ends in one small
act: hanging his own nameplate, straightening it twice, and standing back.
The pride is in the straightening, not in the announcement.
"""

LINE = "After forty years of night shifts, my father finally hung his own nameplate on the workshop door, straightened it twice, and stood back to look at it for a long time."

# The entry must be exactly one line of 1-240 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, limit is 240"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
