from pathlib import Path


def get_input() -> list[str]:
    return Path('input.txt').read_text().splitlines()


def get_current_from_path(filesystem, path):
    if path == '/':
        return filesystem

    current = filesystem
    for folder in path.split('.')[1:]:
        current = current[folder]

    return current


def handle_cd(dest, filesystem, current, path):
    if dest == '/':
        return filesystem, '/'

    if dest == '..':
        new_path = '.'.join(path.split('.')[:-1])
        return get_current_from_path(filesystem, new_path), new_path

    new_path = f'{path}.{dest}'
    return get_current_from_path(filesystem, new_path), new_path


def parse_command(command, filesystem, current, path):
    cleaned_command = command[2:].strip()

    cmd, *args = cleaned_command.split(' ')

    if cmd == 'cd':
        return handle_cd(args[0], filesystem, current, path)
    elif cmd == 'ls':  # We can ignore ls as we handle non-commands another way
        return current, path


def parse_line(line, filesystem, current, path):
    if not line.startswith('$'):
        desc, filename = line.split()

        if desc == 'dir':
            current[filename] = {}
        else:
            current[filename] = int(desc)
        return current, path

    return parse_command(line, filesystem, current, path)


def calculate_directory_sizes(name, directory, directory_sizes):
    num = sum(
        # Use path to avoid duplicates in dictionary
        calculate_directory_sizes(f'{name}.{subname}', subdir, directory_sizes)
        if isinstance(subdir, dict)
        else subdir
        for subname, subdir in directory.items()
    )
    directory_sizes[name] = num
    return num


def main():
    filesystem = {}
    input_data = get_input()

    current = filesystem
    path = '/'
    for line in input_data:
        current, path = parse_line(line, filesystem, current, path)

    # Find all directories and subdirectories with a total size of less than
    # 100_000 bytes
    directory_sizes = {}
    calculate_directory_sizes('/', filesystem, directory_sizes)
    small_directories = {
        name: size
        for name, size in directory_sizes.items()
        if size < 100_000
    }
    print(small_directories)
    print(sum(small_directories.values()))


if __name__ == '__main__':
    main()
