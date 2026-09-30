#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <algorithm>

using namespace std;

const double PI = 3.14159265358979323846;

// ============================================================
//                    NUMBER SYSTEM TOOLKIT
// ============================================================

// Convert character to digit
int charToDigit(char c)
{
    if (c >= '0' && c <= '9')
        return c - '0';

    if (c >= 'A' && c <= 'F')
        return c - 'A' + 10;

    if (c >= 'a' && c <= 'f')
        return c - 'a' + 10;

    return -1;
}

// Convert digit to character
char digitToChar(int d)
{
    if (d < 10)
        return char('0' + d);

    return char('A' + d - 10);
}

// Check whether number is valid for the given base
bool isValidNumber(string s, int base)
{
    if (s.length() == 0)
        return false;

    int start = 0;

    if (s[0] == '-')
    {
        if (s.length() == 1)
            return false;

        start = 1;
    }

    for (int i = start; i < (int)s.length(); i++)
    {
        int d = charToDigit(s[i]);

        if (d < 0 || d >= base)
            return false;
    }

    return true;
}

// ============================================================
//                 BASE NUMBER TO DECIMAL
// ============================================================

long long toDecimal(string number, int base)
{
    bool negative = false;

    if (number[0] == '-')
    {
        negative = true;
        number = number.substr(1);
    }

    long long decimal = 0;

    // OLD STYLE FOR LOOP
    for (int i = 0; i < (int)number.length(); i++)
    {
        char c = number[i];

        int digit = charToDigit(c);

        decimal = decimal * base + digit;
    }

    if (negative)
        return -decimal;

    return decimal;
}

// ============================================================
//                 DECIMAL TO ANY BASE
// ============================================================

string fromDecimal(long long decimal, int base)
{
    if (decimal == 0)
        return "0";

    bool negative = false;

    if (decimal < 0)
    {
        negative = true;
        decimal = -decimal;
    }

    string result = "";

    while (decimal > 0)
    {
        int remainder = decimal % base;

        result = result + digitToChar(remainder);

        decimal = decimal / base;
    }

    reverse(result.begin(), result.end());

    if (negative)
        result = "-" + result;

    return result;
}

// ============================================================
//                 DECIMAL TO BINARY
// ============================================================

void decimalToBinarySteps(long long n)
{
    cout << "\n========== DECIMAL TO BINARY ==========\n";
    cout << "Input: " << n << "\n\n";

    if (n == 0)
    {
        cout << "0 in binary = 0\n";
        return;
    }

    long long value = n;

    if (value < 0)
        value = -value;

    string result = "";

    cout << "Repeated division by 2:\n\n";

    while (value > 0)
    {
        long long quotient = value / 2;
        long long remainder = value % 2;

        cout << value << " / 2 = "
             << quotient << " remainder "
             << remainder << "\n";

        result = result + char('0' + remainder);

        value = quotient;
    }

    reverse(result.begin(), result.end());

    if (n < 0)
        result = "-" + result;

    cout << "\nRead the remainders from bottom to top.\n";

    cout << "Answer: " << n
         << "(10) = "
         << result
         << "(2)\n";
}

// ============================================================
//                 DECIMAL TO OCTAL
// ============================================================

void decimalToOctalSteps(long long n)
{
    cout << "\n========== DECIMAL TO OCTAL ==========\n";
    cout << "Input: " << n << "\n\n";

    long long value = n;

    if (value < 0)
        value = -value;

    if (value == 0)
    {
        cout << "Answer: 0(10) = 0(8)\n";
        return;
    }

    string result = "";

    cout << "Repeated division by 8:\n\n";

    while (value > 0)
    {
        long long quotient = value / 8;
        long long remainder = value % 8;

        cout << value << " / 8 = "
             << quotient << " remainder "
             << remainder << "\n";

        result = result + char('0' + remainder);

        value = quotient;
    }

    reverse(result.begin(), result.end());

    if (n < 0)
        result = "-" + result;

    cout << "\nAnswer: " << n
         << "(10) = "
         << result
         << "(8)\n";
}

// ============================================================
//                 DECIMAL TO HEXADECIMAL
// ============================================================

