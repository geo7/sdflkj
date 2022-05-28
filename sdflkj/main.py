"""
Adding module docstring to shut pylint up.

This is a docstring which does nothing other than please a linter.
"""

from . import util


def main() -> int:
    """Main function for pylint."""
    print("using util func")
    print(util.add(1, 2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
