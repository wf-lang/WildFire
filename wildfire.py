import sys
import os

def exec(src):
    grid = []
    for line in src.split('\n'):
        line = line.strip('\r')
        if '#' in line:
            line = line[:line.index('#')]
        grid.append(list(line))
    height = len(grid)
    width = max((len(row) for row in grid), default=0)
    if width == 0:
        return
    for i in range(height):
        grid[i].extend([' '] * (width - len(grid[i])))
    start_x, start_y = -1, -1
    has_plant_command = False
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '@':
                start_x, start_y = x, y
            if grid[y][x] == 'P':
                has_plant_command = True
    if start_x == -1:
        sys.stderr.write("Error: Starting point '@' not found.\n")
        sys.exit(1)
    if not has_plant_command:
        sys.stderr.write("Error: Rule Violation. No 'P' command found in source. Execution denied.\n")
        sys.exit(1)
    memory = [0] * 30000
    pointer = 0
    dx, dy = 1, 0
    x, y = start_x, start_y
    has_planted_at_runtime = False
    while 0 <= x < width and 0 <= y < height:
        char = grid[y][x]
        if char == ' ':
            break
        grid[y][x] = ' '
        if char == 'T':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif char == 't':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif char == '}':
            pointer += 1
        elif char == '{':
            pointer = max(0, pointer - 1)
        elif char == '>':
            dx, dy = 1, 0
        elif char == '<':
            dx, dy = -1, 0
        elif char == '^':
            dx, dy = 0, -1
        elif char == 'v':
            dx, dy = 0, 1
        elif char == '.':
            sys.stdout.write(chr(memory[pointer]))
            sys.stdout.flush()
        elif char == ',':
            ch = sys.stdin.read(1)
            memory[pointer] = ord(ch) if ch else 0
        elif char == '?':
            if memory[pointer] == 0:
                x += dx
                y += dy
        elif char == 'P':
            has_planted_at_runtime = True
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                grid[ny][nx] = chr(memory[pointer])
        x += dx
        y += dy
    if not has_planted_at_runtime:
        sys.stderr.write("\nError: Rule Violation. The 'P' command was not executed during runtime. Forest died.\n")
        sys.exit(1)

def idle():
    sys.stdout.write("Wildfire IDLE (Enter 'RUN' to execute, 'EXIT' to quit)\n")
    while True:
        sys.stdout.write("WF> ")
        sys.stdout.flush()
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                return
            if line.strip() == "EXIT":
                return
            if line.strip() == "RUN":
                break
            lines.append(line)
        if lines:
            source = '\n'.join(lines)
            exec(source)
            sys.stdout.write("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                exec(f.read())
        else:
            sys.stdout.write("File not found.\n")
    else:
        idle()