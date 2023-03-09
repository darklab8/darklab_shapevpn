from src.app import main  # type: ignore[import]
import sys

if __name__ == "__main__":
    print(f"argv={sys.argv}")
    main()