void decimalToHexSteps(long long n)
{
    cout << "\n========== DECIMAL TO HEXADECIMAL ==========\n";
    cout << "Input: " << n << "\n\n";

    long long value = n;

    if (value < 0)
        value = -value;

    if (value == 0)
    {
        cout << "Answer: 0(10) = 0(H)\n";
        return;
    }

    string result = "";

    cout << "Repeated division by 16:\n\n";

    while (value > 0)
    {
        long long quotient = value / 16;
        long long remainder = value % 16;

        cout << value << " / 16 = "
             << quotient << " remainder "
             << remainder
             << " ("
             << digitToChar(remainder)
             << ")\n";

        result = result + digitToChar(remainder);

        value = quotient;
    }

    reverse(result.begin(), result.end());

    if (n < 0)
        result = "-" + result;

    cout << "\nAnswer: " << n
         << "(10) = "
         << result
         << "(16)\n";
}

// ============================================================
//                 ANY BASE TO DECIMAL
// ============================================================

void baseToDecimalSteps(string number, int base, string baseName)
{
    cout << "\n========== "
         << baseName
         << " TO DECIMAL ==========\n";

    cout << "Input: " << number << "\n\n";

    bool negative = false;

    if (number[0] == '-')
    {
        negative = true;
        number = number.substr(1);
    }

    cout << "Using positional expansion:\n\n";

    long long result = 0;

    int power = number.length() - 1;

    // OLD STYLE FOR LOOP
    for (int i = 0; i < (int)number.length(); i++)
    {
        char c = number[i];

        int digit = charToDigit(c);

        cout << digit
             << " x "
             << base
             << "^"
             << power;

        long long contribution =
            digit * (long long)pow(base, power);

        cout << " = "
             << contribution
             << "\n";

        result = result + contribution;

        power--;
    }

    if (negative)
        result = -result;

    cout << "\nAnswer: "
         << result
         << "(10)\n";
}

// ============================================================
//                 NUMBER SYSTEM CONVERSION
// ============================================================

void conversionModule()
{
    int choice;

    do
    {
        cout << "\n========================================\n";
        cout << "       NUMBER SYSTEM CONVERSION\n";
        cout << "========================================\n";

        cout << "1. Binary to Decimal\n";
        cout << "2. Binary to Octal\n";
        cout << "3. Binary to Hexadecimal\n";
        cout << "4. Decimal to Binary\n";
        cout << "5. Decimal to Octal\n";
        cout << "6. Decimal to Hexadecimal\n";
        cout << "7. Octal to Binary\n";
        cout << "8. Octal to Decimal\n";
        cout << "9. Octal to Hexadecimal\n";
        cout << "10. Hexadecimal to Binary\n";
        cout << "11. Hexadecimal to Decimal\n";
        cout << "12. Hexadecimal to Octal\n";
        cout << "13. Back to Main Menu\n";

        cout << "\nEnter choice: ";
        cin >> choice;

        string number;

        switch (choice)
        {
        case 1:

            cout << "Enter Binary number: ";
            cin >> number;

            if (!isValidNumber(number, 2))
            {
                cout << "Invalid Binary number!\n";
                break;
            }

            baseToDecimalSteps(number, 2, "BINARY");

            break;

        case 2:

            cout << "Enter Binary number: ";
            cin >> number;

            if (!isValidNumber(number, 2))
            {
                cout << "Invalid Binary number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 2);

                cout << "\nBinary -> Decimal -> Octal\n";

                cout << "Binary = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Octal = "
                     << fromDecimal(decimal, 8)
                     << "\n";
            }

            break;

        case 3:

            cout << "Enter Binary number: ";
            cin >> number;

            if (!isValidNumber(number, 2))
            {
                cout << "Invalid Binary number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 2);

                cout << "\nBinary -> Decimal -> Hexadecimal\n";

                cout << "Binary = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Hexadecimal = "
                     << fromDecimal(decimal, 16)
                     << "\n";
            }

            break;

        case 4:
        {
            long long n;

            cout << "Enter Decimal number: ";
            cin >> n;

            decimalToBinarySteps(n);

            break;
        }

        case 5:
        {
            long long n;

            cout << "Enter Decimal number: ";
            cin >> n;

            decimalToOctalSteps(n);

            break;
        }

        case 6:
        {
            long long n;

            cout << "Enter Decimal number: ";
            cin >> n;

            decimalToHexSteps(n);

            break;
        }

        case 7:

            cout << "Enter Octal number: ";
            cin >> number;

            if (!isValidNumber(number, 8))
            {
                cout << "Invalid Octal number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 8);

                cout << "\nOctal -> Decimal -> Binary\n";

                cout << "Octal = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Binary = "
                     << fromDecimal(decimal, 2)
                     << "\n";
            }

            break;

        case 8:

            cout << "Enter Octal number: ";
            cin >> number;

            if (!isValidNumber(number, 8))
            {
                cout << "Invalid Octal number!\n";
                break;
            }

            baseToDecimalSteps(number, 8, "OCTAL");

            break;

        case 9:

            cout << "Enter Octal number: ";
            cin >> number;

            if (!isValidNumber(number, 8))
            {
                cout << "Invalid Octal number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 8);

                cout << "\nOctal = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Hexadecimal = "
                     << fromDecimal(decimal, 16)
                     << "\n";
            }

            break;

        case 10:

            cout << "Enter Hexadecimal number: ";
            cin >> number;

            if (!isValidNumber(number, 16))
            {
                cout << "Invalid Hexadecimal number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 16);

                cout << "\nHexadecimal = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Binary = "
                     << fromDecimal(decimal, 2)
                     << "\n";
            }

            break;

        case 11:

            cout << "Enter Hexadecimal number: ";
            cin >> number;

            if (!isValidNumber(number, 16))
            {
                cout << "Invalid Hexadecimal number!\n";
                break;
            }

            baseToDecimalSteps(
                number,
                16,
                "HEXADECIMAL"
            );

            break;

        case 12:

            cout << "Enter Hexadecimal number: ";
            cin >> number;

            if (!isValidNumber(number, 16))
            {
                cout << "Invalid Hexadecimal number!\n";
                break;
            }

            {
                long long decimal = toDecimal(number, 16);

                cout << "\nHexadecimal = "
                     << number
                     << "\n";

                cout << "Decimal = "
                     << decimal
                     << "\n";

                cout << "Octal = "
                     << fromDecimal(decimal, 8)
                     << "\n";
            }

            break;

        case 13:

            cout << "Returning to main menu...\n";

            break;

        default:

            cout << "Invalid choice!\n";
        }

    } while (choice != 13);
}

