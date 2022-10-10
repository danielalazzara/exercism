def convert(input_grid):
    if not len(input_grid) % 4 ==0:
        raise ValueError("Number of input lines is not a multiple of four")
    if not len(input_grid[0]) % 3 ==0:
        raise ValueError("Number of input columns is not a multiple of three")
    else:
        print()
        row = len(input_grid) // 4
        new = ["", "", "", ""]
        for x in range(row):
            for i in range(4):
                new[i] += input_grid[4 * x + i] + ",,," if x != row - 1 else input_grid[4 * x + i]
        input_grid = new

    ocr = {" _ | ||_|   ": "0",
           "     |  |   ": "1",
           " _  _||_    ": "2",
           " _  _| _|   ": "3",
           "   |_|  |   ": "4",
           " _ |_  _|   ": "5",
           " _ |_ |_|   ": "6",
           " _   |  |   ": "7",
           " _ |_||_|   ": "8",
           " _ |_| _|   ": "9",
           ",,,,,,,,,,,,": ","}
    
    output = ""
    for x in range(len(input_grid[0]) // 3):
        number = ""
        for i in range(4):
            number += input_grid[i][3 * x:3 * x + 3]
        output += ocr[number] if number in ocr else "?"
    return output
  
