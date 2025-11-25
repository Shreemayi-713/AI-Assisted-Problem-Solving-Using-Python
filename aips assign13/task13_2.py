def read_file(path: str) -> str:
    """Return file contents with basic error handling."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{path!r} does not exist.") from exc
    except PermissionError as exc:
        raise PermissionError(f"No access to {path!r}.") from exc
    except OSError as exc:
        raise OSError(f"Cannot read {path!r}: {exc}") from exc


def main() -> None:
    print("Legacy reader with proper error handling\n(type 'quit' to exit)")
    while True:
        filename = input("File name: ").strip()
        if filename.lower() in {"quit", "q", "exit"}:
            break
        if not filename:
            print("Please enter a file name.")
            continue
        try:
            print("\n--- file contents ---")
            print(read_file(filename))
            print("--- end ---\n")
        except (FileNotFoundError, PermissionError, OSError) as err:
            print(err)
        except Exception as err:  # safeguard for unexpected issues
            print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()