// ============================================================
//                 ARITHMETIC MODULE
// ============================================================

void arithmeticModule()
{
    int choice;

    double a, b;

    cout << "\n========================================\n";
    cout << "          ARITHMETIC OPERATIONS\n";
    cout << "========================================\n";

    cout << "1. Addition\n";
    cout << "2. Subtraction\n";
    cout << "3. Multiplication\n";
    cout << "4. Division\n";

    cout << "\nEnter choice: ";
    cin >> choice;

    cout << "Enter first number: ";
    cin >> a;

    cout << "Enter second number: ";
    cin >> b;

    cout << fixed << setprecision(4);

    switch (choice)
    {
    case 1:

        cout << "\nFormula: a + b\n";

        cout << "Step: "
             << a
             << " + "
             << b
             << "\n";

        cout << "Answer = "
             << a + b
             << "\n";

        break;

    case 2:

        cout << "\nFormula: a - b\n";

        cout << "Step: "
             << a
             << " - "
             << b
             << "\n";

        cout << "Answer = "
             << a - b
             << "\n";

        break;

    case 3:

        cout << "\nFormula: a x b\n";

        cout << "Step: "
             << a
             << " x "
             << b
             << "\n";

        cout << "Answer = "
             << a * b
             << "\n";

        break;

    case 4:

        if (b == 0)
        {
            cout << "\nError: Division by zero is not allowed.\n";
        }
        else
        {
            cout << "\nFormula: a / b\n";

            cout << "Step: "
                 << a
                 << " / "
                 << b
                 << "\n";

            cout << "Answer = "
                 << a / b
                 << "\n";
        }

        break;

    default:

        cout << "Invalid choice!\n";
    }
}

// ============================================================
//                      FACTORIAL
// ============================================================

