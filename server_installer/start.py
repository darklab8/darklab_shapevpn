import sys

from src.app import main  # type: ignore[import]

if __name__ == "__main__":
    print(f"argv={sys.argv}")
    main()
