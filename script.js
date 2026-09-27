/**
 * NUMBER SYSTEM & ADVANCED MATH TOOLKIT - SCRIPT ENGINE
 * Production-ready, fully interactive implementation.
 */

document.addEventListener('DOMContentLoaded', () => {
    // =========================================================
    // 1. STATE & THEME INITIALIZATION
    // =========================================================
    const state = {
        theme: localStorage.getItem('nst_theme') || 'dark',
        activeTab: 'live-converter',
        bitBoardSize: 8,
        bitBoardState: new Array(32).fill(0),
        trigAngleMode: 'deg', // 'deg', 'rad', 'grad'
        currentTrigAngleDeg: 45,
        quiz: {
            score: 0,
            streak: 0,
            currentQuestion: null
        }
    };

    document.documentElement.setAttribute('data-theme', state.theme);
    updateThemeButtonUI();

    // Initialize all components
    initTabNavigation();
    initThemeToggle();
    initQuickActions();
    initLiveConverter();
    initStepConverter();
    initDecimalArithmetic();
    initBinaryArithmetic();
    initValidator();
    initBitBoard();
    initTrigonometry();
    initLogarithms();
    initQuiz();

    // =========================================================
    // 2. THEME & NAVIGATION
    // =========================================================
    function initThemeToggle() {
        const themeBtn = document.getElementById('themeToggleBtn');
        if (!themeBtn) return;
        themeBtn.addEventListener('click', () => {
            state.theme = state.theme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', state.theme);
            localStorage.setItem('nst_theme', state.theme);
            updateThemeButtonUI();
            drawUnitCircle();
            drawLogGraph();
        });
    }

    function updateThemeButtonUI() {
        const themeText = document.getElementById('themeText');
        if (themeText) {
            themeText.textContent = state.theme === 'dark' ? 'Dark Mode' : 'Light Mode';
        }
    }

    function initTabNavigation() {
        const navItems = document.querySelectorAll('.nav-item');
        const tabPanes = document.querySelectorAll('.tab-pane');
        const tabTitle = document.getElementById('tabTitle');
        const tabSubtitle = document.getElementById('tabSubtitle');
        const sidebar = document.getElementById('sidebar');
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');

        const tabMetadata = {
            'live-converter': {
                title: 'Live Multi-Converter',
                subtitle: 'Real-time simultaneous conversion across Decimal, Binary, Octal, Hexadecimal & ASCII'
            },
            'step-converter': {
                title: 'Step-by-Step Solver',
                subtitle: 'Detailed mathematical breakdown of division & positional expansion algorithms'
            },
            'decimal-arithmetic': {
                title: 'Decimal Arithmetic',
                subtitle: 'Perform arithmetic operations with step-by-step formula breakdown'
            },
            'binary-arithmetic': {
                title: 'Binary Arithmetic',
                subtitle: 'Direct binary calculations with carry tracking and decimal verification'
            },
            'validator': {
                title: 'Number Validator',
                subtitle: 'Real-time base syntax checker with per-character analysis'
            },
            'bit-board': {
                title: 'Interactive Bit Board',
                subtitle: 'Clickable 8/16/32-bit registers with live signed/unsigned interpretations'
            },
            'trigonometry': {
                title: 'Trigonometry Lab & Unit Circle',
                subtitle: 'Interactive unit circle, exact standard angles, reciprocals & hyperbolics'
            },
            'logarithms': {
                title: 'Logarithm Suite & Step Solver',
                subtitle: 'Multi-base logarithms (Base 10, e, 2, custom), change of base steps & curve plotter'
            },
            'cheat-sheet': {
                title: 'Cheat Sheet & Tables',
                subtitle: 'Reference tables for 4-bit nibbles, powers of 2, and data sizes'
            },
            'practice-quiz': {
                title: 'Practice & Quiz Mode',
                subtitle: 'Test your understanding of number systems, trigonometry, and logarithms'
            }
        };

        navItems.forEach(item => {
            item.addEventListener('click', () => {
                const targetTab = item.dataset.tab;
                if (!targetTab) return;

                navItems.forEach(n => n.classList.remove('active'));
                tabPanes.forEach(p => p.classList.remove('active'));

                item.classList.add('active');
                const targetPane = document.getElementById(targetTab);
                if (targetPane) targetPane.classList.add('active');

                if (tabMetadata[targetTab]) {
                    if (tabTitle) tabTitle.textContent = tabMetadata[targetTab].title;
                    if (tabSubtitle) tabSubtitle.textContent = tabMetadata[targetTab].subtitle;
                }

                state.activeTab = targetTab;

                if (targetTab === 'trigonometry') setTimeout(drawUnitCircle, 50);
                if (targetTab === 'logarithms') setTimeout(drawLogGraph, 50);

                if (window.innerWidth <= 768 && sidebar) {
                    sidebar.classList.remove('open');
                }
            });
        });

        const sidebarBackdrop = document.getElementById('sidebarBackdrop');
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
        });
    }

    // =========================================================
    // 3. TOAST & QUICK ACTIONS
    // =========================================================
    function showToast(message) {
        const toast = document.getElementById('toast');
        if (!toast) return;
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2200);
    }

    function initQuickActions() {
        document.querySelectorAll('.copy-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.dataset.target;
                const input = document.getElementById(targetId);
                if (input && input.value) {
                    navigator.clipboard.writeText(input.value).then(() => {
                        showToast(`Copied "${input.value}" to clipboard!`);
                    }).catch(() => {
                        input.select();
                        document.execCommand('copy');
                        showToast(`Copied to clipboard!`);
                    });
                }
            });
        });

        const quickResetBtn = document.getElementById('quickResetBtn');
        if (quickResetBtn) {
            quickResetBtn.addEventListener('click', () => {
                const ids = ['liveDec', 'liveBin', 'liveOct', 'liveHex', 'liveCustom', 'liveAscii'];
                ids.forEach(id => {
                    const el = document.getElementById(id);
                    if (el) el.value = '';
                });
                const binFormatted = document.getElementById('liveBinFormatted');
                if (binFormatted) binFormatted.textContent = '0000 0000';
                updateInfoStats(0);
                showToast('Cleared all inputs');
            });
        }
    }

    // =========================================================
    // 4. LIVE MULTI-CONVERTER
    // =========================================================
    function initLiveConverter() {
        const decInput = document.getElementById('liveDec');
        const binInput = document.getElementById('liveBin');
        const octInput = document.getElementById('liveOct');
        const hexInput = document.getElementById('liveHex');
        const customInput = document.getElementById('liveCustom');
        const customSelect = document.getElementById('customBaseSelect');
        const asciiInput = document.getElementById('liveAscii');
        const binFormatted = document.getElementById('liveBinFormatted');

        if (!decInput) return;

        function formatBinaryWithSpaces(binStr) {
            if (!binStr) return '0000 0000';
            const padLen = (4 - (binStr.length % 4)) % 4;
            const padded = '0'.repeat(padLen) + binStr;
            return padded.match(/.{1,4}/g)?.join(' ') || binStr;
        }

        function updateAllFromDecimal(decVal, source = 'dec') {
            if (isNaN(decVal) || decVal === null || decVal === '') {
                if (source !== 'dec' && decInput) decInput.value = '';
                if (source !== 'bin' && binInput) binInput.value = '';
                if (source !== 'oct' && octInput) octInput.value = '';
                if (source !== 'hex' && hexInput) hexInput.value = '';
                if (source !== 'custom' && customInput) customInput.value = '';
                if (source !== 'ascii' && asciiInput) asciiInput.value = '';
                if (binFormatted) binFormatted.textContent = '0000 0000';
                updateInfoStats(0);
                return;
            }

            const num = BigInt(Math.floor(Number(decVal)));
            const customBase = customSelect ? parseInt(customSelect.value, 10) : 36;

            if (source !== 'dec' && decInput) decInput.value = num.toString(10);
            if (source !== 'bin' && binInput) binInput.value = num.toString(2);
            if (source !== 'oct' && octInput) octInput.value = num.toString(8);
            if (source !== 'hex' && hexInput) hexInput.value = num.toString(16).toUpperCase();
            if (source !== 'custom' && customInput) customInput.value = num.toString(customBase).toUpperCase();

            if (source !== 'ascii' && asciiInput) {
                if (num >= 32n && num <= 126n) {
                    asciiInput.value = String.fromCharCode(Number(num));
                } else if (num >= 0n && num < 32n) {
                    const controlCodes = ["NUL","SOH","STX","ETX","EOT","ENQ","ACK","BEL","BS","HT","LF","VT","FF","CR","SO","SI","DLE","DC1","DC2","DC3","DC4","NAK","SYN","ETB","CAN","EM","SUB","ESC","FS","GS","RS","US"];
                    asciiInput.value = `[${controlCodes[Number(num)]}]`;
                } else {
                    asciiInput.value = `(Dec: ${num})`;
                }
            }

            if (binFormatted) binFormatted.textContent = formatBinaryWithSpaces(num.toString(2));
            updateInfoStats(Number(num));
        }

        function updateInfoStats(num) {
            const bitLenElem = document.getElementById('statBitLength');
            const byteCountElem = document.getElementById('statByteCount');
            const parityElem = document.getElementById('statParity');
            const powerOfTwoElem = document.getElementById('statPowerOfTwo');

            if (!num || num < 0) {
                if (bitLenElem) bitLenElem.textContent = '0 bits';
                if (byteCountElem) byteCountElem.textContent = '0 Bytes';
                if (parityElem) parityElem.textContent = '0 (Even)';
                if (powerOfTwoElem) powerOfTwoElem.textContent = 'No';
                return;
            }

            const bin = num.toString(2);
            const bitLength = bin.length;
            const byteCount = Math.ceil(bitLength / 8);
            const onesCount = (bin.match(/1/g) || []).length;
            const isEvenParity = onesCount % 2 === 0;
            const isPowerOfTwo = (num > 0) && ((num & (num - 1)) === 0);

            if (bitLenElem) bitLenElem.textContent = `${bitLength} bits`;
            if (byteCountElem) byteCountElem.textContent = `${byteCount} Byte${byteCount > 1 ? 's' : ''}`;
            if (parityElem) parityElem.textContent = `${onesCount} (${isEvenParity ? 'Even' : 'Odd'})`;
            if (powerOfTwoElem) {
                if (isPowerOfTwo) {
                    const power = Math.log2(num);
                    powerOfTwoElem.textContent = `Yes (2^${power})`;
                } else {
                    powerOfTwoElem.textContent = 'No';
                }
            }
        }

        decInput.addEventListener('input', (e) => {
            const clean = e.target.value.replace(/[^0-9]/g, '');
            if (e.target.value !== clean) e.target.value = clean;
            if (clean === '') { updateAllFromDecimal('', 'dec'); return; }
            updateAllFromDecimal(parseInt(clean, 10), 'dec');
        });

        if (binInput) {
            binInput.addEventListener('input', (e) => {
                const clean = e.target.value.replace(/[^01]/g, '');
                if (e.target.value !== clean) e.target.value = clean;
                if (clean === '') { updateAllFromDecimal('', 'bin'); return; }
                const dec = parseInt(clean, 2);
                updateAllFromDecimal(dec, 'bin');
            });
        }

        if (octInput) {
            octInput.addEventListener('input', (e) => {
                const clean = e.target.value.replace(/[^0-7]/g, '');
                if (e.target.value !== clean) e.target.value = clean;
                if (clean === '') { updateAllFromDecimal('', 'oct'); return; }
                const dec = parseInt(clean, 8);
                updateAllFromDecimal(dec, 'oct');
            });
        }

        if (hexInput) {
            hexInput.addEventListener('input', (e) => {
                const clean = e.target.value.replace(/[^0-9a-fA-F]/g, '').toUpperCase();
                if (e.target.value !== clean) e.target.value = clean;
                if (clean === '') { updateAllFromDecimal('', 'hex'); return; }
                const dec = parseInt(clean, 16);
                updateAllFromDecimal(dec, 'hex');
            });
        }

        if (customInput) {
            customInput.addEventListener('input', (e) => {
                const base = customSelect ? parseInt(customSelect.value, 10) : 36;
                const val = e.target.value.trim();
                if (val === '') { updateAllFromDecimal('', 'custom'); return; }
                try {
                    const dec = parseInt(val, base);
                    if (!isNaN(dec)) updateAllFromDecimal(dec, 'custom');
                } catch {}
            });
        }

        if (customSelect) {
            customSelect.addEventListener('change', () => {
                const decVal = parseInt(decInput.value, 10);
                if (!isNaN(decVal)) updateAllFromDecimal(decVal, 'dec');
            });
        }

        if (asciiInput) {
            asciiInput.addEventListener('input', (e) => {
                const text = e.target.value;
                if (!text) { updateAllFromDecimal('', 'ascii'); return; }
                const charCode = text.charCodeAt(0);
                updateAllFromDecimal(charCode, 'ascii');
            });
        }

        document.querySelectorAll('.chip[data-fill]').forEach(chip => {
            chip.addEventListener('click', () => {
                const val = chip.dataset.fill;
                decInput.value = val;
                updateAllFromDecimal(parseInt(val, 10), 'dec');
            });
        });

        updateAllFromDecimal(255, 'dec');
    }

    // =========================================================
    // 5. STEP-BY-STEP CONVERTER SOLVER (C++ Port)
    // =========================================================
    function initStepConverter() {
        const typeSelect = document.getElementById('stepConversionType');
        const inputNum = document.getElementById('stepInputNumber');
        const calcBtn = document.getElementById('calculateStepBtn');
        const outputContainer = document.getElementById('stepOutputContainer');

        if (!typeSelect || !inputNum || !calcBtn || !outputContainer) return;

        function generateSteps() {
            const method = typeSelect.value;
            const inputVal = inputNum.value.trim();

            if (!inputVal) {
                outputContainer.innerHTML = `<div class="error-msg">Please enter a number to convert.</div>`;
                return;
            }

            switch (method) {
                case 'dec2bin': outputContainer.innerHTML = solveDecimalToBinary(inputVal); break;
                case 'dec2oct': outputContainer.innerHTML = solveDecimalToOctal(inputVal); break;
                case 'dec2hex': outputContainer.innerHTML = solveDecimalToHexadecimal(inputVal); break;
                case 'bin2dec': outputContainer.innerHTML = solveBinaryToDecimal(inputVal); break;
                case 'oct2dec': outputContainer.innerHTML = solveOctalToDecimal(inputVal); break;
                case 'hex2dec': outputContainer.innerHTML = solveHexadecimalToDecimal(inputVal); break;
            }
        }

        calcBtn.addEventListener('click', generateSteps);
        inputNum.addEventListener('keypress', (e) => { if (e.key === 'Enter') generateSteps(); });

        typeSelect.addEventListener('change', () => {
            if (typeSelect.value.startsWith('dec2')) inputNum.value = '29';
            else if (typeSelect.value === 'bin2dec') inputNum.value = '11101';
            else if (typeSelect.value === 'oct2dec') inputNum.value = '35';
            else if (typeSelect.value === 'hex2dec') inputNum.value = '1D';
            generateSteps();
        });

        generateSteps();
    }

    function solveDecimalToBinary(valStr) {
        const dec = parseInt(valStr, 10);
        if (isNaN(dec)) return `<div class="error-msg">Invalid Decimal Number!</div>`;
        if (dec < 0) return `<div class="error-msg">Please enter a positive decimal number.</div>`;
        if (dec === 0) return `<div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">0₂</div></div>`;

        let decimal = dec;
        const original = dec;
        const remainders = [];
        const rows = [];
        let step = 1;

        while (decimal > 0) {
            const quotient = Math.floor(decimal / 2);
            const rem = decimal % 2;
            remainders.push(rem);
            rows.push(`<tr><td>Step ${step}</td><td>${decimal} ÷ 2</td><td><strong>${quotient}</strong></td><td><span class="remainder-highlight">${rem}</span></td></tr>`);
            decimal = quotient;
            step++;
        }

        const binResult = [...remainders].reverse().join('');
        const bottomToTop = [...remainders].reverse().join(' ');

        return `
            <div class="step-header-banner">
                <span class="step-badge-title">DECIMAL TO BINARY (REPEATED DIVISION BY 2)</span>
                <span class="badge">Base 10 → Base 2</span>
            </div>
            <p><strong>Process:</strong> Divide continuously by 2 and collect remainders.</p>
            <table class="step-table">
                <thead><tr><th>Step</th><th>Division</th><th>Quotient</th><th>Remainder</th></tr></thead>
                <tbody>${rows.join('')}</tbody>
            </table>
            <div class="read-direction-box">
                <p>⬆️ <strong>Read remainders bottom-to-top (LSB to MSB):</strong></p>
                <div class="remainder-sequence">${bottomToTop}</div>
            </div>
            <p><strong>Therefore:</strong> ${original} in Decimal = <code>${binResult}</code> in Binary</p>
            <div class="final-answer-card">
                <div><div class="final-answer-title">FINAL ANSWER</div><div class="text-muted">Decimal ${original}₁₀ in Binary</div></div>
                <div class="final-answer-value">${binResult}₂</div>
            </div>
        `;
    }

    function solveDecimalToOctal(valStr) {
        const dec = parseInt(valStr, 10);
        if (isNaN(dec)) return `<div class="error-msg">Invalid Decimal Number!</div>`;
        if (dec < 0) return `<div class="error-msg">Please enter a positive decimal number.</div>`;
        if (dec === 0) return `<div class="final-answer-card"><div class="final-answer-value">0₈</div></div>`;

        let decimal = dec;
        const original = dec;
        const remainders = [];
        const rows = [];
        let step = 1;

        while (decimal > 0) {
            const quotient = Math.floor(decimal / 8);
            const rem = decimal % 8;
            remainders.push(rem);
            rows.push(`<tr><td>Step ${step}</td><td>${decimal} ÷ 8</td><td><strong>${quotient}</strong></td><td><span class="remainder-highlight">${rem}</span></td></tr>`);
            decimal = quotient;
            step++;
        }

        const octResult = [...remainders].reverse().join('');
        return `
            <div class="step-header-banner"><span class="step-badge-title">DECIMAL TO OCTAL (REPEATED DIVISION BY 8)</span><span class="badge">Base 10 → Base 8</span></div>
            <table class="step-table"><thead><tr><th>Step</th><th>Division</th><th>Quotient</th><th>Remainder</th></tr></thead><tbody>${rows.join('')}</tbody></table>
            <div class="read-direction-box"><p>⬆️ <strong>Read remainders bottom-to-top:</strong></p><div class="remainder-sequence">${[...remainders].reverse().join(' ')}</div></div>
            <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${octResult}₈</div></div>
        `;
    }

    function solveDecimalToHexadecimal(valStr) {
        const dec = parseInt(valStr, 10);
        if (isNaN(dec)) return `<div class="error-msg">Invalid Decimal Number!</div>`;
        if (dec < 0) return `<div class="error-msg">Please enter a positive decimal number.</div>`;
        if (dec === 0) return `<div class="final-answer-card"><div class="final-answer-value">0₁₆</div></div>`;

        const hexChars = "0123456789ABCDEF";
        let decimal = dec;
        const resultChars = [];
        const rows = [];
        let step = 1;

        while (decimal > 0) {
            const quotient = Math.floor(decimal / 16);
            const rem = decimal % 16;
            const hexChar = hexChars[rem];
            resultChars.push(hexChar);
            const remNote = rem >= 10 ? ` (${hexChar})` : '';
            rows.push(`<tr><td>Step ${step}</td><td>${decimal} ÷ 16</td><td><strong>${quotient}</strong></td><td><span class="remainder-highlight">${rem}${remNote}</span></td></tr>`);
            decimal = quotient;
            step++;
        }

        const hexResult = [...resultChars].reverse().join('');
        return `
            <div class="step-header-banner"><span class="step-badge-title">DECIMAL TO HEXADECIMAL (REPEATED DIVISION BY 16)</span><span class="badge">Base 10 → Base 16</span></div>
            <table class="step-table"><thead><tr><th>Step</th><th>Division</th><th>Quotient</th><th>Remainder</th></tr></thead><tbody>${rows.join('')}</tbody></table>
            <div class="read-direction-box"><p>⬆️ <strong>Read remainders bottom-to-top:</strong></p><div class="remainder-sequence">${[...resultChars].reverse().join(' ')}</div></div>
            <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${hexResult}₁₆</div></div>
        `;
    }

    function solveBinaryToDecimal(binStr) {
        if (!/^[01]+$/.test(binStr)) return `<div class="error-msg">Invalid Binary Number! Only 0 and 1 are allowed.</div>`;
        const len = binStr.length;
        let decimal = 0;
        const steps = [];
        const additions = [];

        for (let i = len - 1; i >= 0; i--) {
            const digit = parseInt(binStr[i], 10);
            const pos = len - 1 - i;
            const value = digit * Math.pow(2, pos);
            decimal += value;
            steps.push(`<div class="expansion-step-item"><span class="calc-math">Digit '${digit}' at position 2<sup>${pos}</sup>: ${digit} × 2<sup>${pos}</sup> (${Math.pow(2, pos)})</span><span class="calc-res">= ${value}</span></div>`);
            additions.push(value);
        }

        return `
            <div class="step-header-banner"><span class="step-badge-title">BINARY TO DECIMAL (POSITIONAL EXPANSION)</span><span class="badge">Base 2 → Base 10</span></div>
            <div class="expansion-list">${steps.reverse().join('')}</div>
            <div class="addition-summation-box"><p class="text-muted"><strong>Add values:</strong></p><div>${additions.reverse().join(' + ')} = <strong>${decimal}</strong></div></div>
            <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${decimal}₁₀</div></div>
        `;
    }

    function solveOctalToDecimal(octStr) {
        if (!/^[0-7]+$/.test(octStr)) return `<div class="error-msg">Invalid Octal Number! Only 0-7 allowed.</div>`;
        const len = octStr.length;
        let decimal = 0;
        const steps = [];
        const additions = [];

        for (let i = len - 1; i >= 0; i--) {
            const digit = parseInt(octStr[i], 10);
            const pos = len - 1 - i;
            const value = digit * Math.pow(8, pos);
            decimal += value;
            steps.push(`<div class="expansion-step-item"><span class="calc-math">Digit '${digit}' at position 8<sup>${pos}</sup>: ${digit} × 8<sup>${pos}</sup></span><span class="calc-res">= ${value}</span></div>`);
            additions.push(value);
        }

        return `
            <div class="step-header-banner"><span class="step-badge-title">OCTAL TO DECIMAL (POSITIONAL EXPANSION)</span><span class="badge">Base 8 → Base 10</span></div>
            <div class="expansion-list">${steps.reverse().join('')}</div>
            <div class="addition-summation-box"><p class="text-muted"><strong>Add values:</strong></p><div>${additions.reverse().join(' + ')} = <strong>${decimal}</strong></div></div>
            <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${decimal}₁₀</div></div>
        `;
    }

    function solveHexadecimalToDecimal(hexStr) {
        const hex = hexStr.toUpperCase();
        if (!/^[0-9A-F]+$/.test(hex)) return `<div class="error-msg">Invalid Hexadecimal Number! Digits 0-9, A-F allowed.</div>`;
        const len = hex.length;
        let decimal = 0;
        const steps = [];
        const additions = [];

        for (let i = len - 1; i >= 0; i--) {
            const char = hex[i];
            let value = (char >= '0' && char <= '9') ? char.charCodeAt(0) - 48 : char.charCodeAt(0) - 65 + 10;
            const pos = len - 1 - i;
            const calculated = value * Math.pow(16, pos);
            decimal += calculated;
            steps.push(`<div class="expansion-step-item"><span class="calc-math">Digit '${char}' (value ${value}) at position 16<sup>${pos}</sup>: ${value} × 16<sup>${pos}</sup></span><span class="calc-res">= ${calculated}</span></div>`);
            additions.push(calculated);
        }

        return `
            <div class="step-header-banner"><span class="step-badge-title">HEXADECIMAL TO DECIMAL (POSITIONAL EXPANSION)</span><span class="badge">Base 16 → Base 10</span></div>
            <div class="expansion-list">${steps.reverse().join('')}</div>
            <div class="addition-summation-box"><p class="text-muted"><strong>Add values:</strong></p><div>${additions.reverse().join(' + ')} = <strong>${decimal}</strong></div></div>
            <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${decimal}₁₀</div></div>
        `;
    }

    // =========================================================
    // 6. DECIMAL ARITHMETIC
    // =========================================================
    function initDecimalArithmetic() {
        const numA = document.getElementById('decNumA');
        const numB = document.getElementById('decNumB');
        const opSelect = document.getElementById('decOp');
        const calcBtn = document.getElementById('calcDecArithBtn');
        const resultContainer = document.getElementById('decArithResult');

        if (!numA || !numB || !opSelect || !calcBtn || !resultContainer) return;

        function calculate() {
            const a = parseInt(numA.value, 10);
            const b = parseInt(numB.value, 10);
            const op = opSelect.value;

            if (isNaN(a) || isNaN(b)) {
                resultContainer.innerHTML = `<div class="error-msg">Please enter valid decimal integers.</div>`;
                return;
            }

            let opSymbol = '+', opTitle = 'ADDITION', formula = 'Addition = A + B', result;

            if (op === 'add') { opSymbol = '+'; opTitle = 'ADDITION'; result = a + b; }
            else if (op === 'sub') { opSymbol = '−'; opTitle = 'SUBTRACTION'; result = a - b; }
            else if (op === 'mul') { opSymbol = '×'; opTitle = 'MULTIPLICATION'; result = a * b; }
            else if (op === 'div') {
                opSymbol = '÷'; opTitle = 'DIVISION';
                if (b === 0) { resultContainer.innerHTML = `<div class="error-msg">Division by zero is not allowed.</div>`; return; }
                result = (a / b).toFixed(4).replace(/\.?0+$/, '');
            } else if (op === 'mod') {
                opSymbol = '%'; opTitle = 'MODULUS';
                if (b === 0) { resultContainer.innerHTML = `<div class="error-msg">Modulus by zero is not allowed.</div>`; return; }
                result = a % b;
            }

            resultContainer.innerHTML = `
                <div class="step-header-banner"><span class="step-badge-title">DECIMAL ${opTitle}</span><span class="badge">${a} ${opSymbol} ${b}</span></div>
                <div class="arithmetic-step-box">First number = ${a}
Second number = ${b}

Calculation:
${op !== 'div' && op !== 'mod' ? `  ${a}
${opSymbol} ${b}
----------------
  ${result}` : `${a} ${opSymbol} ${b} = ${result}`}

FINAL ANSWER: ${result}</div>
                <div class="final-answer-card"><div><div class="final-answer-title">FINAL ANSWER</div></div><div class="final-answer-value">${result}</div></div>
            `;
        }

        calcBtn.addEventListener('click', calculate);
        calculate();
    }

    // =========================================================
    // 7. BINARY ARITHMETIC
    // =========================================================
    function initBinaryArithmetic() {
        const binA = document.getElementById('binNumA');
        const binB = document.getElementById('binNumB');
        const binOp = document.getElementById('binOp');
        const calcBtn = document.getElementById('calcBinArithBtn');
        const resultContainer = document.getElementById('binArithResult');
        const hintA = document.getElementById('binHintA');
        const hintB = document.getElementById('binHintB');

        if (!binA || !binB || !binOp || !calcBtn || !resultContainer) return;

        function updateHints() {
            const a = binA.value.trim();
            const b = binB.value.trim();
            if (/^[01]+$/.test(a)) hintA.textContent = `Decimal: ${parseInt(a, 2)}`;
            else hintA.textContent = `Invalid binary`;

            if (/^[01]+$/.test(b)) hintB.textContent = `Decimal: ${parseInt(b, 2)}`;
            else hintB.textContent = `Invalid binary`;
        }

        binA.addEventListener('input', updateHints);
        binB.addEventListener('input', updateHints);

        function calculate() {
            const a = binA.value.trim();
            const b = binB.value.trim();
            const op = binOp.value;

            if (!/^[01]+$/.test(a) || !/^[01]+$/.test(b)) {
                resultContainer.innerHTML = `<div class="error-msg">Invalid Binary Number! Only 0 and 1 are allowed.</div>`;
                return;
            }

            const decA = parseInt(a, 2);
            const decB = parseInt(b, 2);
            let decResult, binResult, opTitle, opSymbol;

            if (op === 'add') { opTitle = 'BINARY ADDITION'; opSymbol = '+'; decResult = decA + decB; binResult = decResult.toString(2); }
            else if (op === 'sub') {
                opTitle = 'BINARY SUBTRACTION'; opSymbol = '−';
                if (decA < decB) { resultContainer.innerHTML = `<div class="error-msg">First number must be greater than second number for standard subtraction.</div>`; return; }
                decResult = decA - decB; binResult = decResult.toString(2);
            }
            else if (op === 'mul') { opTitle = 'BINARY MULTIPLICATION'; opSymbol = '×'; decResult = decA * decB; binResult = decResult.toString(2); }
            else if (op === 'div') {
                opTitle = 'BINARY DIVISION'; opSymbol = '÷';
                if (decB === 0) { resultContainer.innerHTML = `<div class="error-msg">Division by zero is not allowed.</div>`; return; }
                decResult = Math.floor(decA / decB); binResult = decResult.toString(2);
            }

            resultContainer.innerHTML = `
                <div class="step-header-banner"><span class="step-badge-title">${opTitle}</span><span class="badge">${a}₂ ${opSymbol} ${b}₂</span></div>
                <div class="arithmetic-step-box">Convert to Decimal:
${a} = ${decA}
${b} = ${decB}

Calculation: ${decA} ${opSymbol} ${decB} = ${decResult}

Convert back to Binary:
${decResult} = ${binResult}

FINAL ANSWER: ${binResult}</div>
                <div class="final-answer-card"><div><div class="final-answer-title">FINAL BINARY ANSWER</div><div class="text-muted">Decimal: ${decResult}</div></div><div class="final-answer-value">${binResult}₂</div></div>
            `;
        }

        calcBtn.addEventListener('click', calculate);
        updateHints();
        calculate();
    }

    // =========================================================
    // 8. NUMBER VALIDATOR
    // =========================================================
    function initValidator() {
        const input = document.getElementById('validateInput');
        if (!input) return;

        function runValidation() {
            const val = input.value.trim();
            validateBase('Bin', val, /^[01]$/, 'Binary');
            validateBase('Oct', val, /^[0-7]$/, 'Octal');
            validateBase('Dec', val, /^[0-9]$/, 'Decimal');
            validateBase('Hex', val, /^[0-9a-fA-F]$/, 'Hexadecimal');
        }

        function validateBase(key, str, charRegex, baseName) {
            const card = document.getElementById(`valCard${key}`);
            const badge = document.getElementById(`valBadge${key}`);
            const stream = document.getElementById(`valStream${key}`);

            if (!card || !badge || !stream) return;

            if (!str) {
                card.className = 'validator-card';
                badge.className = 'val-badge';
                badge.textContent = 'Awaiting input';
                stream.innerHTML = '';
                return;
            }

            let allValid = true;
            const chips = [];

            for (let i = 0; i < str.length; i++) {
                const c = str[i];
                const isValid = charRegex.test(c);
                if (!isValid) allValid = false;
                chips.push(`<span class="char-chip ${isValid ? 'valid-char' : 'invalid-char'}">${c}</span>`);
            }

            stream.innerHTML = chips.join('');
            card.className = allValid ? 'validator-card valid' : 'validator-card invalid';
            badge.className = allValid ? 'val-badge badge-valid' : 'val-badge badge-invalid';
            badge.textContent = allValid ? `Valid ${baseName}` : `Invalid ${baseName}`;
        }

        input.addEventListener('input', runValidation);
        runValidation();
    }

    // =========================================================
    // 9. INTERACTIVE BIT BOARD
    // =========================================================
    function initBitBoard() {
        const container = document.getElementById('bitGridContainer');
        const sizeButtons = document.querySelectorAll('#bitSizeGroup button');
        const bitClearBtn = document.getElementById('bitClearBtn');
        const bitSetAllBtn = document.getElementById('bitSetAllBtn');
        const bitInvertBtn = document.getElementById('bitInvertBtn');
        const bitShiftLeftBtn = document.getElementById('bitShiftLeftBtn');
        const bitShiftRightBtn = document.getElementById('bitShiftRightBtn');

        if (!container) return;

        sizeButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                sizeButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                state.bitBoardSize = parseInt(btn.dataset.bits, 10);
                renderBitBoard();
            });
        });

        function renderBitBoard() {
            container.innerHTML = '';
            const size = state.bitBoardSize;
            const byteCount = size / 8;

            for (let byteIndex = 0; byteIndex < byteCount; byteIndex++) {
                const byteGroup = document.createElement('div');
                byteGroup.className = 'byte-group';

                for (let bitInByte = 7; bitInByte >= 0; bitInByte--) {
                    const bitPos = (byteCount - 1 - byteIndex) * 8 + bitInByte;
                    const isSet = state.bitBoardState[bitPos] === 1;

                    const cell = document.createElement('div');
                    cell.className = 'bit-cell';

                    const posLabel = document.createElement('span');
                    posLabel.className = 'bit-pos';
                    posLabel.textContent = `b${bitPos}`;

                    const bitBtn = document.createElement('button');
                    bitBtn.className = `bit-btn ${isSet ? 'on' : ''}`;
                    bitBtn.textContent = isSet ? '1' : '0';
                    bitBtn.addEventListener('click', () => {
                        state.bitBoardState[bitPos] = state.bitBoardState[bitPos] === 1 ? 0 : 1;
                        renderBitBoard();
                    });

                    const weightLabel = document.createElement('span');
                    weightLabel.className = 'bit-weight';
                    weightLabel.textContent = bitPos < 16 ? Math.pow(2, bitPos) : `2^${bitPos}`;

                    cell.appendChild(posLabel);
                    cell.appendChild(bitBtn);
                    cell.appendChild(weightLabel);
                    byteGroup.appendChild(cell);
                }

                container.appendChild(byteGroup);
            }

            updateBitValues();
        }

        function updateBitValues() {
            const size = state.bitBoardSize;
            let binStr = '';
            for (let i = size - 1; i >= 0; i--) {
                binStr += state.bitBoardState[i];
            }

            const unsignedDec = BigInt('0b' + binStr);
            let signedDec = unsignedDec;

            if (state.bitBoardState[size - 1] === 1) {
                const maxVal = 1n << BigInt(size);
                signedDec = unsignedDec - maxVal;
            }

            const hexStr = unsignedDec.toString(16).toUpperCase().padStart(Math.ceil(size / 4), '0');
            const octStr = unsignedDec.toString(8);

            const unsignedEl = document.getElementById('bitValUnsigned');
            const signedEl = document.getElementById('bitValSigned');
            const hexEl = document.getElementById('bitValHex');
            const octEl = document.getElementById('bitValOct');
            const asciiEl = document.getElementById('bitValAscii');

            if (unsignedEl) unsignedEl.textContent = unsignedDec.toString();
            if (signedEl) signedEl.textContent = signedDec.toString();
            if (hexEl) hexEl.textContent = `0x${hexStr}`;
            if (octEl) octEl.textContent = `0o${octStr}`;

            const asciiVal = Number(unsignedDec & 0xFFn);
            let asciiChar = 'N/A';
            if (asciiVal >= 32 && asciiVal <= 126) asciiChar = `'${String.fromCharCode(asciiVal)}'`;
            else if (asciiVal === 0) asciiChar = 'NUL';
            else asciiChar = `[0x${asciiVal.toString(16).toUpperCase()}]`;

            if (asciiEl) asciiEl.textContent = asciiChar;
        }

        if (bitClearBtn) bitClearBtn.addEventListener('click', () => { state.bitBoardState.fill(0); renderBitBoard(); });
        if (bitSetAllBtn) bitSetAllBtn.addEventListener('click', () => { for (let i = 0; i < state.bitBoardSize; i++) state.bitBoardState[i] = 1; renderBitBoard(); });
        if (bitInvertBtn) bitInvertBtn.addEventListener('click', () => { for (let i = 0; i < state.bitBoardSize; i++) state.bitBoardState[i] = state.bitBoardState[i] === 1 ? 0 : 1; renderBitBoard(); });
        if (bitShiftLeftBtn) bitShiftLeftBtn.addEventListener('click', () => { for (let i = state.bitBoardSize - 1; i > 0; i--) state.bitBoardState[i] = state.bitBoardState[i - 1]; state.bitBoardState[0] = 0; renderBitBoard(); });
        if (bitShiftRightBtn) bitShiftRightBtn.addEventListener('click', () => { for (let i = 0; i < state.bitBoardSize - 1; i++) state.bitBoardState[i] = state.bitBoardState[i + 1]; state.bitBoardState[state.bitBoardSize - 1] = 0; renderBitBoard(); });

        renderBitBoard();
    }

    // =========================================================
    // 10. TRIGONOMETRY LAB & UNIT CIRCLE
    // =========================================================
    const exactTrigValues = {
        0:   { sin: '0', cos: '1', tan: '0', csc: 'Undefined', sec: '1', cot: 'Undefined' },
        30:  { sin: '1/2', cos: '√3 / 2', tan: '√3 / 3', csc: '2', sec: '2√3 / 3', cot: '√3' },
        45:  { sin: '√2 / 2', cos: '√2 / 2', tan: '1', csc: '√2', sec: '√2', cot: '1' },
        60:  { sin: '√3 / 2', cos: '1/2', tan: '√3', csc: '2√3 / 3', sec: '2', cot: '√3 / 3' },
        90:  { sin: '1', cos: '0', tan: 'Undefined', csc: '1', sec: 'Undefined', cot: '0' },
        120: { sin: '√3 / 2', cos: '-1/2', tan: '-√3', csc: '2√3 / 3', sec: '-2', cot: '-√3 / 3' },
        135: { sin: '√2 / 2', cos: '-√2 / 2', tan: '-1', csc: '√2', sec: '-√2', cot: '-1' },
        150: { sin: '1/2', cos: '-√3 / 2', tan: '-√3 / 3', csc: '2', sec: '-2√3 / 3', cot: '-√3' },
        180: { sin: '0', cos: '-1', tan: '0', csc: 'Undefined', sec: '-1', cot: 'Undefined' },
        210: { sin: '-1/2', cos: '-√3 / 2', tan: '√3 / 3', csc: '-2', sec: '-2√3 / 3', cot: '√3' },
        225: { sin: '-√2 / 2', cos: '-√2 / 2', tan: '1', csc: '-√2', sec: '-√2', cot: '1' },
        240: { sin: '-√3 / 2', cos: '-1/2', tan: '√3', csc: '-2√3 / 3', sec: '-2', cot: '√3 / 3' },
        270: { sin: '-1', cos: '0', tan: 'Undefined', csc: '-1', sec: 'Undefined', cot: '0' },
        300: { sin: '-√3 / 2', cos: '1/2', tan: '-√3', csc: '-2√3 / 3', sec: '2', cot: '-√3 / 3' },
        315: { sin: '-√2 / 2', cos: '√2 / 2', tan: '-1', csc: '-√2', sec: '√2', cot: '-1' },
        330: { sin: '-1/2', cos: '√3 / 2', tan: '-√3 / 3', csc: '-2', sec: '2√3 / 3', cot: '-√3' },
        360: { sin: '0', cos: '1', tan: '0', csc: 'Undefined', sec: '1', cot: 'Undefined' }
    };

    function initTrigonometry() {
        const angleInput = document.getElementById('trigAngleInput');
        const angleSlider = document.getElementById('trigAngleSlider');
        const modeButtons = document.querySelectorAll('#trigAngleModeGroup button');
        const unitBadge = document.getElementById('trigUnitBadge');

        if (!angleInput) return;

        modeButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                modeButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                state.trigAngleMode = btn.dataset.mode;
                
                if (unitBadge) {
                    if (state.trigAngleMode === 'deg') unitBadge.textContent = 'deg (°)';
                    else if (state.trigAngleMode === 'rad') unitBadge.textContent = 'rad';
                    else if (state.trigAngleMode === 'grad') unitBadge.textContent = 'grad';
                }

                syncTrigInputsFromState();
            });
        });

        angleInput.addEventListener('input', () => {
            let val = parseFloat(angleInput.value);
            if (isNaN(val)) return;

            let deg = val;
            if (state.trigAngleMode === 'rad') deg = val * (180 / Math.PI);
            else if (state.trigAngleMode === 'grad') deg = val * 0.9;

            state.currentTrigAngleDeg = deg;
            if (angleSlider) angleSlider.value = ((deg % 360) + 360) % 360;
            updateTrigOutputs();
            drawUnitCircle();
        });

        if (angleSlider) {
            angleSlider.addEventListener('input', () => {
                const deg = parseFloat(angleSlider.value);
                state.currentTrigAngleDeg = deg;

                if (state.trigAngleMode === 'deg') angleInput.value = deg;
                else if (state.trigAngleMode === 'rad') angleInput.value = (deg * (Math.PI / 180)).toFixed(4);
                else if (state.trigAngleMode === 'grad') angleInput.value = (deg / 0.9).toFixed(2);

                updateTrigOutputs();
                drawUnitCircle();
            });
        }

        document.querySelectorAll('[data-trig-angle]').forEach(btn => {
            btn.addEventListener('click', () => {
                const deg = parseFloat(btn.dataset.trigAngle);
                state.currentTrigAngleDeg = deg;
                if (angleSlider) angleSlider.value = deg;

                if (state.trigAngleMode === 'deg') angleInput.value = deg;
                else if (state.trigAngleMode === 'rad') angleInput.value = (deg * (Math.PI / 180)).toFixed(4);
                else if (state.trigAngleMode === 'grad') angleInput.value = (deg / 0.9).toFixed(2);

                updateTrigOutputs();
                drawUnitCircle();
            });
        });

        syncTrigInputsFromState();
    }

    function syncTrigInputsFromState() {
        const angleInput = document.getElementById('trigAngleInput');
        const angleSlider = document.getElementById('trigAngleSlider');
        let deg = state.currentTrigAngleDeg;

        if (angleInput) {
            if (state.trigAngleMode === 'deg') angleInput.value = deg;
            else if (state.trigAngleMode === 'rad') angleInput.value = (deg * (Math.PI / 180)).toFixed(4);
            else if (state.trigAngleMode === 'grad') angleInput.value = (deg / 0.9).toFixed(2);
        }

        if (angleSlider) {
            angleSlider.value = ((deg % 360) + 360) % 360;
        }

        updateTrigOutputs();
        drawUnitCircle();
    }

    function updateTrigOutputs() {
        const rad = state.currentTrigAngleDeg * (Math.PI / 180);
        const normDeg = Math.round(((state.currentTrigAngleDeg % 360) + 360) % 360);

        const sinVal = Math.sin(rad);
        const cosVal = Math.cos(rad);
        let tanVal = (normDeg === 90 || normDeg === 270) ? NaN : Math.tan(rad);

        const cscVal = Math.abs(sinVal) < 1e-12 ? NaN : 1 / sinVal;
        const secVal = Math.abs(cosVal) < 1e-12 ? NaN : 1 / cosVal;
        const cotVal = Math.abs(tanVal) < 1e-12 ? NaN : 1 / tanVal;

        const sinhVal = Math.sinh(rad);
        const coshVal = Math.cosh(rad);
        const tanhVal = Math.tanh(rad);

        const formatVal = (v) => isNaN(v) ? 'Undefined' : Math.abs(v) < 1e-12 ? '0.0000' : v.toFixed(4);

        const setTxt = (id, txt) => {
            const el = document.getElementById(id);
            if (el) el.textContent = txt;
        };

        setTxt('resSin', formatVal(sinVal));
        setTxt('resCos', formatVal(cosVal));
        setTxt('resTan', formatVal(tanVal));
        setTxt('resCsc', formatVal(cscVal));
        setTxt('resSec', formatVal(secVal));
        setTxt('resCot', formatVal(cotVal));

        setTxt('resSinh', formatVal(sinhVal));
        setTxt('resCosh', formatVal(coshVal));
        setTxt('resTanh', formatVal(tanhVal));

        const exact = exactTrigValues[normDeg];
        setTxt('exactSin', exact ? exact.sin : '');
        setTxt('exactCos', exact ? exact.cos : '');
        setTxt('exactTan', exact ? exact.tan : '');
        setTxt('exactCsc', exact ? exact.csc : '');
        setTxt('exactSec', exact ? exact.sec : '');
        setTxt('exactCot', exact ? exact.cot : '');

        setTxt('unitCoordsBadge', `(x: ${formatVal(cosVal)}, y: ${formatVal(sinVal)})`);
    }

    function drawUnitCircle() {
        const canvas = document.getElementById('unitCircleCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        const cx = width / 2;
        const cy = height / 2;
        const radius = 110;

        ctx.clearRect(0, 0, width, height);

        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const axisColor = isDark ? '#475569' : '#cbd5e1';
        const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.05)';
        const textColor = isDark ? '#94a3b8' : '#475569';

        // Background guide
        ctx.strokeStyle = gridColor;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(cx, cy, radius * 0.5, 0, 2 * Math.PI);
        ctx.stroke();

        // Axes
        ctx.strokeStyle = axisColor;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(15, cy);
        ctx.lineTo(width - 15, cy);
        ctx.moveTo(cx, 15);
        ctx.lineTo(cx, height - 15);
        ctx.stroke();

        // Labels
        ctx.fillStyle = textColor;
        ctx.font = '11px sans-serif';
        ctx.fillText('+X (cos)', width - 48, cy - 8);
        ctx.fillText('+Y (sin)', cx + 8, 25);
        ctx.fillText('(1, 0)', cx + radius + 4, cy - 6);
        ctx.fillText('(0, 1)', cx + 4, cy - radius - 6);
        ctx.fillText('(-1, 0)', cx - radius - 36, cy - 6);
        ctx.fillText('(0, -1)', cx + 4, cy + radius + 14);

        // Unit Circle
        ctx.strokeStyle = isDark ? '#38bdf8' : '#0284c7';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, radius, 0, 2 * Math.PI);
        ctx.stroke();

        // Point
        const rad = state.currentTrigAngleDeg * (Math.PI / 180);
        const px = cx + radius * Math.cos(rad);
        const py = cy - radius * Math.sin(rad);

        // Cosine Projection (Blue)
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(px, cy);
        ctx.stroke();

        // Sine Projection (Green)
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(px, cy);
        ctx.lineTo(px, py);
        ctx.stroke();

        // Hypotenuse (Pink)
        ctx.strokeStyle = '#ec4899';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(px, py);
        ctx.stroke();

        // Arc
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(cx, cy, 32, 0, -rad, true);
        ctx.stroke();

        // Point
        ctx.fillStyle = '#f8fafc';
        ctx.beginPath();
        ctx.arc(px, py, 6, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#ec4899';
        ctx.lineWidth = 2.5;
        ctx.stroke();
    }

    // =========================================================
    // 11. LOGARITHM SUITE & STEP SOLVER (ROBUST NUMERIC PARSING)
    // =========================================================
    function parseMathInput(str) {
        if (!str) return NaN;
        const trimmed = str.toString().trim().toLowerCase();
        if (trimmed === 'e') return Math.E;
        if (trimmed === 'pi' || trimmed === 'π') return Math.PI;
        return parseFloat(trimmed);
    }

    function initLogarithms() {
        const argInput = document.getElementById('logArgInput');
        const baseInput = document.getElementById('logBaseInput');
        const calcBtn = document.getElementById('calcLogBtn');
        const resultContainer = document.getElementById('logStepResult');
        const presetChips = document.querySelectorAll('.quick-log-bases button');

        if (!argInput || !baseInput || !calcBtn || !resultContainer) return;

        presetChips.forEach(chip => {
            chip.addEventListener('click', () => {
                const baseVal = chip.dataset.logBase;
                baseInput.value = baseVal;
                calculateLog();
            });
        });

        function calculateLog() {
            const rawArg = argInput.value.trim();
            const rawBase = baseInput.value.trim();

            const arg = parseMathInput(rawArg);
            const base = parseMathInput(rawBase);

            if (isNaN(arg) || isNaN(base)) {
                resultContainer.innerHTML = `<div class="error-msg">Please enter valid numeric values for Argument and Base (e.g. 100, 10, e, 2).</div>`;
                return;
            }

            if (arg <= 0) {
                resultContainer.innerHTML = `<div class="error-msg"><strong>Domain Error:</strong> Argument x must be strictly positive (x &gt; 0). Given: ${arg}</div>`;
                return;
            }

            if (base <= 0 || Math.abs(base - 1) < 1e-12) {
                resultContainer.innerHTML = `<div class="error-msg"><strong>Base Error:</strong> Base b must be strictly positive and cannot equal 1 (b &gt; 0, b ≠ 1). Given: ${base}</div>`;
                return;
            }

            const lnArg = Math.log(arg);
            const lnBase = Math.log(base);
            const logResult = lnArg / lnBase;

            const baseDisplay = Math.abs(base - Math.E) < 1e-6 ? 'e' : base;
            const logNotation = baseDisplay === 'e' ? `ln(${arg})` : base === 10 ? `log₁₀(${arg})` : base === 2 ? `log₂(${arg})` : `log<sub>${base}</sub>(${arg})`;

            resultContainer.innerHTML = `
                <div class="step-header-banner">
                    <span class="step-badge-title">LOGARITHM STEP-BY-STEP CALCULATION</span>
                    <span class="badge">${logNotation}</span>
                </div>
                <div class="arithmetic-step-box">
<strong>Given:</strong>
  Argument (x) = ${arg}
  Base (b)     = ${baseDisplay}

<strong>Formula (Change of Base):</strong>
  log<sub>b</sub>(x) = ln(x) / ln(b) = log₁₀(x) / log₁₀(b)

<strong>Steps:</strong>
  Step 1: Calculate natural log of argument:
          ln(${arg}) = ${lnArg.toFixed(6)}

  Step 2: Calculate natural log of base:
          ln(${baseDisplay}) = ${lnBase.toFixed(6)}

  Step 3: Divide Step 1 by Step 2:
          ${logNotation} = ${lnArg.toFixed(6)} ÷ ${lnBase.toFixed(6)}
          = <strong>${logResult.toFixed(6)}</strong>

<strong>Verification (Exponential Form):</strong>
  b<sup>result</sup> = (${baseDisplay})<sup>${logResult.toFixed(4)}</sup> = ${Math.pow(base, logResult).toFixed(4)} ≈ ${arg}

<strong>Therefore:</strong>
  FINAL ANSWER: ${logResult.toFixed(6)}
                </div>
                <div class="final-answer-card">
                    <div>
                        <div class="final-answer-title">FINAL LOGARITHMIC ANSWER</div>
                        <div class="text-muted">${logNotation}</div>
                    </div>
                    <div class="final-answer-value">${logResult.toFixed(6)}</div>
                </div>
            `;

            drawLogGraph(arg, base, logResult);
        }

        calcBtn.addEventListener('click', calculateLog);
        argInput.addEventListener('input', calculateLog);
        baseInput.addEventListener('input', calculateLog);

        calculateLog();
    }

    function drawLogGraph(activeX = 100, activeBase = 10, activeY = 2) {
        const canvas = document.getElementById('logGraphCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        ctx.clearRect(0, 0, width, height);

        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const axisColor = isDark ? '#475569' : '#cbd5e1';
        const textColor = isDark ? '#94a3b8' : '#475569';

        const originX = 40;
        const originY = height / 2 + 30;

        // Axes
        ctx.strokeStyle = axisColor;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(originX, 15);
        ctx.lineTo(originX, height - 15);
        ctx.moveTo(15, originY);
        ctx.lineTo(width - 15, originY);
        ctx.stroke();

        ctx.fillStyle = textColor;
        ctx.font = '10px monospace';
        ctx.fillText('x=0', originX - 25, 25);
        ctx.fillText('+X', width - 25, originY - 6);
        ctx.fillText('+Y', originX + 6, 25);
        ctx.fillText('(1,0)', originX + 28, originY + 14);

        const scaleX = (width - originX - 30) / 10;
        const scaleY = 32;

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        let started = false;
        for (let px = 1; px <= width - originX - 20; px += 2) {
            const mathX = px / scaleX;
            if (mathX <= 0) continue;

            const mathY = Math.log(mathX) / Math.log(activeBase > 0 && activeBase !== 1 ? activeBase : 10);
            const canvasY = originY - mathY * scaleY;

            if (canvasY >= 10 && canvasY <= height - 10) {
                if (!started) {
                    ctx.moveTo(originX + px, canvasY);
                    started = true;
                } else {
                    ctx.lineTo(originX + px, canvasY);
                }
            }
        }
        ctx.stroke();

        // Intercept (1,0)
        const interceptX = originX + 1 * scaleX;
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(interceptX, originY, 4, 0, 2 * Math.PI);
        ctx.fill();

        const coordBadge = document.getElementById('logCoordBadge');
        if (coordBadge) {
            coordBadge.textContent = `Point: (${activeX}, ${isNaN(activeY) ? '?' : activeY.toFixed(3)})`;
        }
    }

    // =========================================================
    // 12. PRACTICE & QUIZ
    // =========================================================
    function initQuiz() {
        const promptElem = document.getElementById('quizPrompt');
        const optionsGrid = document.getElementById('quizOptions');
        const feedbackBox = document.getElementById('quizFeedback');
        const feedbackText = document.getElementById('feedbackText');
        const nextBtn = document.getElementById('quizNextBtn');
        const scoreElem = document.getElementById('quizScore');
        const streakElem = document.getElementById('quizStreak');

        if (!promptElem || !optionsGrid || !feedbackBox || !nextBtn) return;

        function generateQuizQuestion() {
            feedbackBox.style.display = 'none';
            optionsGrid.innerHTML = '';

            const types = ['dec2bin', 'bin2dec', 'hex2dec', 'binAdd', 'trigBasic', 'logBasic'];
            const chosenType = types[Math.floor(Math.random() * types.length)];

            let questionText = '';
            let correctAnswer = '';
            let options = [];

            if (chosenType === 'dec2bin') {
                const dec = Math.floor(Math.random() * 63) + 1;
                questionText = `Convert Decimal <span class="text-accent">${dec}</span> to Binary:`;
                correctAnswer = dec.toString(2);
                options = [correctAnswer, (dec + 1).toString(2), (dec - 1 > 0 ? dec - 1 : dec + 2).toString(2), (dec ^ 3).toString(2)];
            } else if (chosenType === 'bin2dec') {
                const dec = Math.floor(Math.random() * 31) + 1;
                const bin = dec.toString(2);
                questionText = `Convert Binary <span class="text-accent">${bin}₂</span> to Decimal:`;
                correctAnswer = dec.toString();
                options = [correctAnswer, (dec + 2).toString(), (dec - 2 > 0 ? dec - 2 : dec + 4).toString(), (dec + 1).toString()];
            } else if (chosenType === 'hex2dec') {
                const dec = Math.floor(Math.random() * 255) + 1;
                const hex = dec.toString(16).toUpperCase();
                questionText = `Convert Hexadecimal <span class="text-accent">0x${hex}</span> to Decimal:`;
                correctAnswer = dec.toString();
                options = [correctAnswer, (dec + 16).toString(), (dec - 10 > 0 ? dec - 10 : dec + 8).toString(), (dec + 5).toString()];
            } else if (chosenType === 'binAdd') {
                const a = Math.floor(Math.random() * 15) + 1;
                const b = Math.floor(Math.random() * 15) + 1;
                questionText = `Add binary: <span class="text-accent">${a.toString(2)}₂ + ${b.toString(2)}₂</span>:`;
                correctAnswer = (a + b).toString(2);
                options = [correctAnswer, (a + b + 1).toString(2), (a + b - 1 > 0 ? a + b - 1 : a + b + 2).toString(2), ((a ^ b)).toString(2)];
            } else if (chosenType === 'trigBasic') {
                const trigQuestions = [
                    { q: 'What is sin(30°)?', a: '1/2', opts: ['1/2', '√3/2', '√2/2', '1'] },
                    { q: 'What is cos(60°)?', a: '1/2', opts: ['1/2', '√3/2', '0', '1'] },
                    { q: 'What is tan(45°)?', a: '1', opts: ['1', '0', '√3', 'Undefined'] },
                    { q: 'What is sin(90°)?', a: '1', opts: ['1', '0', '-1', '1/2'] },
                    { q: 'What is cos(0°)?', a: '1', opts: ['1', '0', '-1', 'Undefined'] }
                ];
                const tq = trigQuestions[Math.floor(Math.random() * trigQuestions.length)];
                questionText = `<span class="text-accent">${tq.q}</span>`;
                correctAnswer = tq.a;
                options = [...tq.opts];
            } else if (chosenType === 'logBasic') {
                const logQuestions = [
                    { q: 'What is log₂(64)?', a: '6', opts: ['6', '5', '8', '32'] },
                    { q: 'What is log₁₀(1000)?', a: '3', opts: ['3', '2', '4', '100'] },
                    { q: 'What is log₂(256)?', a: '8', opts: ['8', '7', '16', '64'] },
                    { q: 'What is log₅(125)?', a: '3', opts: ['3', '2', '5', '25'] },
                    { q: 'What is ln(1)?', a: '0', opts: ['0', '1', 'e', 'Undefined'] }
                ];
                const lq = logQuestions[Math.floor(Math.random() * logQuestions.length)];
                questionText = `<span class="text-accent">${lq.q}</span>`;
                correctAnswer = lq.a;
                options = [...lq.opts];
            }

            options = Array.from(new Set(options));
            while (options.length < 4) {
                options.push((Math.floor(Math.random() * 50)).toString(2));
                options = Array.from(new Set(options));
            }

            options.sort(() => Math.random() - 0.5);

            state.quiz.currentQuestion = { text: questionText, correctAnswer: correctAnswer };
            promptElem.innerHTML = questionText;

            options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'quiz-option-btn';
                btn.textContent = opt;
                btn.addEventListener('click', () => handleOptionClick(btn, opt, correctAnswer));
                optionsGrid.appendChild(btn);
            });
        }

        function handleOptionClick(selectedBtn, chosenOpt, correctOpt) {
            const allBtns = optionsGrid.querySelectorAll('.quiz-option-btn');
            allBtns.forEach(btn => btn.disabled = true);

            const isCorrect = chosenOpt === correctOpt;

            if (isCorrect) {
                selectedBtn.classList.add('correct');
                state.quiz.score += 10;
                state.quiz.streak += 1;
                if (feedbackText) feedbackText.innerHTML = `🎉 <strong>Correct!</strong> Great job! (+10 pts)`;
            } else {
                selectedBtn.classList.add('wrong');
                state.quiz.streak = 0;
                allBtns.forEach(btn => {
                    if (btn.textContent === correctOpt) btn.classList.add('correct');
                });
                if (feedbackText) feedbackText.innerHTML = `❌ <strong>Not quite!</strong> Correct answer was <code>${correctOpt}</code>.`;
            }

            if (scoreElem) scoreElem.textContent = state.quiz.score;
            if (streakElem) streakElem.textContent = `${state.quiz.streak} 🔥`;
            feedbackBox.style.display = 'flex';
        }

        nextBtn.addEventListener('click', generateQuizQuestion);
        generateQuizQuestion();
    }
});
