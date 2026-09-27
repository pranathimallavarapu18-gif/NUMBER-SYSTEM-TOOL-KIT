import sys
import os
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_cornerstone_presentation(output_path, logo_path_banner, logo_path_corner):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Exact Color Palette matching the Aditya Cornerstone reference PPT
    NAVY_TITLE   = RGBColor(27, 42, 95)      # #1B2A5F Dark Navy for Titles
    SUBTITLE_TXT = RGBColor(71, 85, 105)     # #475569 Slate for subtitles
    TEXT_DARK    = RGBColor(15, 23, 42)      # #0F172A Main text
    TEXT_MUTED   = RGBColor(100, 116, 139)   # #64748B Muted text
    CARD_BG      = RGBColor(248, 250, 252)   # #F8FAFC Soft grey card
    CARD_BORDER  = RGBColor(226, 232, 240)   # #E2E8F0 Card border
    ACCENT_BLUE  = RGBColor(37, 99, 235)     # #2563EB Royal Blue accent
    ACCENT_LINE  = RGBColor(30, 58, 138)     # #1E3A8A Dark blue left bar
    WHITE        = RGBColor(255, 255, 255)
    STEP_NUM_BG  = RGBColor(30, 42, 95)

    def add_corner_logo(slide):
        if os.path.exists(logo_path_corner):
            slide.shapes.add_picture(logo_path_corner, Inches(8.40), Inches(0.22), Inches(4.63), Inches(0.74))

    def add_slide_header(slide, title_text, subtitle_text=None):
        add_corner_logo(slide)

        # Title
        tb = slide.shapes.add_textbox(Inches(0.70), Inches(0.40), Inches(7.5), Inches(0.65))
        tf = tb.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Aptos Display"
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = NAVY_TITLE

        # Subtitle
        if subtitle_text:
            tb_sub = slide.shapes.add_textbox(Inches(0.72), Inches(1.08), Inches(11.20), Inches(0.40))
            tf_sub = tb_sub.text_frame
            tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.name = "Aptos"
            p_sub.font.size = Pt(12)
            p_sub.font.color.rgb = SUBTITLE_TXT

    def add_page_number(slide, num_str):
        tb = slide.shapes.add_textbox(Inches(12.45), Inches(7.05), Inches(0.60), Inches(0.25))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = num_str
        p.font.name = "Aptos"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)

    # Top Banner Logo
    if os.path.exists(logo_path_banner):
        s1.shapes.add_picture(logo_path_banner, Inches(0.6), Inches(0.20), Inches(12.13), Inches(1.55))

    # Top Category Subheading
    sub_top = s1.shapes.add_textbox(Inches(0.6), Inches(1.85), Inches(12.13), Inches(0.45))
    st_tf = sub_top.text_frame
    st_p = st_tf.paragraphs[0]
    st_p.text = "OOP through C++ CORNERSTONE PROJECT          NUMBER SYSTEM TOOLKIT          REVIEW - 2"
    st_p.font.name = "Aptos"
    st_p.font.size = Pt(12)
    st_p.font.bold = True
    st_p.font.color.rgb = NAVY_TITLE

    # Horizontal Divider Line
    line1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(2.25), Inches(12.13), Inches(0.02))
    line1.fill.solid()
    line1.fill.fore_color.rgb = CARD_BORDER
    line1.line.fill.background()

    # Left Column: Team & Guide
    left_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(2.45), Inches(5.6), Inches(4.7))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = CARD_BORDER

    ltf = left_card.text_frame
    ltf.margin_left = ltf.margin_right = Inches(0.3)
    ltf.margin_top = Inches(0.25)

    p = ltf.paragraphs[0]
    p.text = "Team Members –   Batch- 04 (Data Science)"
    p.font.name = "Aptos"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    p.space_after = Pt(8)

    members = [
        ("25B11DS349", "M. Lakshmi Srinivas"),
        ("25B11DS127", "D. Varaprasad"),
        ("25B11DS370", "N. Akhila Devi"),
        ("25B11DS628", "Y. Nithya Sree"),
        ("25B11DS320", "M. Venkata Pranathi")
    ]
    for roll, name in members:
        mp = ltf.add_paragraph()
        mp.text = f"{roll}   –   {name}"
        mp.font.name = "Aptos"
        mp.font.size = Pt(11.5)
        mp.font.color.rgb = TEXT_DARK
        mp.space_after = Pt(3)

    ci_head = ltf.add_paragraph()
    ci_head.text = "\nCourse Instructor :"
    ci_head.font.name = "Aptos"
    ci_head.font.size = Pt(12)
    ci_head.font.bold = True
    ci_head.font.color.rgb = NAVY_TITLE

    ci_name = ltf.add_paragraph()
    ci_name.text = "Dr. KARNAM SREENU"
    ci_name.font.name = "Aptos"
    ci_name.font.size = Pt(11.5)
    ci_name.font.bold = True
    ci_name.font.color.rgb = TEXT_DARK

    ci_dept = ltf.add_paragraph()
    ci_dept.text = "ASSISTANT PROFESSOR, DEPT. OF CSE (DATA SCIENCE)"
    ci_dept.font.name = "Aptos"
    ci_dept.font.size = Pt(10)
    ci_dept.font.color.rgb = SUBTITLE_TXT

    # Right Column: Project Overview & Modules List matching website exactly
    right_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.5), Inches(2.45), Inches(6.23), Inches(4.7))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = CARD_BG
    right_card.line.color.rgb = CARD_BORDER

    rtf = right_card.text_frame
    rtf.margin_left = rtf.margin_right = Inches(0.35)
    rtf.margin_top = Inches(0.20)

    rp0 = rtf.paragraphs[0]
    rp0.text = "NUMBER SYSTEM TOOLKIT"
    rp0.font.name = "Aptos Display"
    rp0.font.size = Pt(16.5)
    rp0.font.bold = True
    rp0.font.color.rgb = NAVY_TITLE

    rp_sub = rtf.add_paragraph()
    rp_sub.text = "C++ & Web Platform for Base Conversions, Logic Gates & Advanced Math"
    rp_sub.font.name = "Aptos"
    rp_sub.font.size = Pt(10.5)
    rp_sub.font.color.rgb = SUBTITLE_TXT
    rp_sub.space_after = Pt(8)

    mod_head = rtf.add_paragraph()
    mod_head.text = "MODULES (As in Toolkit Suite)"
    mod_head.font.name = "Aptos"
    mod_head.font.size = Pt(12)
    mod_head.font.bold = True
    mod_head.font.color.rgb = ACCENT_BLUE
    mod_head.space_after = Pt(4)

    modules_website = [
        "🔄  Live Multi-Converter (Dec, Bin, Oct, Hex, Custom Radix, ASCII)",
        "🪜  Step-by-Step Solver (Division & Positional Expansion)",
        "🧮  Decimal Arithmetic Module",
        "⚡  Binary Arithmetic Module (+, -, *, /)",
        "🔍  Number Validator Module",
        "🎛️  Interactive Bit Board (8-Bit Switchboard)",
        "📐  Trigonometry Lab (All 6 Ratios & Dynamic Unit Circle)",
        "📉  Logarithm Suite (ln, log10, log2, Arbitrary Base log_b)",
        "📊  Cheat Sheet & Tables (Powers of 2 & Multi-Base Matrix)",
        "🎯  Practice & Quiz (Interactive Challenge Hub)"
    ]
    for m in modules_website:
        mp = rtf.add_paragraph()
        mp.text = m
        mp.font.name = "Aptos"
        mp.font.size = Pt(10)
        mp.font.color.rgb = TEXT_DARK
        mp.space_after = Pt(1.5)

    add_page_number(s1, "01")

    # =========================================================================
    # SLIDE 2: ABSTRACT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "ABSTRACT")

    ab_card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.70), Inches(1.6), Inches(11.93), Inches(5.0))
    ab_card.fill.solid()
    ab_card.fill.fore_color.rgb = CARD_BG
    ab_card.line.color.rgb = CARD_BORDER

    ab_tf = ab_card.text_frame
    ab_tf.margin_left = ab_tf.margin_right = Inches(0.4)
    ab_tf.margin_top = Inches(0.35)

    abstract_paragraphs = [
        "The Number System Toolkit is a C++ and web application for managing multi-base conversions, digital logic operations, and advanced mathematical computations.",
        "It features a Live Multi-Converter supporting Decimal, Binary, Octal, Hexadecimal, ASCII and Custom Radix (2 to 36) with real-time bidirectional synchronization.",
        "A Step-by-Step Solver automates repeated division and positional power expansions to generate mathematical proofs for students.",
        "It provides Binary & Decimal Arithmetic, Number Validation, an Interactive Bit Board, Trigonometry Lab (unit circle canvas), and a Logarithm Suite.",
        "The project demonstrates structured data management, OOP principles, string manipulation, input validation, and interactive visualization."
    ]

    for idx, text_p in enumerate(abstract_paragraphs):
        p = ab_tf.paragraphs[0] if idx == 0 else ab_tf.add_paragraph()
        p.text = f"•   {text_p}"
        p.font.name = "Aptos"
        p.font.size = Pt(13.5)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(16)

    add_page_number(s2, "02")

    # =========================================================================
    # SLIDE 3: PROJECT PURPOSE & SCOPE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Project Purpose & Scope", "What the system manages and who it is designed to support")

    cards_scope = [
        ("Number Systems Hub", "Manages Live Multi-Converter, Step-by-Step Solver, Decimal & Binary Arithmetic, and Number Validator with strict radix character validation."),
        ("Interactive Bit Board & Gates", "Provides an 8-bit clickable switchboard to visualize bit toggles, bitwise logic gates (AND, OR, XOR, NOT, Shifts), and 1's/2's complements in real time."),
        ("Advanced Math & Practice", "Features the Trigonometry Lab (unit circle canvas), Logarithm Suite (arbitrary base change), Cheat Sheet Tables, and Practice Quiz.")
    ]

    for i, (title, desc) in enumerate(cards_scope):
        left_pos = 0.72 + i * 4.03
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left_pos), Inches(1.75), Inches(3.85), Inches(3.95))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER

        bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left_pos), Inches(1.75), Inches(0.08), Inches(3.95))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_LINE
        bar.line.fill.background()

        ctf = card.text_frame
        ctf.margin_left = Inches(0.25)
        ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)

        cp = ctf.paragraphs[0]
        cp.text = title
        cp.font.name = "Aptos"
        cp.font.size = Pt(15.5)
        cp.font.bold = True
        cp.font.color.rgb = NAVY_TITLE
        cp.space_after = Pt(12)

        dp = ctf.add_paragraph()
        dp.text = desc
        dp.font.name = "Aptos"
        dp.font.size = Pt(12.5)
        dp.font.color.rgb = TEXT_DARK

    core_box = s3.shapes.add_textbox(Inches(0.75), Inches(6.0), Inches(11.70), Inches(0.55))
    ctf = core_box.text_frame
    cp = ctf.paragraphs[0]
    cp.text = "Core objective: keep numerical calculations structured, validated, educational, and persistent in a simple application."
    cp.font.name = "Aptos"
    cp.font.size = Pt(13.5)
    cp.font.bold = True
    cp.font.color.rgb = NAVY_TITLE

    add_page_number(s3, "03")

    # =========================================================================
    # SLIDE 4: DATA TYPES & VALIDATION
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Data Types & Validation", "Each field uses a type that matches the kind of information it stores")

    table_shape = s4.shapes.add_table(9, 3, Inches(0.70), Inches(1.65), Inches(11.93), Inches(4.8))
    table = table_shape.table
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(2.0)
    table.columns[2].width = Inches(7.33)

    headers = ["FIELD", "DATA TYPE", "VALIDATION / EXAMPLE"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_TITLE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Aptos"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE

    rows_data = [
        ("Input Number", "string", "Validated against radix digit set (e.g. '0-1' for Base 2, '0-F' for Base 16)"),
        ("Custom Radix", "int", "Range: 2 to 36 (Base 3 to Base 36)"),
        ("Decimal Integer", "long long", "Non-negative integer for arithmetic and multi-base processing"),
        ("Binary String", "string", "Characters strictly '0' and '1' with arbitrary bit-widths"),
        ("Bit Board Register", "uint8_t / string", "8-bit unsigned integer / binary toggle switches (0 to 255)"),
        ("Angle (θ)", "double", "Floating-point angle in Degrees (0°–360°) or Radians"),
        ("Logarithm Input", "double", "Positive real number (x > 0); rejects non-positive values"),
        ("Logarithm Base", "double", "Positive real number (base > 0, base != 1)")
    ]

    for row_idx, row in enumerate(rows_data):
        for col_idx, val in enumerate(row):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(248, 250, 252) if row_idx % 2 == 0 else RGBColor(241, 245, 249)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Aptos"
            p.font.size = Pt(11)
            p.font.bold = (col_idx < 2)
            p.font.color.rgb = NAVY_TITLE if col_idx == 0 else (ACCENT_BLUE if col_idx == 1 else TEXT_DARK)

    note_box = s4.shapes.add_textbox(Inches(0.75), Inches(6.65), Inches(11.60), Inches(0.35))
    ntf = note_box.text_frame
    np = ntf.paragraphs[0]
    np.text = "Note: Numbers are handled as strings to support arbitrary bit-lengths and alphanumeric custom bases without overflow."
    np.font.name = "Aptos"
    np.font.size = Pt(11)
    np.font.italic = True
    np.font.color.rgb = SUBTITLE_TXT

    add_page_number(s4, "04")

    # =========================================================================
    # SLIDE 5: CONVERSION & PROCESSING FLOW
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Conversion & Processing Flow", "Input details are entered, validated and converted through mathematical algorithms")

    steps_data = [
        ("1", "Live Input", "User enters value in Dec, Bin, Oct, Hex, or Custom Base"),
        ("2", "Validator", "Checks digits against selected base constraints"),
        ("3", "Base-10 Engine", "Positional expansion: sum of (digit * base^i)"),
        ("4", "Radix Generator", "Repeated modulus division & remainder collection"),
        ("5", "Step Output", "Updates all fields + renders Step-by-Step Solver")
    ]

    for i, (num_str, title, desc) in enumerate(steps_data):
        left_pos = 0.70 + i * 2.42
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left_pos), Inches(1.85), Inches(2.28), Inches(3.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER

        bar = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left_pos), Inches(1.85), Inches(0.06), Inches(3.2))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_LINE
        bar.line.fill.background()

        badge = s5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left_pos + 0.15), Inches(2.0), Inches(0.38), Inches(0.38))
        badge.fill.solid()
        badge.fill.fore_color.rgb = STEP_NUM_BG
        badge.line.fill.background()
        btf = badge.text_frame
        bp = btf.paragraphs[0]
        bp.text = num_str
        bp.font.name = "Aptos"
        bp.font.size = Pt(11)
        bp.font.bold = True
        bp.font.color.rgb = WHITE
        bp.alignment = PP_ALIGN.CENTER

        ctf = card.text_frame
        ctf.margin_left = Inches(0.18)
        ctf.margin_top = Inches(0.65)
        ctf.margin_right = Inches(0.15)

        tp = ctf.paragraphs[0]
        tp.text = title
        tp.font.name = "Aptos"
        tp.font.size = Pt(13)
        tp.font.bold = True
        tp.font.color.rgb = NAVY_TITLE
        tp.space_after = Pt(8)

        dp = ctf.add_paragraph()
        dp.text = desc
        dp.font.name = "Aptos"
        dp.font.size = Pt(11)
        dp.font.color.rgb = TEXT_DARK

    b1 = s5.shapes.add_textbox(Inches(0.70), Inches(5.35), Inches(11.93), Inches(0.65))
    b1_tf = b1.text_frame
    p1 = b1_tf.paragraphs[0]
    p1.text = "NUMBER VALIDATOR: Rejects invalid characters (e.g. '8' in Octal, '2' in Binary, negative radix)."
    p1.font.name = "Aptos"
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = NAVY_TITLE

    p2 = b1_tf.add_paragraph()
    p2.text = "LIVE MULTI-CONVERTER: Decimal (10)  |  Binary (2)  |  Octal (8)  |  Hex (16)  |  Custom Radix (2–36)  |  ASCII"
    p2.font.name = "Aptos"
    p2.font.size = Pt(12)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_before = Pt(4)

    add_page_number(s5, "05")

    # =========================================================================
    # SLIDE 6: ARITHMETIC & INTERACTIVE BIT BOARD
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "Arithmetic & Interactive Bit Board Modules", "Binary calculations, Decimal arithmetic, and bit manipulation handled efficiently")

    modules_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.70), Inches(1.65), Inches(11.93), Inches(5.0))
    modules_box.fill.solid()
    modules_box.fill.fore_color.rgb = CARD_BG
    modules_box.line.color.rgb = CARD_BORDER

    mtf = modules_box.text_frame
    mtf.margin_left = mtf.margin_right = Inches(0.35)
    mtf.margin_top = Inches(0.22)

    sections = [
        ("1. Binary & Decimal Arithmetic", "• Binary Arithmetic: Enter Binary A & B → (+, -, *, /) with carry/borrow propagation.\n• Decimal Arithmetic: Standard arithmetic operations with automatic base synchronization."),
        ("2. Interactive Bit Board", "• Clickable 8-Bit switchboard with individual toggle switches (Bit 7 to Bit 0).\n• Displays simultaneous Decimal, Hexadecimal, and ASCII character representations in real time."),
        ("3. Bitwise Logic & Complements", "• Bitwise Operators: AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), Right Shift (>>).\n• Complements: 1's Complement (inverting bits) and 2's Complement (signed negative integer representation)."),
        ("Example Output", "• Binary Addition: 10110 + 01101 = 100011 (Decimal 22 + 13 = 35)\n• Bitwise XOR: 12 ^ 10 = 6 (1100 ^ 1010 = 0110) | 2's Complement of 12 (00001100) = 11110100 (-12)")
    ]

    for idx, (title, desc) in enumerate(sections):
        p_t = mtf.paragraphs[0] if idx == 0 else mtf.add_paragraph()
        p_t.text = title
        p_t.font.name = "Aptos"
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = NAVY_TITLE
        p_t.space_before = Pt(6) if idx > 0 else Pt(0)
        p_t.space_after = Pt(2)

        for line in desc.split('\n'):
            p_d = mtf.add_paragraph()
            p_d.text = line
            p_d.font.name = "Aptos"
            p_d.font.size = Pt(10.5)
            p_d.font.color.rgb = TEXT_DARK
            p_d.space_after = Pt(1.5)

    add_page_number(s6, "06")

    # =========================================================================
    # SLIDE 7: IMPLEMENTATION
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "IMPLEMENTATION")

    imp_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.70), Inches(1.6), Inches(11.93), Inches(5.1))
    imp_card.fill.solid()
    imp_card.fill.fore_color.rgb = CARD_BG
    imp_card.line.color.rgb = CARD_BORDER

    itf = imp_card.text_frame
    itf.margin_left = itf.margin_right = Inches(0.4)
    itf.margin_top = Inches(0.3)

    imp_items = [
        ("Language", "C++ (C++17 Standard) & Modern Client-Side Web Architecture"),
        ("Input/Output", "cin and cout (Console Engine) + Reactive Web Application GUI"),
        ("Data structures", "classes (NumberSystem, BitwiseLab, MathSuite), strings, vectors, arrays"),
        ("Validation", "Number Validator checks radix limits (2-36), character bounds, and log domains (x > 0, base != 1)"),
        ("Operations", "Live Multi-Converter, Step-by-Step Solver, Binary/Decimal Arithmetic, Bit Board, Complements"),
        ("Analysis", "repeated division tables, positional expansion equations, dynamic HTML5 Canvas Unit Circle visualizer"),
        ("Persistence", "modular C++ class structure, interactive browser state, Cheat Sheets & Practice Quiz")
    ]

    for idx, (lbl, val) in enumerate(imp_items):
        p = itf.paragraphs[0] if idx == 0 else itf.add_paragraph()
        p.text = f"{lbl}:  {val}"
        p.font.name = "Aptos"
        p.font.size = Pt(13)
        p.font.bold = False
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    add_page_number(s7, "07")

    # =========================================================================
    # SLIDE 8: ADVANCED MATH (TRIGONOMETRY & LOGARITHM SUITE)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "Advanced Math Modules", "Trigonometry Lab and Logarithm Suite extending digital computation")

    cards_math = [
        ("Trigonometry Lab", [
            "Evaluates all 6 trigonometric ratios:",
            "  sin(θ), cos(θ), tan(θ), csc(θ), sec(θ), cot(θ)",
            "Dual angle modes: Degrees (°) & Radians (rad).",
            "Interactive HTML5 2D Canvas Unit Circle:",
            "  - Dynamic angle ray with drag & slider.",
            "  - Live projection coordinates: x = cos(θ), y = sin(θ).",
            "Safely handles undefined asymptotes (tan 90°, cot 0°)."
        ]),
        ("Logarithm Suite", [
            "Natural Logarithm: ln(x) with base e.",
            "Common Logarithm: log10(x).",
            "Binary Logarithm: log2(x) for complexity analysis.",
            "Arbitrary base change formula:",
            "  log_b(x) = ln(x) / ln(b)",
            "High-precision floating point evaluators.",
            "Domain protection (rejects x <= 0, base <= 1)."
        ]),
        ("Reference & Practice", [
            "Cheat Sheet & Tables:",
            "  - Powers of 2 Table (2^0 to 2^16).",
            "  - 0–15 Multi-Base Equivalence Matrix.",
            "  - Standard Angle Trigonometric Table.",
            "Practice & Quiz Module:",
            "  - 3 Difficulty tiers (Easy, Medium, Hard).",
            "  - Live score counter and step explanations."
        ])
    ]

    for i, (title, items) in enumerate(cards_math):
        left_pos = 0.72 + i * 4.03
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left_pos), Inches(1.75), Inches(3.85), Inches(4.85))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER

        bar = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left_pos), Inches(1.75), Inches(0.08), Inches(4.85))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_LINE
        bar.line.fill.background()

        ctf = card.text_frame
        ctf.margin_left = Inches(0.22)
        ctf.margin_right = Inches(0.18)
        ctf.margin_top = Inches(0.2)

        cp = ctf.paragraphs[0]
        cp.text = title
        cp.font.name = "Aptos"
        cp.font.size = Pt(15)
        cp.font.bold = True
        cp.font.color.rgb = NAVY_TITLE
        cp.space_after = Pt(8)

        for itm in items:
            p = ctf.add_paragraph()
            p.text = f"• {itm}" if not itm.startswith("  ") else f"    {itm.strip()}"
            p.font.name = "Aptos"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(3)

    add_page_number(s8, "08")

    # =========================================================================
    # SLIDE 9: STEP-BY-STEP SOLVER & CHEAT SHEETS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "Step-by-Step Solver & Cheat Sheets", "The same numerical records can be viewed at different analytical scopes")

    cards_disp = [
        ("Step-by-Step Solver", [
            "• Repeated Modulus Division Table (Quotient, Remainder, Direction)",
            "• Positional Expansion Breakdown: sum(d_i * base^i)",
            "• Full-Adder Carry Simulation for Binary Sums",
            "• Change-of-Base Logarithmic Equation Proof",
            "• Dynamic equation rendering on the fly"
        ]),
        ("Cheat Sheet & Tables", [
            "• Powers of 2 Lookup Table (2^0 to 2^16)",
            "• 0–15 Base Equivalence Reference Matrix",
            "• ASCII Character Code mapping",
            "• Standard Angle Trigonometry values",
            "• Logarithmic identities quick lookup"
        ]),
        ("Practice & Quiz Hub", [
            "• Interactive Challenge Quiz generator",
            "• 3 difficulty levels (Easy, Medium, Hard)",
            "• Instant automated score & streak tracking",
            "• Detailed solution breakdown for learners",
            "• Execution time < 1ms across all modules"
        ])
    ]

    for i, (title, items) in enumerate(cards_disp):
        left_pos = 0.72 + i * 4.03
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left_pos), Inches(1.75), Inches(3.85), Inches(4.1))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER

        bar = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left_pos), Inches(1.75), Inches(0.08), Inches(4.1))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_LINE
        bar.line.fill.background()

        ctf = card.text_frame
        ctf.margin_left = Inches(0.22)
        ctf.margin_right = Inches(0.18)
        ctf.margin_top = Inches(0.2)

        cp = ctf.paragraphs[0]
        cp.text = title
        cp.font.name = "Aptos"
        cp.font.size = Pt(15)
        cp.font.bold = True
        cp.font.color.rgb = NAVY_TITLE
        cp.space_after = Pt(8)

        for itm in items:
            p = ctf.add_paragraph()
            p.text = itm
            p.font.name = "Aptos"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(3)

    foot_box = s9.shapes.add_textbox(Inches(0.75), Inches(6.15), Inches(11.70), Inches(0.40))
    ftf = foot_box.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "Filtering and step generation are dynamic: intermediate calculations and derivations are rendered on the fly."
    fp.font.name = "Aptos"
    fp.font.size = Pt(12)
    fp.font.italic = True
    fp.font.color.rgb = SUBTITLE_TXT

    add_page_number(s9, "09")

    # =========================================================================
    # SLIDE 10: SYSTEM WORKFLOW & TAKEAWAY
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_header(s10, "System Workflow & Takeaway", "A single application connects input data, base conversions, arithmetic and mathematical analysis.")

    pipe_steps = [
        ("01", "Live Input"),
        ("02", "Validator"),
        ("03", "Core Engine"),
        ("04", "Step Solver"),
        ("05", "Visual Output")
    ]
    for idx, (num_s, title_s) in enumerate(pipe_steps):
        left_pos = 0.70 + idx * 2.45
        box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left_pos), Inches(1.75), Inches(1.95), Inches(1.15))
        box.fill.solid()
        box.fill.fore_color.rgb = NAVY_TITLE
        box.line.fill.background()

        btf = box.text_frame
        btf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p0 = btf.paragraphs[0]
        p0.text = num_s
        p0.font.name = "Aptos"
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = WHITE
        p0.alignment = PP_ALIGN.CENTER

        p1 = btf.add_paragraph()
        p1.text = title_s
        p1.font.name = "Aptos"
        p1.font.size = Pt(11)
        p1.font.color.rgb = RGBColor(226, 232, 240)
        p1.alignment = PP_ALIGN.CENTER

        if idx < 4:
            arr = s10.shapes.add_textbox(Inches(left_pos + 1.95), Inches(2.05), Inches(0.50), Inches(0.50))
            atf = arr.text_frame
            ap = atf.paragraphs[0]
            ap.text = "→"
            ap.font.name = "Aptos"
            ap.font.size = Pt(20)
            ap.font.bold = True
            ap.font.color.rgb = ACCENT_BLUE
            ap.alignment = PP_ALIGN.CENTER

    low_card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.70), Inches(3.2), Inches(11.93), Inches(3.55))
    low_card.fill.solid()
    low_card.fill.fore_color.rgb = CARD_BG
    low_card.line.color.rgb = CARD_BORDER

    ltf = low_card.text_frame
    ltf.margin_left = ltf.margin_right = Inches(0.35)
    ltf.margin_top = Inches(0.2)

    hp1 = ltf.paragraphs[0]
    hp1.text = "What the project demonstrates"
    hp1.font.name = "Aptos"
    hp1.font.size = Pt(14)
    hp1.font.bold = True
    hp1.font.color.rgb = NAVY_TITLE
    hp1.space_after = Pt(6)

    demo_items = [
        "C++ classes, modular methods, and OOP encapsulation",
        "Live Multi-Converter & Step-by-Step Solver algorithms",
        "Binary & Decimal Arithmetic engines and interactive Bit Board",
        "Trigonometry Lab with dynamic HTML5 Canvas Unit Circle",
        "Logarithm Suite, Cheat Sheets, and Practice Quiz Hub"
    ]
    for d in demo_items:
        dp = ltf.add_paragraph()
        dp.text = f"•  {d}"
        dp.font.name = "Aptos"
        dp.font.size = Pt(11)
        dp.font.color.rgb = TEXT_DARK
        dp.space_after = Pt(2)

    tk_head = ltf.add_paragraph()
    tk_head.text = "\nKey Takeaway"
    tk_head.font.name = "Aptos"
    tk_head.font.size = Pt(13)
    tk_head.font.bold = True
    tk_head.font.color.rgb = NAVY_TITLE
    tk_head.space_after = Pt(2)

    tk_p = ltf.add_paragraph()
    tk_p.text = "Structured numerical data + multi-base conversion + arithmetic + bitwise logic + advanced math, organized in a unified toolkit."
    tk_p.font.name = "Aptos"
    tk_p.font.size = Pt(11.5)
    tk_p.font.bold = True
    tk_p.font.color.rgb = ACCENT_BLUE

    add_page_number(s10, "10")

    # =========================================================================
    # SLIDE 11: CONCLUSION
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_slide_header(s11, "CONCLUSION")

    c_card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.70), Inches(1.6), Inches(11.93), Inches(5.0))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = CARD_BG
    c_card.line.color.rgb = CARD_BORDER

    ctf = c_card.text_frame
    ctf.margin_left = ctf.margin_right = Inches(0.4)
    ctf.margin_top = Inches(0.35)

    conclusion_points = [
        "The Number System Toolkit unifies base conversions, arithmetic, bitwise logic, and advanced mathematics into a single platform.",
        "It provides a clear workflow: Live Multi-Converter, Step-by-Step Solver, Decimal/Binary Arithmetic, Bit Board, Trigonometry Lab, and Logarithm Suite.",
        "The project demonstrates practical application of C++ OOP classes, vectors, validation, string algorithms, <cmath> functions, and interactive web visualization.",
        "The system serves as a powerful educational toolkit for students learning Digital Logic Design (DLD) and computer architecture."
    ]

    for idx, cp_text in enumerate(conclusion_points):
        p = ctf.paragraphs[0] if idx == 0 else ctf.add_paragraph()
        p.text = f"•   {cp_text}"
        p.font.name = "Aptos"
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(18)

    add_page_number(s11, "11")

    # =========================================================================
    # SLIDE 12: THANK YOU
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_corner_logo(s12)

    th_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.8), Inches(10.33), Inches(4.5))
    th_card.fill.solid()
    th_card.fill.fore_color.rgb = CARD_BG
    th_card.line.color.rgb = CARD_BORDER

    th_tf = th_card.text_frame
    th_tf.margin_top = Inches(0.8)

    p0 = th_tf.paragraphs[0]
    p0.text = "THANK YOU 🔢"
    p0.font.name = "Aptos Display"
    p0.font.size = Pt(40)
    p0.font.bold = True
    p0.font.color.rgb = NAVY_TITLE
    p0.alignment = PP_ALIGN.CENTER

    p1 = th_tf.add_paragraph()
    p1.text = "NUMBER SYSTEM & MATH TOOLKIT"
    p1.font.name = "Aptos"
    p1.font.size = Pt(18)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_BLUE
    p1.alignment = PP_ALIGN.CENTER
    p1.space_before = Pt(8)

    p2 = th_tf.add_paragraph()
    p2.text = "We appreciate your time and attention — questions are welcome"
    p2.font.name = "Aptos"
    p2.font.size = Pt(14)
    p2.font.italic = True
    p2.font.color.rgb = SUBTITLE_TXT
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(12)

    p3 = th_tf.add_paragraph()
    p3.text = "Department of Computer Science & Engineering (Data Science) · Aditya University"
    p3.font.name = "Aptos"
    p3.font.size = Pt(11.5)
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(20)

    prs.save(output_path)
    print(f"Cornerstone presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Number_System_Toolkit_Review2_Updated.pptx")
    banner = os.path.join(out_dir, "extracted_assets", "img_slide_1_object 2.jpg")
    corner = os.path.join(out_dir, "extracted_assets", "img_slide_2_Picture 19.png")
    build_cornerstone_presentation(out_file, banner, corner)
