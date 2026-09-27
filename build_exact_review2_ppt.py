import sys
import os
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_exact_reference_ppt(output_path):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Exact Color Palette matching reference
    NAVY_DARK    = RGBColor(30, 42, 94)      # #1E2A5E Deep Navy from reference
    NAVY_TITLE   = RGBColor(27, 42, 95)      # Title Navy
    CATEGORY_BLU = RGBColor(59, 130, 246)    # Sky/Blue Accent #3B82F6
    BG_LIGHT     = RGBColor(255, 255, 255)   # White
    CIRCLE_RING  = RGBColor(219, 234, 254)   # Soft Blue ring #DBEAFE
    CIRCLE_BG    = RGBColor(238, 242, 255)   # Soft icon circle #EEF2FF
    CODE_BOX_BG  = RGBColor(15, 23, 42)      # Deep dark code box #0F172A
    CODE_TEXT    = RGBColor(241, 245, 249)   # Code text off-white
    OUTPUT_BG    = RGBColor(10, 15, 30)      # Terminal box
    OUTPUT_TITLE = RGBColor(56, 189, 248)    # Output title Sky Blue
    OUTPUT_TEXT  = RGBColor(203, 213, 225)   # Slate text
    OUTPUT_GREEN = RGBColor(74, 222, 128)    # Bright green text
    TEXT_BODY    = RGBColor(71, 85, 105)     # #475569 Body Slate
    TEXT_DARK    = RGBColor(30, 41, 59)      # #1E293B Dark Slate
    TEXT_LIGHT   = RGBColor(255, 255, 255)   # White
    FOOTER_COLOR = RGBColor(148, 163, 184)   # Muted Footer

    def add_mac_code_box(slide, left, top, width, height, code_text):
        # Code Box Background
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        box.fill.solid()
        box.fill.fore_color.rgb = CODE_BOX_BG
        box.line.color.rgb = RGBColor(30, 41, 59)
        box.line.width = Pt(1)

        # 3 macOS dots: Red, Yellow, Green
        dot_y = top + 0.18
        dot_r = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.22), Inches(dot_y), Inches(0.14), Inches(0.14))
        dot_r.fill.solid()
        dot_r.fill.fore_color.rgb = RGBColor(239, 68, 68)  # Red
        dot_r.line.fill.background()

        dot_y_sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.42), Inches(dot_y), Inches(0.14), Inches(0.14))
        dot_y_sh.fill.solid()
        dot_y_sh.fill.fore_color.rgb = RGBColor(234, 179, 8) # Yellow
        dot_y_sh.line.fill.background()

        dot_g = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.62), Inches(dot_y), Inches(0.14), Inches(0.14))
        dot_g.fill.solid()
        dot_g.fill.fore_color.rgb = RGBColor(34, 197, 94)  # Green
        dot_g.line.fill.background()

        # Code text box
        tb = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.38), Inches(width - 0.4), Inches(height - 0.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        lines = code_text.strip().split('\n')
        for idx, l in enumerate(lines):
            p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
            p.text = l
            p.font.name = "Consolas"
            p.font.size = Pt(10.5)
            p.font.color.rgb = CODE_TEXT
            p.space_after = Pt(1)

    def add_terminal_output_box(slide, left, top, width, height, output_lines):
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        box.fill.solid()
        box.fill.fore_color.rgb = OUTPUT_BG
        box.line.color.rgb = RGBColor(30, 41, 59)
        box.line.width = Pt(1)

        tb = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.15), Inches(width - 0.5), Inches(height - 0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = "PROGRAM OUTPUT"
        p0.font.name = "Calibri"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = OUTPUT_TITLE
        p0.space_after = Pt(6)

        for l in output_lines:
            p = tf.add_paragraph()
            p.text = l
            p.font.name = "Consolas"
            p.font.size = Pt(10)
            if "completed" in l.lower() or "passed" in l.lower() or "result:" in l.lower() or "final" in l.lower():
                p.font.color.rgb = OUTPUT_GREEN
            else:
                p.font.color.rgb = OUTPUT_TEXT
            p.space_after = Pt(1.5)

    def add_module_slide(prs, mod_num, mod_title, what_it_does, cpp_concepts, code_text, output_lines):
        slide = prs.slides.add_slide(blank_layout)

        # Top small category text
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(6.0), Inches(0.35))
        ctf = cat_box.text_frame
        cp = ctf.paragraphs[0]
        cp.text = "M O D U L E S   ·   E X P L A N A T I O N"
        cp.font.name = "Calibri"
        cp.font.size = Pt(11)
        cp.font.bold = True
        cp.font.color.rgb = CATEGORY_BLU

        # Module Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(6.5), Inches(0.65))
        ttf = title_box.text_frame
        tp = ttf.paragraphs[0]
        tp.text = f"Module {mod_num} — {mod_title}"
        tp.font.name = "Calibri"
        tp.font.size = Pt(24)
        tp.font.bold = True
        tp.font.color.rgb = NAVY_TITLE

        # Left Column - What It Does
        left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(5.0), Inches(5.1))
        ltf = left_box.text_frame
        ltf.word_wrap = True
        ltf.margin_left = ltf.margin_top = ltf.margin_right = ltf.margin_bottom = 0

        # "What It Does" header
        wp = ltf.paragraphs[0]
        wp.text = "What It Does"
        wp.font.name = "Calibri"
        wp.font.size = Pt(17)
        wp.font.bold = True
        wp.font.color.rgb = NAVY_TITLE
        wp.space_after = Pt(8)

        # Description
        dp = ltf.add_paragraph()
        dp.text = what_it_does
        dp.font.name = "Calibri"
        dp.font.size = Pt(13)
        dp.font.color.rgb = TEXT_BODY
        dp.space_after = Pt(20)

        # C++ CONCEPTS USED header
        cp2 = ltf.add_paragraph()
        cp2.text = "C++ CONCEPTS USED"
        cp2.font.name = "Calibri"
        cp2.font.size = Pt(12)
        cp2.font.bold = True
        cp2.font.color.rgb = CATEGORY_BLU
        cp2.space_after = Pt(12)

        # Concepts bullets
        for title, desc in cpp_concepts:
            bp = ltf.add_paragraph()
            bp.text = f"●   {title} — {desc}"
            bp.font.name = "Calibri"
            bp.font.size = Pt(12)
            bp.font.color.rgb = TEXT_DARK
            bp.space_after = Pt(8)

        # Right Column - Code Box & Output Box
        add_mac_code_box(slide, 6.2, 1.4, 6.3, 3.6, code_text)
        add_terminal_output_box(slide, 6.2, 5.2, 6.3, 1.75, output_lines)

        # Footer
        foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(6.0), Inches(0.3))
        ftf = foot_box.text_frame
        fp = ftf.paragraphs[0]
        fp.text = "Number System Toolkit (C++) · 2nd Review"
        fp.font.name = "Calibri"
        fp.font.size = Pt(10)
        fp.font.color.rgb = FOOTER_COLOR

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Exact Reference Layout)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY_DARK
    bg1.line.color.rgb = NAVY_DARK

    # Top-left white square badge
    sq = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.3), Inches(0.45), Inches(0.45))
    sq.fill.solid()
    sq.fill.fore_color.rgb = RGBColor(219, 234, 254)
    sq.line.fill.background()

    # Right large circular graphic
    outer_circ = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.8), Inches(1.5), Inches(4.5), Inches(4.5))
    outer_circ.fill.solid()
    outer_circ.fill.fore_color.rgb = RGBColor(23, 33, 75)
    outer_circ.line.fill.background()

    inner_circ = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.5), Inches(2.2), Inches(3.1), Inches(3.1))
    inner_circ.fill.solid()
    inner_circ.fill.fore_color.rgb = RGBColor(255, 255, 255)
    inner_circ.line.fill.background()

    # Icon/Emblem in inner circle
    itf = inner_circ.text_frame
    itf.vertical_anchor = MSO_ANCHOR.MIDDLE
    ip = itf.paragraphs[0]
    ip.text = "🔢"
    ip.font.size = Pt(48)
    ip.alignment = PP_ALIGN.CENTER

    # Title & Subtitle text
    tbox = s1.shapes.add_textbox(Inches(0.9), Inches(2.4), Inches(8.5), Inches(2.2))
    ttf = tbox.text_frame
    ttf.word_wrap = True
    tp = ttf.paragraphs[0]
    tp.text = "NUMBER SYSTEM TOOLKIT"
    tp.font.name = "Calibri"
    tp.font.size = Pt(36)
    tp.font.bold = True
    tp.font.color.rgb = TEXT_LIGHT

    sub_p = ttf.add_paragraph()
    sub_p.text = "A Unified C++ Platform for Multi-Base Conversions & Digital Logic Operations"
    sub_p.font.name = "Calibri"
    sub_p.font.size = Pt(16)
    sub_p.font.italic = True
    sub_p.font.color.rgb = RGBColor(203, 213, 225)
    sub_p.space_before = Pt(8)

    # Team Box at bottom
    tm_box = s1.shapes.add_textbox(Inches(0.9), Inches(4.8), Inches(8.5), Inches(2.2))
    tm_tf = tm_box.text_frame
    tm_p0 = tm_tf.paragraphs[0]
    tm_p0.text = "TEAM MEMBERS:"
    tm_p0.font.name = "Calibri"
    tm_p0.font.size = Pt(11)
    tm_p0.font.bold = True
    tm_p0.font.color.rgb = CATEGORY_BLU
    tm_p0.space_after = Pt(4)

    team_str = (
        "25B11DS349 - M. Lakshmi Srinivas  |  25B11DS127 - D. Varaprasad\n"
        "25B11DS370 - N. Akhila Devi  |  25B11DS628 - Y. Nithya Sree  |  25B11DS320 - M. Venkata Pranathi\n"
        "Department of Computer Science & Engineering (Data Science) · Aditya University"
    )
    for line in team_str.split('\n'):
        p = tm_tf.add_paragraph()
        p.text = line
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = RGBColor(226, 232, 240)
        p.space_after = Pt(2)

    # =========================================================================
    # SLIDE 2: ABSTRACT SLIDE (Exact Reference Layout)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)

    # Top-right background decorative circle
    dec_ring = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.8), Inches(-1.5), Inches(5.0), Inches(5.0))
    dec_ring.fill.solid()
    dec_ring.fill.fore_color.rgb = CIRCLE_RING
    dec_ring.line.fill.background()

    dec_inner = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.8), Inches(-0.5), Inches(3.0), Inches(3.0))
    dec_inner.fill.solid()
    dec_inner.fill.fore_color.rgb = BG_LIGHT
    dec_inner.line.fill.background()

    # Bell icon inside circle
    bell_box = s2.shapes.add_textbox(Inches(11.0), Inches(0.4), Inches(1.5), Inches(1.5))
    btf = bell_box.text_frame
    bp = btf.paragraphs[0]
    bp.text = "🔔"
    bp.font.size = Pt(36)
    bp.alignment = PP_ALIGN.CENTER

    # Abstract Title
    ab_box = s2.shapes.add_textbox(Inches(0.9), Inches(0.9), Inches(6.0), Inches(0.8))
    atf = ab_box.text_frame
    ap = atf.paragraphs[0]
    ap.text = "Abstract"
    ap.font.name = "Calibri"
    ap.font.size = Pt(32)
    ap.font.bold = True
    ap.font.color.rgb = NAVY_TITLE

    # Abstract Bullet Points (5 bullets exactly like reference)
    abs_bullets = [
        "Manual number system conversions are time-consuming and error-prone for students.",
        "This toolkit digitizes and automates multi-base calculations with verified step-by-step logic.",
        "Integrates standard bases (Binary, Octal, Hexadecimal) and arbitrary custom bases (2 to 36).",
        "Includes full binary arithmetic, bitwise manipulation, 1's/2's complements, and math suites.",
        "Provides real-time instant computations and mathematical explanations for informed learning."
    ]

    abs_tb = s2.shapes.add_textbox(Inches(0.9), Inches(2.3), Inches(10.5), Inches(4.5))
    ab_tf = abs_tb.text_frame
    ab_tf.word_wrap = True

    for idx, b_text in enumerate(abs_bullets):
        p = ab_tf.paragraphs[0] if idx == 0 else ab_tf.add_paragraph()
        p.text = f"•   {b_text}"
        p.font.name = "Calibri"
        p.font.size = Pt(15.5)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(22)

    # =========================================================================
    # SLIDE 3: KEY MODULES (Exact Reference 2x2 Grid Layout)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)

    km_box = s3.shapes.add_textbox(Inches(0.9), Inches(0.9), Inches(6.0), Inches(0.8))
    ktf = km_box.text_frame
    kp = ktf.paragraphs[0]
    kp.text = "Key Modules"
    kp.font.name = "Calibri"
    kp.font.size = Pt(32)
    kp.font.bold = True
    kp.font.color.rgb = NAVY_TITLE

    modules_2x2 = [
        # (Col 1/2, Row 1/2, Icon, Title)
        (0.9, 2.3, "🔄", "Multi-Base Conversion & Solver"),
        (6.8, 2.3, "➕", "Binary Arithmetic Operations"),
        (0.9, 4.4, "⚙️", "Bitwise Manipulation & Complements"),
        (6.8, 4.4, "📐", "Advanced Math (Trig & Log Suite)")
    ]

    for left, top, icon_char, title_str in modules_2x2:
        # Icon Circle
        circ = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left), Inches(top), Inches(0.9), Inches(0.9))
        circ.fill.solid()
        circ.fill.fore_color.rgb = CIRCLE_BG
        circ.line.color.rgb = CIRCLE_RING
        circ.line.width = Pt(1)

        c_tf = circ.text_frame
        c_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        cp = c_tf.paragraphs[0]
        cp.text = icon_char
        cp.font.size = Pt(20)
        cp.alignment = PP_ALIGN.CENTER

        # Title Label
        t_box = s3.shapes.add_textbox(Inches(left + 1.1), Inches(top + 0.18), Inches(4.5), Inches(0.6))
        ttf = t_box.text_frame
        ttf.word_wrap = True
        tp = ttf.paragraphs[0]
        tp.text = title_str
        tp.font.name = "Calibri"
        tp.font.size = Pt(15.5)
        tp.font.color.rgb = TEXT_DARK
        tp.font.bold = False

    # =========================================================================
    # SLIDE 4: MODULE 1 — Multi-Base Conversion
    # =========================================================================
    mod1_what = (
        "Converts numbers seamlessly between Decimal, Binary, Octal, "
        "Hexadecimal, and Custom bases (2–36) using repeated division "
        "and positional power expansion algorithms."
    )
    mod1_cpp = [
        ("Classes & Objects", "a NumberSystem class encapsulates all conversion algorithms"),
        ("Encapsulation", "base radix and digit mappings are maintained securely"),
        ("Loops & Strings", "repeated modulus division extracts remainders into dynamic strings"),
        ("Standard Library", "std::reverse() orders remainders from MSB to LSB")
    ]
    mod1_code = (
        "class NumberSystem {\n"
        "public:\n"
        "  string decimalToBase(int num, int base) {\n"
        "    if (num == 0) return \"0\";\n"
        "    string digits = \"0123456789ABCDEF\";\n"
        "    string result = \"\";\n"
        "    while (num > 0) {\n"
        "      result += digits[num % base];\n"
        "      num /= base;\n"
        "    }\n"
        "    reverse(result.begin(), result.end());\n"
        "    return result;\n"
        "  }\n"
        "};"
    )
    mod1_output = [
        "-- Multi-Base Conversion Output --",
        "Input Decimal : 255",
        "Binary (Base 2) : 11111111",
        "Octal  (Base 8) : 377",
        "Hex    (Base 16): FF",
        "Conversion completed successfully."
    ]
    add_module_slide(prs, 1, "Multi-Base Conversion", mod1_what, mod1_cpp, mod1_code, mod1_output)

    # =========================================================================
    # SLIDE 5: MODULE 2 — Binary Arithmetic Operations
    # =========================================================================
    mod2_what = (
        "Performs fundamental binary arithmetic operations (Addition, "
        "Subtraction, Multiplication, and Division) with full bit-level "
        "carry propagation and digit alignment."
    )
    mod2_cpp = [
        ("Modular Functions", "addBinary() models full-adder logic with carry propagation"),
        ("Pass-by-Value & Loops", "iterates through binary strings from LSB to MSB"),
        ("String Arithmetic", "converts char digits to integer values on the fly"),
        ("Control Flow", "handles carry overflow and variable length binary inputs")
    ]
    mod2_code = (
        "string addBinary(string a, string b) {\n"
        "  string result = \"\";\n"
        "  int i = a.length() - 1, j = b.length() - 1;\n"
        "  int carry = 0;\n"
        "  while (i >= 0 || j >= 0 || carry) {\n"
        "    int sum = carry;\n"
        "    if (i >= 0) sum += a[i--] - '0';\n"
        "    if (j >= 0) sum += b[j--] - '0';\n"
        "    result += to_string(sum % 2);\n"
        "    carry = sum / 2;\n"
        "  }\n"
        "  reverse(result.begin(), result.end());\n"
        "  return result;\n"
        "}"
    )
    mod2_output = [
        "-- Binary Arithmetic Simulator --",
        "Binary A: 10110 (Decimal 22)",
        "Binary B: 01101 (Decimal 13)",
        "Operation: Addition (+)",
        "Carry Generated: 1",
        "Result: 100011 (Decimal 35)"
    ]
    add_module_slide(prs, 2, "Binary Arithmetic Operations", mod2_what, mod2_cpp, mod2_code, mod2_output)

    # =========================================================================
    # SLIDE 6: MODULE 3 — Bitwise Manipulation & Complements
    # =========================================================================
    mod3_what = (
        "Executes low-level bitwise operations (AND, OR, XOR, NOT, Bit-shifts) "
        "and calculates 1's and 2's Complement representations for signed binary "
        "numbers."
    )
    mod3_cpp = [
        ("Bitwise Operators", "&, |, ^, ~, <<, >> execute direct CPU-level bit manipulation"),
        ("Encapsulation", "BitwiseLab class provides pure member functions for logic gates"),
        ("Character Transformation", "inverts bit characters '0' <-> '1' for 1's complement"),
        ("Two's Complement Logic", "adds binary '1' to 1's complement for signed integer modeling")
    ]
    mod3_code = (
        "class BitwiseLab {\n"
        "public:\n"
        "  int bitwiseAND(int a, int b) { return a & b; }\n"
        "  int bitwiseXOR(int a, int b) { return a ^ b; }\n"
        "  string onesComplement(string bin) {\n"
        "    for (char &c : bin) c = (c == '0') ? '1' : '0';\n"
        "    return bin;\n"
        "  }\n"
        "  string twosComplement(string bin) {\n"
        "    return addBinary(onesComplement(bin), \"1\");\n"
        "  }\n"
        "};"
    )
    mod3_output = [
        "-- Bitwise & Complement Suite --",
        "Input A: 12 (1100), Input B: 10 (1010)",
        "Bitwise AND (A & B) : 8 (1000)",
        "Bitwise XOR (A ^ B) : 6 (0110)",
        "1's Complement of A : 0011",
        "2's Complement of A : 0100 (-12 signed)"
    ]
    add_module_slide(prs, 3, "Bitwise Manipulation & Complements", mod3_what, mod3_cpp, mod3_code, mod3_output)

    # =========================================================================
    # SLIDE 7: MODULE 4 — Advanced Math (Trig & Log Suite)
    # =========================================================================
    mod4_what = (
        "Extends integer base conversions with high-precision scientific math, "
        "evaluating all 6 trigonometric ratios and computing arbitrary-base "
        "logarithmic equations."
    )
    mod4_cpp = [
        ("<cmath> Integration", "utilizes sin(), cos(), tan(), log(), log10() standard functions"),
        ("Type Conversion", "converts degree angles to radians using M_PI constant"),
        ("Change-of-Base Formula", "computes log_b(x) = ln(x) / ln(b) for non-standard bases"),
        ("Domain Validation", "guards against invalid inputs like log(x <= 0) or base <= 1")
    ]
    mod4_code = (
        "#include <cmath>\n"
        "class MathSuite {\n"
        "public:\n"
        "  double trigCalc(string func, double deg) {\n"
        "    double rad = deg * (M_PI / 180.0);\n"
        "    if (func == \"sin\") return sin(rad);\n"
        "    if (func == \"cos\") return cos(rad);\n"
        "    if (func == \"tan\") return tan(rad);\n"
        "    return 0.0;\n"
        "  }\n"
        "  double customLog(double base, double val) {\n"
        "    if (val <= 0 || base <= 1) return -1.0;\n"
        "    return log(val) / log(base);\n"
        "  }\n"
        "};"
    )
    mod4_output = [
        "-- Advanced Math Suite Output --",
        "Angle: 30.00° -> sin(30°) = 0.5000, cos(30°) = 0.8660",
        "Logarithm Suite:",
        "log2(256)   = 8.0000",
        "log10(1000) = 3.0000",
        "log5(125)   = 3.0000 (Custom Base)",
        "Calculations verified successfully."
    ]
    add_module_slide(prs, 4, "Advanced Math (Trig & Log Suite)", mod4_what, mod4_cpp, mod4_code, mod4_output)

    # =========================================================================
    # SLIDE 8: THANK YOU SLIDE (Exact Reference Layout)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    bg8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg8.fill.solid()
    bg8.fill.fore_color.rgb = NAVY_DARK
    bg8.line.color.rgb = NAVY_DARK

    # Top-left small decorative square
    sq8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.3), Inches(0.45), Inches(0.45))
    sq8.fill.solid()
    sq8.fill.fore_color.rgb = RGBColor(219, 234, 254)
    sq8.line.fill.background()

    # Right circular graphic
    outer_circ8 = s8.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.8), Inches(1.5), Inches(4.5), Inches(4.5))
    outer_circ8.fill.solid()
    outer_circ8.fill.fore_color.rgb = RGBColor(23, 33, 75)
    outer_circ8.line.fill.background()

    inner_circ8 = s8.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.5), Inches(2.2), Inches(3.1), Inches(3.1))
    inner_circ8.fill.solid()
    inner_circ8.fill.fore_color.rgb = RGBColor(255, 255, 255)
    inner_circ8.line.fill.background()

    itf8 = inner_circ8.text_frame
    itf8.vertical_anchor = MSO_ANCHOR.MIDDLE
    ip8 = itf8.paragraphs[0]
    ip8.text = "🔢"
    ip8.font.size = Pt(48)
    ip8.alignment = PP_ALIGN.CENTER

    # Thank you text
    th_box = s8.shapes.add_textbox(Inches(0.9), Inches(2.7), Inches(8.5), Inches(2.2))
    th_tf = th_box.text_frame
    th_tf.word_wrap = True
    th_p = th_tf.paragraphs[0]
    th_p.text = "THANK YOU"
    th_p.font.name = "Calibri"
    th_p.font.size = Pt(36)
    th_p.font.bold = True
    th_p.font.color.rgb = TEXT_LIGHT

    th_sub = th_tf.add_paragraph()
    th_sub.text = "We appreciate your time and attention — questions are welcome"
    th_sub.font.name = "Calibri"
    th_sub.font.size = Pt(16)
    th_sub.font.italic = True
    th_sub.font.color.rgb = RGBColor(203, 213, 225)
    th_sub.space_before = Pt(8)

    prs.save(output_path)
    print(f"Exact reference PPT saved successfully to: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Review_2_Number_System_Toolkit_Standard.pptx")
    build_exact_reference_ppt(out_file)
