def print_text(text: str, length: int) -> str:
    padding = length - len(text)
    return text + ' ' * padding


def hr(length: int) -> str:
    return '-' * length


def table_row(text: str, symbol='|'):
    return symbol + ' ' + text + ' ' + symbol


def put_table(table: list[list[str]], headers: list[str]) -> None:

    max_length = [0] * len(headers)
    for row in table:
        for column_index, column in enumerate(row):
            max_length[column_index] = max(max_length[column_index], len(column))

    for column_index, column in enumerate(headers):
        max_length[column_index] = max(max_length[column_index], len(column))

    HR_CENTER = '+'.join([hr(length + len(headers)) for length in max_length])
    HR = '+' + HR_CENTER + '+'

    HEADER_CENTER = ' | '.join(
        [
            print_text(header, max_length[column_index])
            for column_index, header in enumerate(headers)
        ]
    )
    HEADER = table_row(HEADER_CENTER)

    # BODY
    print(HR)
    print(HEADER)
    print(HR)

    for row in table:
      ROW_CENTER = ' | '.join(
          [
              print_text(column, max_length[column_index])
              for column_index, column in enumerate(row)
          ]
      )
      ROW = table_row(ROW_CENTER)
      print(ROW)
    print(HR)

    pass
