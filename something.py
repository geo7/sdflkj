"""
Adding module docstring to shut pylint up.

This is a docstring which does nothing other than please a linter.
"""


def main() -> int:
    """Main function for pylint."""
    # Comment for the sake of it.
    # Another one.
    # Another one...
    print("this is something")
    print("fail black")
    x_for_pylint = 12
    del x_for_pylint
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
