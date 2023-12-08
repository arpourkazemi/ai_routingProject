def get_input():
    rows, cols = map(int, input().split())
    matrix = []
    for i in range(rows):
        row_values = list( input().split())
        matrix.append(row_values)
    return matrix


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            rows, cols = map(int, file.readline().split())
            matrix = []
            for i in range(rows):
                row_values = list( file.readline().split())
                matrix.append(row_values)
        return matrix
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

