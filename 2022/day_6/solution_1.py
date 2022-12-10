from pathlib import Path

N_UNIQUE = 4

def main():
    input_data = Path('input.txt').read_text().strip()

    for i in range(N_UNIQUE, len(input_data)):
        unique_chars = set(input_data[i-N_UNIQUE:i])
        if len(unique_chars) == N_UNIQUE:
            print(i)
            break


if __name__ == '__main__':
    main()