void factorialModule()
{
    int n;

    cout << "\n========================================\n";
    cout << "              FACTORIAL\n";
    cout << "========================================\n";

    cout << "Enter a non-negative integer: ";

    cin >> n;

    if (n < 0)
    {
        cout << "Factorial is not defined for negative numbers.\n";
        return;
    }

    unsigned long long result = 1;

    cout << "\nFormula:\n";

    cout << n << "! = ";

    if (n == 0)
    {
        cout << "1\n";

        cout << "\nAnswer: 0! = 1\n";

        return;
    }

    for (int i = n; i >= 1; i--)
    {
        cout << i;

        if (i != 1)
            cout << " x ";

        result = result * i;
    }

    cout << "\n\nCalculation:\n";

    unsigned long long temp = 1;

    for (int i = 1; i <= n; i++)
    {
        temp = temp * i;

        cout << "Step "
             << i
             << ": "
             << temp
             << "\n";
    }

    cout << "\nAnswer: "
         << n
         << "! = "
         << result
         << "\n";
}

// ============================================================
//                      EXPONENTIAL
// ============================================================

void exponentialModule()
{
    double base;
    double exponent;

    cout << "\n========================================\n";
    cout << "             EXPONENTIAL\n";
    cout << "========================================\n";

    cout << "Enter base: ";
    cin >> base;

    cout << "Enter exponent: ";
    cin >> exponent;

    double answer = pow(base, exponent);

    cout << "\nFormula:\n";

    cout << "a^b = "
         << base
         << "^"
         << exponent
         << "\n";

    if (exponent >= 0 &&
        exponent == (int)exponent &&
        exponent <= 20)
    {
        int e = (int)exponent;

        cout << "\nStep-by-step:\n";

        if (e == 0)
        {
            cout << "Any non-zero number raised to 0 = 1\n";
        }
        else
        {
            double result = 1;

            for (int i = 1; i <= e; i++)
            {
                result = result * base;

                cout << "Step "
                     << i
                     << ": "
                     << result
                     << "\n";
            }
        }
    }
    else
    {
        cout << "\nUsing exponential calculation:\n";

        cout << "e^(b x ln(a))\n";
    }

    cout << fixed << setprecision(6);

    cout << "\nAnswer: "
         << base
         << "^"
         << exponent
         << " = "
         << answer
         << "\n";
}

// ============================================================
//                      LOGARITHMIC
// ============================================================

void logarithmicModule()
{
    int choice;

    double x;
    double base;

    cout << "\n========================================\n";
    cout << "             LOGARITHMIC\n";
    cout << "========================================\n";

    cout << "1. Natural Logarithm ln(x)\n";
    cout << "2. Common Logarithm log10(x)\n";
    cout << "3. Logarithm with any base\n";

    cout << "\nEnter choice: ";
    cin >> choice;

    cout << "Enter x: ";
    cin >> x;

    if (x <= 0)
    {
        cout << "Error: x must be greater than 0.\n";
        return;
    }

    cout << fixed << setprecision(6);

    switch (choice)
    {
    case 1:
    {
        double answer = log(x);

        cout << "\nFormula:\n";

        cout << "ln(x) = loge(x)\n";

        cout << "\nln("
             << x
             << ") = "
             << answer
             << "\n";

        cout << "\nAnswer = "
             << answer
             << "\n";

        break;
    }

    case 2:
    {
        double answer = log10(x);

        cout << "\nFormula:\n";

        cout << "log10(x)\n";

        cout << "\nlog10("
             << x
             << ") = "
             << answer
             << "\n";

        cout << "\nAnswer = "
             << answer
             << "\n";

        break;
    }

    case 3:
    {
        cout << "Enter base: ";
        cin >> base;

        if (base <= 0 || base == 1)
        {
            cout << "Invalid base.\n";
            cout << "Base must be greater than 0 and not equal to 1.\n";
            return;
        }

        double answer = log(x) / log(base);

        cout << "\nFormula:\n";

        cout << "log_b(x) = ln(x) / ln(b)\n";

        cout << "\nlog_"
             << base
             << "("
             << x
             << ") = ln("
             << x
             << ") / ln("
             << base
             << ")\n";

        cout << "\nAnswer = "
             << answer
             << "\n";

        break;
    }

    default:

        cout << "Invalid choice!\n";
    }
}

// ============================================================
//                   TRIGONOMETRIC
// ============================================================

