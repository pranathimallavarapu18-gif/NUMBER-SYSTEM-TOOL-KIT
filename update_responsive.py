import re
import os

html_path = r'C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit\index.html'
styles_path = r'C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit\styles.css'
script_path = r'C:\Users\pranathi\.gemini\antigravity\scratch\number-system-toolkit\script.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update Responsive CSS Rules
responsive_css_additions = """
/* =========================================================
   ENHANCED RESPONSIVE STYLES & TOUCH OPTIMIZATIONS
   ========================================================= */

/* Backdrop overlay for mobile drawer */
.sidebar-backdrop {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 998;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease;
}

.sidebar-backdrop.show {
    opacity: 1;
    pointer-events: auto;
}

.sidebar-close-btn {
    display: none;
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 1.5rem;
    cursor: pointer;
    margin-left: auto;
    padding: 0.25rem 0.5rem;
    border-radius: var(--radius-sm);
    line-height: 1;
}

.sidebar-close-btn:hover {
    color: var(--text-primary);
    background: var(--bg-card-hover);
}

/* Canvas Responsive Sizing */
.canvas-wrapper canvas {
    max-width: 100%;
    height: auto;
    display: block;
}

/* Responsive Table Wrapper */
.table-responsive {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin-bottom: 1rem;
}

.data-table {
    min-width: 480px;
}

/* Prevent overflow in code/formula output */
.arithmetic-step-box, .step-output-container, .val-char-stream, .binary-formatted {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    word-break: break-all;
    overflow-wrap: break-word;
}

/* Responsive Breakpoints */
@media (max-width: 1200px) {
    .tables-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 1024px) {
    .trig-layout-grid, .log-calculator-grid {
        grid-template-columns: 1fr;
    }
    .secondary-converters {
        grid-template-columns: 1fr;
    }
    .info-grid-card {
        grid-template-columns: repeat(2, 1fr);
    }
    .step-controls {
        grid-template-columns: 1fr;
    }
    .form-row {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 768px) {
    .sidebar {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: min(300px, 85vw);
        transform: translateX(-100%);
        box-shadow: none;
        z-index: 1000;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }

    .sidebar.open {
        transform: translateX(0);
        box-shadow: 12px 0 35px rgba(0, 0, 0, 0.6);
    }

    .sidebar-backdrop {
        display: block;
    }

    .sidebar-close-btn {
        display: inline-flex;
    }

    .mobile-menu-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }

    .main-content {
        padding: 1rem 1rem 2.5rem 1rem;
        max-width: 100%;
    }

    .top-header {
        margin-bottom: 1.25rem;
        padding-bottom: 0.85rem;
    }

    .card-header, .card-body {
        padding: 1.15rem;
    }

    .converter-grid {
        grid-template-columns: 1fr;
    }

    .trig-results-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .quiz-options-grid {
        grid-template-columns: 1fr;
    }

    .form-row {
        grid-template-columns: 1fr;
    }

    .btn-group {
        width: 100%;
    }

    .btn-group .btn {
        flex: 1;
    }
}

@media (max-width: 540px) {
    .main-content {
        padding: 0.85rem 0.65rem 2rem 0.65rem;
    }

    #tabTitle {
        font-size: 1.35rem;
    }

    #tabSubtitle {
        font-size: 0.8rem;
    }

    .card {
        border-radius: var(--radius-md);
        margin-bottom: 1rem;
    }

    .card-header, .card-body {
        padding: 1rem 0.85rem;
    }

    .info-grid-card {
        grid-template-columns: 1fr 1fr;
        gap: 0.6rem;
    }

    .info-stat-item {
        padding: 0.75rem;
    }

    .stat-val {
        font-size: 1rem;
    }

    .input-card {
        padding: 1rem 0.85rem;
    }

    .input-wrapper input {
        font-size: 1.25rem;
    }

    .btn {
        padding: 0.6rem 1rem;
        font-size: 0.85rem;
    }

    .bit-btn {
        width: 36px;
        height: 46px;
        font-size: 1.15rem;
    }

    .byte-group {
        gap: 0.25rem;
    }

    .bit-value-summary {
        grid-template-columns: 1fr 1fr;
        gap: 0.6rem;
    }

    .summary-box {
        padding: 0.75rem;
    }

    .summary-box .val {
        font-size: 1.1rem;
    }

    .toast {
        left: 1rem;
        right: 1rem;
        bottom: 1rem;
        text-align: center;
    }

    .quiz-feedback-box {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
    }
}

@media (max-width: 380px) {
    .main-content {
        padding: 0.65rem 0.5rem 1.5rem 0.5rem;
    }

    #tabTitle {
        font-size: 1.2rem;
    }

    .trig-results-grid {
        grid-template-columns: 1fr;
    }

    .info-grid-card {
        grid-template-columns: 1fr;
    }

    .bit-value-summary {
        grid-template-columns: 1fr;
    }

    .bit-btn {
        width: 28px;
        height: 38px;
        font-size: 0.95rem;
    }

    .byte-group {
        gap: 0.15rem;
    }
}
"""

