"""
Adding module docstring to shut pylint up.

This is a docstring which does nothing other than please a linter.
"""


def main() -> int:
    print("this is something")
    print("fail black")
    x = 12
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