void trigonometricModule()
{
    int choice;

    double angle;

    cout << "\n========================================\n";
    cout << "          TRIGONOMETRIC FUNCTIONS\n";
    cout << "========================================\n";

    cout << "1. sin(x)\n";
    cout << "2. cos(x)\n";
    cout << "3. tan(x)\n";
    cout << "4. sin^-1(x)\n";
    cout << "5. cos^-1(x)\n";
    cout << "6. tan^-1(x)\n";

    cout << "\nEnter choice: ";
    cin >> choice;

    cout << "Enter angle/value: ";
    cin >> angle;

    cout << fixed << setprecision(6);

    switch (choice)
    {
    case 1:
    {
        double radians =
            angle * PI / 180.0;

        double answer = sin(radians);

        cout << "\nFormula:\n";

        cout << "sin(theta)\n";

        cout << "\nRadians = "
             << angle
             << " x PI / 180\n";

        cout << "Radians = "
             << radians
             << "\n";

        cout << "\nsin("
             << angle
             << " degrees) = "
             << answer
             << "\n";

        cout << "\nAnswer = "
             << answer
             << "\n";

        break;
    }

    case 2:
    {
        double radians =
            angle * PI / 180.0;

        double answer = cos(radians);

        cout << "\nFormula:\n";

        cout << "cos(theta)\n";

        cout << "\nRadians = "
             << angle
             << " x PI / 180\n";

        cout << "Radians = "
             << radians
             << "\n";

        cout << "\ncos("
             << angle
             << " degrees) = "
             << answer
             << "\n";

        cout << "\nAnswer = "
             << answer
             << "\n";

        break;
    }

    case 3:
    {
        double radians =
            angle * PI / 180.0;

        if (fabs(cos(radians)) < 1e-10)
        {
            cout << "\ntan("
                 << angle
                 << " degrees) is undefined.\n";

            return;
        }

        double answer = tan(radians);

        cout << "\nFormula:\n";

        cout << "tan(theta) = sin(theta) / cos(theta)\n";

        cout << "\nRadians = "
             << angle
             << " x PI / 180\n";

        cout << "Radians = "
             << radians
             << "\n";

        cout << "\nAnswer: tan("
             << angle
             << " degrees) = "
             << answer
             << "\n";

        break;
    }

    case 4:

        if (angle < -1 || angle > 1)
        {
            cout << "Input must be between -1 and 1.\n";
            return;
        }

        cout << "\nFormula:\n";

        cout << "theta = sin^-1(x)\n";

        cout << "\nResult in radians = "
             << asin(angle)
             << "\n";

        cout << "Result in degrees = "
             << asin(angle) * 180.0 / PI
             << "\n";

        break;

    case 5:

        if (angle < -1 || angle > 1)
        {
            cout << "Input must be between -1 and 1.\n";
            return;
        }

        cout << "\nFormula:\n";

        cout << "theta = cos^-1(x)\n";

        cout << "\nResult in radians = "
             << acos(angle)
             << "\n";

        cout << "Result in degrees = "
             << acos(angle) * 180.0 / PI
             << "\n";

        break;

    case 6:

        cout << "\nFormula:\n";

        cout << "theta = tan^-1(x)\n";

        cout << "\nResult in radians = "
             << atan(angle)
             << "\n";

        cout << "Result in degrees = "
             << atan(angle) * 180.0 / PI
             << "\n";

        break;

    default:

        cout << "Invalid choice!\n";
    }
}

// ============================================================
//                         MAIN
// ============================================================

int main()
{
    int choice;

    do
    {
        cout << "\n\n";
        cout << "============================================\n";
        cout << "          NUMBER SYSTEM TOOLKIT\n";
        cout << "============================================\n";

        cout << "1. Number System Conversion\n";
        cout << "2. Arithmetic Operations\n";
        cout << "3. Factorial\n";
        cout << "4. Exponential\n";
        cout << "5. Logarithmic Functions\n";
        cout << "6. Trigonometric Functions\n";
        cout << "7. Exit\n";

        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:

            conversionModule();

            break;

        case 2:

            arithmeticModule();

            break;

        case 3:

            factorialModule();

            break;

        case 4:

            exponentialModule();

            break;

        case 5:

            logarithmicModule();

            break;

        case 6:

            trigonometricModule();

            break;

        case 7:

            cout << "\nThank you for using Number System Toolkit!\n";

            break;

        default:

            cout << "\nInvalid choice! Please try again.\n";
        }

    } while (choice != 7);

    return 0;
}
