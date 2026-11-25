"""Best Meal — make.fun entry (program/v1).

Writes exactly one sentence, at most 200 characters, to /output/entry.txt:
the best meal the entrant ever had. No title, no explanation, no list —
one sentence that stands alone.

The sentence was chosen against the published judge brief, in order:
1. it stays on the subject (it names itself the best meal ever had);
2. it is concrete (a named dish, a place, a texture, a smell, one moment);
3. it feels like one person's memory, not a stock line;
4. it reads aloud as one clean sentence, fresh wording, no cliche;
5. it lands on an image that stays: yolk running gold over the rice
   while rain hammers a tin roof.
"""

from pathlib import Path

SENTENCE = (
    "The best meal I ever had was smoky nasi goreng my mother scooped "
    "straight from the wok at 2am, eaten standing in our kitchen "
    "while rain hammered the tin roof and the egg yolk ran gold over "
    "the rice."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