# Replace the responsive breakpoints in CSS
old_breakpoints_pattern = r'/\* Responsive Breakpoints \*/.*?@media \(max-width: 768px\) \{.*?\n\}'
if re.search(old_breakpoints_pattern, html_content, re.DOTALL):
    html_content = re.sub(old_breakpoints_pattern, responsive_css_additions.strip(), html_content, flags=re.DOTALL)
    print("Replaced old breakpoints with comprehensive responsive CSS.")
else:
    # Insert before </style>
    html_content = html_content.replace('</style>', responsive_css_additions + '\n</style>')
    print("Appended responsive CSS before </style>.")

# 2. Add Backdrop Overlay & Close Button in HTML Markup
if '<div class="sidebar-backdrop"' not in html_content:
    # Add close button inside sidebar header
    html_content = html_content.replace(
        '<div class="sidebar-header">',
        '<div class="sidebar-header">\n                <button class="sidebar-close-btn" id="sidebarCloseBtn" aria-label="Close sidebar">&times;</button>'
    )
    # Add backdrop right after </aside>
    html_content = html_content.replace(
        '</aside>',
        '</aside>\n        <div class="sidebar-backdrop" id="sidebarBackdrop"></div>'
    )
    print("Added sidebar-backdrop and sidebar-close-btn into HTML markup.")

# 3. Update JavaScript logic for mobile navigation and backdrop
old_nav_js = """        if (mobileMenuBtn && sidebar) {
            mobileMenuBtn.addEventListener('click', () => {
                sidebar.classList.toggle('open');
            });
        }"""

new_nav_js = """        const sidebarBackdrop = document.getElementById('sidebarBackdrop');
        const sidebarCloseBtn = document.getElementById('sidebarCloseBtn');

        function openSidebar() {
            if (sidebar) sidebar.classList.add('open');
            if (sidebarBackdrop) sidebarBackdrop.classList.add('show');
            document.body.classList.add('sidebar-open');
        }

        function closeSidebar() {
            if (sidebar) sidebar.classList.remove('open');
            if (sidebarBackdrop) sidebarBackdrop.classList.remove('show');
            document.body.classList.remove('sidebar-open');
        }

        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (sidebar && sidebar.classList.contains('open')) {
                    closeSidebar();
                } else {
                    openSidebar();
                }
            });
        }

        if (sidebarBackdrop) {
            sidebarBackdrop.addEventListener('click', closeSidebar);
        }

        if (sidebarCloseBtn) {
            sidebarCloseBtn.addEventListener('click', closeSidebar);
        }

        // Close sidebar when clicking any nav-item on mobile
        navItems.forEach(item => {
            item.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    closeSidebar();
                }
            });
        });

        // Window resize handler for canvas & sidebar
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) {
                closeSidebar();
            }
            if (state.activeTab === 'trigonometry') {
                drawUnitCircle();
            }
            if (state.activeTab === 'logarithms') {
                drawLogGraph();
            }
        });"""

if old_nav_js in html_content:
    html_content = html_content.replace(old_nav_js, new_nav_js)
    print("Updated sidebar navigation and resize handlers in JavaScript.")
else:
    print("Notice: old_nav_js not found verbatim, searching pattern...")
    pattern = r'if\s*\(\s*mobileMenuBtn\s*&&\s*sidebar\s*\)\s*\{[\s\S]*?mobileMenuBtn\.addEventListener[\s\S]*?\}\s*\}'
    html_content = re.sub(pattern, new_nav_js, html_content)
    print("Replaced via regex pattern.")

# Save updated index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully updated {html_path}")
