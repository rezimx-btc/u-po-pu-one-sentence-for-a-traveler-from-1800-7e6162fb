"""One sentence that explains the modern internet to a traveler from 1800.

Every word in the sentence was in use before 1800: web, wire, letter,
voice, face, town, lightning. No word coined after the traveler's time.
"""

LINE = (
    "Think of a web of thin wires spun round the whole earth, so that a "
    "letter, a voice, or a face may fly from any town to any other "
    "swifter than lightning."
)


def main() -> None:
    # The brief's own guards: exactly one sentence, at most 200 characters.
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be one sentence"
    assert len(LINE) <= 200, "must be at most 200 characters"
    print(LINE)


if __name__ == "__main__":
    main()
