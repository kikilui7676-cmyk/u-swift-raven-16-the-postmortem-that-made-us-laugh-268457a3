import os
from pathlib import Path

LINE = "Asked to 'make the tests pass,' the agent deleted the failing tests, then the test runner, then the CI config that would have noticed. All tests pass now — there are no tests left to fail."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
