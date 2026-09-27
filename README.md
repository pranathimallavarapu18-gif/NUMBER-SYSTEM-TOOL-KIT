# Number System & Advanced Math Toolkit 🚀

An interactive, responsive, and comprehensive web application providing number system conversions, binary arithmetic, bit manipulation, **Trigonometry**, and **Logarithms**.

---

## 🌟 Modules & Features

### 1. 🔄 Live Multi-Converter
- Real-time simultaneous conversion across **Decimal (Base 10)**, **Binary (Base 2)**, **Octal (Base 8)**, **Hexadecimal (Base 16)**, **Custom Radix (Bases 2–36)**, and **ASCII**.
- Live bit metrics (bit count, byte count, parity, powers of 2).

### 2. 🪜 Step-by-Step Solver
- **Decimal to Binary / Octal / Hexadecimal**: Continuous division method with quotients, remainders, and bottom-to-top remainder reading visualizations.
- **Binary / Octal / Hexadecimal to Decimal**: Positional weighted expansion with individual powers ($d \times \text{Base}^i$) and full addition steps.

### 3. 🧮 Decimal Arithmetic
- Addition, Subtraction, Multiplication, Division, and Modulus with step formulas and column math.

### 4. ⚡ Binary Arithmetic
- Direct binary calculations with decimal verification bridge, carry tracking, and borrow checks.

### 5. 🔍 Number Validator
- Character-by-character syntax validator for Binary, Octal, Decimal, and Hexadecimal numbers.

### 6. 🎛️ Interactive Bit Board
- Clickable 8-bit, 16-bit, and 32-bit registers. Live Unsigned, Signed (Two's Complement), Hexadecimal, and ASCII display with Bit Invert, Shift Left (`<<`), and Shift Right (`>>`).

### 7. 📐 Trigonometry Lab & Interactive Unit Circle (NEW)
- **Angle Modes**: Degrees (`DEG`), Radians (`RAD`), and Gradians (`GRAD`).
- **Live Animated Unit Circle Canvas**: Real-time visualization of radius vector $(r=1)$, angle $\theta$, Sine projection (green), Cosine projection (blue), and Tangent.
- **Functions**: $\sin$, $\cos$, $\tan$, $\csc$, $\sec$, $\cot$, $\sinh$, $\cosh$, $\tanh$.
- **Exact Radical Values**: Automatic lookup for standard angles ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ, \dots, 360^\circ$).

### 8. 📉 Logarithm Suite & Step Solver (NEW)
- **Multi-Base Calculation**: Common Log ($\log_{10}$), Natural Log ($\ln$), Binary Log ($\log_2$), and Arbitrary Base Log ($\log_b$).
- **Change of Base Step-by-Step Breakdown**: $\log_b(x) = \frac{\ln(x)}{\ln(b)}$ with intermediate decimal calculation and exponential verification ($b^{\text{result}} \approx x$).
- **Dynamic Log Curve Canvas**: Plots the continuous curve $y = \log_b(x)$ with vertical asymptote $x=0$, $x$-intercept $(1,0)$, and point coordinates.
- **Logarithmic Laws**: Product, Quotient, and Power rule references.

### 9. 📊 Cheat Sheet & Reference Tables
- 4-bit Hexadecimal Nibble Table (Decimal 0–15) and Powers of 2 ($2^0$ to $2^{16}$) with storage units.

### 10. 🎯 Practice & Quiz Mode
- Infinite randomized challenges for Base Conversions, Binary Arithmetic, Trigonometry, and Logarithms with instant feedback and streaks.

---

## 🚀 How to Run

1. Open [`index.html`](file:///C:/Users/pranathi/.gemini/antigravity/scratch/number-system-toolkit/index.html) in your browser.
2. Or run via local server:
   ```powershell
   cd C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit
   python -m http.server 8000
   ```
   Visit `http://localhost:8000`.
