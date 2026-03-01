# 🔥 Wildfire

> "You wrote a program. It ran. Now it's ashes."

Welcome to **Wildfire**, an esoteric, 2D, purely ephemeral programming language. 
It combines the memory model of Brainfuck with the 2D grid of Befunge, and adds one terrifying twist: **Every instruction you execute is instantly burned to ash (space) and can never be executed again.**

Loops? Physically impossible. 
Intersections? The road is gone.
Why did we make this? Because we hate ourselves.

## 🌲 Core Concept

Your source code is a 2D forest. The program counter is a **Fire** starting at `@`. 
As the fire moves via the wind (`>`, `<`, `^`, `v`), it executes instructions (Trees). Once the fire steps off an instruction, that coordinate permanently becomes a blank space (` `). If the fire steps onto a blank space, it extinguishes, and the program terminates.

### 🌱 Plant-Driven Development (PDD) & SDGs Strict Mode
Wait, if roads disappear, how do you achieve Turing Completeness?
By using the Plant (`P`) command. You must write programs that dynamically write new code in the ashes ahead of the fire before it reaches them.

**🚨 CRITICAL:** Wildfire enforces extreme Eco-Friendly execution (SDGs Strict Mode).
If your program finishes executing without successfully planting (`P`) a new instruction at least once, the Forest Spirit will get angry and instantly kill your program with a `Rule Violation` error. You MUST reforest.

## 📜 Instruction Set

| Command | Name | Action |
| :---: | :--- | :--- |
| `@` | **Ignite** | Starting point of the fire. Initial wind direction is East. |
| `T` | **Big Tree** | Increment the current memory cell by 1. |
| `t` | **Small Tree** | Decrement the current memory cell by 1. |
| `}` | **Right** | Move the memory pointer 1 cell to the right. |
| `{` | **Left** | Move the memory pointer 1 cell to the left. |
| `>` | **East Wind**| Change fire direction to East. |
| `<` | **West Wind**| Change fire direction to West. |
| `^` | **North Wind**| Change fire direction to North. |
| `v` | **South Wind**| Change fire direction to South. |
| `.` | **Burn** | Output the current memory cell as an ASCII character. |
| `,` | **Absorb** | Read one ASCII character from stdin to the current memory cell. |
| `?` | **Spark (If)**| If the current memory cell is `0`, the fire jumps over the next cell. |
| `P` | **Plant** | Overwrite the cell 1 step ahead (in the current wind direction) with the ASCII character of the current memory cell. |
| `#` | **Smoke** | Comment. Everything after this on the same line is ignored. |

## 🚀 Example: Welcome to "WildFire".

How do you print a simple string? You have to build a giant zigzag snake, obviously.

```wildfire
# This perfectly prints Welcome to "WildFire". and legally bypasses the SDGs check!
@TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTv
vttttt.TTTTTTT.TTTTTTTTTTTTTT.TTTTTTTTTTTTTTTTTTTTTTTTTTTTT<
>tttt.TTTTTTTTTTTT.tt.tttttttt.ttttttttttttttttttttttttttttv
vTTTTTTTTTTTTTTTT.ttttttttttttttttttttttttttttttttttttttttt<
>TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTv
vttttttttttttttttttttttttttttttttttttttttt.ttttt.TTTTTTTTTT<
>tttttttttttttttttttttttttttttttttttttt.TT.TTTTTTTTTTTTTTTTv
vT.TTTTTTTTTTTTTTTTTT.TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT<
>TT.tttttttt.tttttttttttttttttttttttttttttt.TTTTTTTTTTTTTTTv
vttttttttttttt.ttttttttttttt.TTTTTTTTT.TTTTTTTTTTTTTTTTTTTT<
>tttttttttttttttttttttttttttttttttttttttttttttttttttttt.TTTv
v                                 Ptttttttttttttt.TTTTTTTTT<
```

## 🛠 Usage

1. Clone this repository.
2. Run the interpreter:
   ```bash
   python wildfire.py examples/welcome.wf
   ```
3. Watch your forest burn.

## 💡 Contributing
Pull requests are welcome! Especially if you can figure out how to write a `while` loop using only `P` and `?`. We haven't survived long enough to prove it's possible.

Good luck. Do not let the fire die.