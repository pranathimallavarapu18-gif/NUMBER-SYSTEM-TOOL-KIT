#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

class NumberSystem {
public:

    // =====================================================
    // 1. DECIMAL TO BINARY
    // =====================================================
    void decimalToBinary(int decimal) {

        if (decimal == 0) {
            cout << "\n----- DECIMAL TO BINARY -----\n";
            cout << "\nProcess:\n";
            cout << "0 is already 0 in Binary.\n";
            cout << "\nTherefore:\n";
            cout << "0 in Decimal = 0 in Binary\n";
            cout << "FINAL ANSWER: 0\n";
            return;
        }

        if (decimal < 0) {
            cout << "Please enter a positive decimal number.\n";
            return;
        }

        int original = decimal;
        int binary[32];
        int i = 0;

        cout << "\n----- DECIMAL TO BINARY -----\n";
        cout << "\nProcess:\n\n";

        int step = 1;

        while (decimal > 0) {

            int quotient = decimal / 2;
            int remainder = decimal % 2;

            cout << "Step " << step << ":\n";
            cout << decimal << " / 2 = " << quotient << "\n";
            cout << "Remainder = " << remainder << "\n\n";

            binary[i] = remainder;
            decimal = quotient;
            i++;
            step++;
        }

        cout << "Now read the remainders from bottom to top:\n";

        for (int j = i - 1; j >= 0; j--) {
            cout << binary[j] << " ";
        }

        cout << "\n\nTherefore:\n";
        cout << original << " in Decimal = ";

        for (int j = i - 1; j >= 0; j--) {
            cout << binary[j];
        }

        cout << " in Binary\n";

        cout << "FINAL ANSWER: ";

        for (int j = i - 1; j >= 0; j--) {
            cout << binary[j];
        }

        cout << "\n";
    }


    // =====================================================
    // 2. DECIMAL TO OCTAL
    // =====================================================
    void decimalToOctal(int decimal) {

        if (decimal == 0) {
            cout << "\n----- DECIMAL TO OCTAL -----\n";
            cout << "\nProcess:\n";
            cout << "0 is already 0 in Octal.\n";
            cout << "\nTherefore:\n";
            cout << "0 in Decimal = 0 in Octal\n";
            cout << "FINAL ANSWER: 0\n";
            return;
        }

        if (decimal < 0) {
            cout << "Please enter a positive decimal number.\n";
            return;
        }

        int original = decimal;
        int octal[32];
        int i = 0;

        cout << "\n----- DECIMAL TO OCTAL -----\n";
        cout << "\nProcess:\n\n";

        int step = 1;

        while (decimal > 0) {

            int quotient = decimal / 8;
            int remainder = decimal % 8;

            cout << "Step " << step << ":\n";
            cout << decimal << " / 8 = " << quotient << "\n";
            cout << "Remainder = " << remainder << "\n\n";

            octal[i] = remainder;
            decimal = quotient;
            i++;
            step++;
        }

        cout << "Now read the remainders from bottom to top:\n";

        for (int j = i - 1; j >= 0; j--) {
            cout << octal[j] << " ";
        }

        cout << "\n\nTherefore:\n";
        cout << original << " in Decimal = ";

        for (int j = i - 1; j >= 0; j--) {
            cout << octal[j];
        }

        cout << " in Octal\n";

        cout << "FINAL ANSWER: ";

        for (int j = i - 1; j >= 0; j--) {
            cout << octal[j];
        }

        cout << "\n";
    }


    // =====================================================
    // 3. DECIMAL TO HEXADECIMAL
    // =====================================================
    void decimalToHexadecimal(int decimal) {

        if (decimal == 0) {
            cout << "\n----- DECIMAL TO HEXADECIMAL -----\n";
            cout << "\nProcess:\n";
            cout << "0 is already 0 in Hexadecimal.\n";
            cout << "\nTherefore:\n";
            cout << "0 in Decimal = 0 in Hexadecimal\n";
            cout << "FINAL ANSWER: 0\n";
            return;
        }

        if (decimal < 0) {
            cout << "Please enter a positive decimal number.\n";
            return;
        }

        int original = decimal;

        char hex[] = "0123456789ABCDEF";
        char result[32];

        int i = 0;

        cout << "\n----- DECIMAL TO HEXADECIMAL -----\n";
        cout << "\nProcess:\n\n";

        int step = 1;

        while (decimal > 0) {

            int quotient = decimal / 16;
            int remainder = decimal % 16;

            cout << "Step " << step << ":\n";
            cout << decimal << " / 16 = " << quotient << "\n";
            cout << "Remainder = " << remainder;

            if (remainder >= 10) {
                cout << " (" << hex[remainder] << ")";
            }

            cout << "\n\n";

            result[i] = hex[remainder];

            decimal = quotient;
            i++;
            step++;
        }

        cout << "Now read the remainders from bottom to top:\n";

        for (int j = i - 1; j >= 0; j--) {
            cout << result[j] << " ";
        }

        cout << "\n\nTherefore:\n";
        cout << original << " in Decimal = ";

        for (int j = i - 1; j >= 0; j--) {
            cout << result[j];
        }

        cout << " in Hexadecimal\n";

        cout << "FINAL ANSWER: ";

        for (int j = i - 1; j >= 0; j--) {
            cout << result[j];
        }

        cout << "\n";
    }


    // =====================================================
    // 4. BINARY TO DECIMAL
    // =====================================================
    void binaryToDecimal(string binary) {

        if (!isBinary(binary)) {
            cout << "\nInvalid Binary Number!\n";
            return;
        }

        int decimal = 0;
        int power = 1;

        cout << "\n----- BINARY TO DECIMAL -----\n";
        cout << "\nProcess:\n\n";

        cout << binary << "\n";

        cout << " ";

        for (int i = 0; i < (int)binary.length(); i++) {
            cout << "?";
        }

        cout << "\n ";

        int totalPositions = (int)binary.length();

        for (int i = totalPositions - 1; i >= 0; i--) {
            cout << "2^" << i << " ";
        }

        cout << "\n\n";

        for (int i = (int)binary.length() - 1; i >= 0; i--) {

            int digit = binary[i] - '0';

            int value = digit * power;

            cout << digit << " × 2^" << ((int)binary.length() - 1 - i)
                 << " = " << value << "\n";

            decimal = decimal + value;
            power = power * 2;
        }

        cout << "\nAdd the values:\n";

        for (int i = 0; i < (int)binary.length(); i++) {

            int digit = binary[i] - '0';
            int exponent = (int)binary.length() - 1 - i;

            int value = digit;

            for (int j = 0; j < exponent; j++) {
                value = value * 2;
            }

            cout << value;

            if (i != (int)binary.length() - 1) {
                cout << " + ";
            }
        }

        cout << " = " << decimal << "\n";

        cout << "\nTherefore:\n";
        cout << binary << " in Binary = "
             << decimal << " in Decimal\n";

        cout << "FINAL ANSWER: " << decimal << "\n";
    }


    // =====================================================
    // 5. OCTAL TO DECIMAL
    // =====================================================
    void octalToDecimal(string octal) {

        if (!isOctal(octal)) {
            cout << "\nInvalid Octal Number!\n";
            return;
        }

        int decimal = 0;
        int power = 1;

        cout << "\n----- OCTAL TO DECIMAL -----\n";
        cout << "\nProcess:\n\n";

        for (int i = (int)octal.length() - 1; i >= 0; i--) {

            int digit = octal[i] - '0';
            int position = (int)octal.length() - 1 - i;

            int value = digit * power;

            cout << digit << " × 8^" << position
                 << " = " << value << "\n";

            decimal = decimal + value;
            power = power * 8;
        }

        cout << "\nAdd the values:\n";

        for (int i = 0; i < (int)octal.length(); i++) {

            int digit = octal[i] - '0';
            int exponent = (int)octal.length() - 1 - i;

            int value = digit;

            for (int j = 0; j < exponent; j++) {
                value = value * 8;
            }

            cout << value;

            if (i != (int)octal.length() - 1) {
                cout << " + ";
            }
        }

        cout << " = " << decimal << "\n";

        cout << "\nTherefore:\n";
        cout << octal << " in Octal = "
             << decimal << " in Decimal\n";

        cout << "FINAL ANSWER: " << decimal << "\n";
    }


    // =====================================================
    // 6. HEXADECIMAL TO DECIMAL
    // =====================================================
    void hexadecimalToDecimal(string hex) {

        if (!isHexadecimal(hex)) {
            cout << "\nInvalid Hexadecimal Number!\n";
            return;
        }

        int decimal = 0;
        int power = 1;

        cout << "\n----- HEXADECIMAL TO DECIMAL -----\n";
        cout << "\nProcess:\n\n";

        for (int i = (int)hex.length() - 1; i >= 0; i--) {

            char c = toupper(hex[i]);

            int value;

            if (c >= '0' && c <= '9') {
                value = c - '0';
            }
            else {
                value = c - 'A' + 10;
            }

            int position = (int)hex.length() - 1 - i;

            int calculated = value * power;

            cout << c << " × 16^" << position
                 << " = " << calculated << "\n";

            decimal = decimal + calculated;
            power = power * 16;
        }

        cout << "\nAdd the values:\n";

        for (int i = 0; i < (int)hex.length(); i++) {

            char c = toupper(hex[i]);

            int value;

            if (c >= '0' && c <= '9') {
                value = c - '0';
            }
            else {
                value = c - 'A' + 10;
            }

            int exponent = (int)hex.length() - 1 - i;

            int calculated = value;

            for (int j = 0; j < exponent; j++) {
                calculated = calculated * 16;
            }

            cout << calculated;

            if (i != (int)hex.length() - 1) {
                cout << " + ";
            }
        }

        cout << " = " << decimal << "\n";

        cout << "\nTherefore:\n";
        cout << hex << " in Hexadecimal = "
             << decimal << " in Decimal\n";

        cout << "FINAL ANSWER: " << decimal << "\n";
    }


    // =====================================================
    // DECIMAL ADDITION
    // =====================================================
    void decimalAddition(int a, int b) {

        cout << "\n----- ADDITION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First number  = " << a << "\n";
        cout << "Second number = " << b << "\n\n";

        cout << "Formula:\n";
        cout << "Addition = First number + Second number\n\n";

        cout << "Calculation:\n\n";

        cout << "  " << a << "\n";
        cout << "+ " << b << "\n";
        cout << "----------------\n";
        cout << "  " << a + b << "\n";

        cout << "\nTherefore:\n";
        cout << "FINAL ANSWER: " << a + b << "\n";
    }


    // =====================================================
    // DECIMAL SUBTRACTION
    // =====================================================
    void decimalSubtraction(int a, int b) {

        cout << "\n----- SUBTRACTION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First number  = " << a << "\n";
        cout << "Second number = " << b << "\n\n";

        cout << "Formula:\n";
        cout << "Subtraction = First number - Second number\n\n";

        cout << "Calculation:\n\n";

        cout << "  " << a << "\n";
        cout << "- " << b << "\n";
        cout << "----------------\n";
        cout << "  " << a - b << "\n";

        cout << "\nTherefore:\n";
        cout << "FINAL ANSWER: " << a - b << "\n";
    }


    // =====================================================
    // DECIMAL MULTIPLICATION
    // =====================================================
    void decimalMultiplication(int a, int b) {

        cout << "\n----- MULTIPLICATION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First number  = " << a << "\n";
        cout << "Second number = " << b << "\n\n";

        cout << "Formula:\n";
        cout << "Multiplication = First number × Second number\n\n";

        cout << "Calculation:\n\n";

        cout << "  " << a << "\n";
        cout << "× " << b << "\n";
        cout << "----------------\n";
        cout << "  " << a * b << "\n";

        cout << "\nTherefore:\n";
        cout << "FINAL ANSWER: " << a * b << "\n";
    }


    // =====================================================
    // DECIMAL DIVISION
    // =====================================================
    void decimalDivision(int a, int b) {

        cout << "\n----- DIVISION -----\n";

        if (b == 0) {
            cout << "\nDivision by zero is not allowed.\n";
            return;
        }

        double result = (double)a / b;

        cout << "\nProcess:\n\n";

        cout << "Dividend = " << a << "\n";
        cout << "Divisor  = " << b << "\n\n";

        cout << "Formula:\n";
        cout << "Division = Dividend / Divisor\n\n";

        cout << "Calculation:\n";
        cout << a << " / " << b << " = " << result << "\n";

        cout << "\nTherefore:\n";
        cout << "FINAL ANSWER: " << result << "\n";
    }


    // =====================================================
    // DECIMAL MODULUS
    // =====================================================
    void decimalModulus(int a, int b) {

        cout << "\n----- MODULUS -----\n";

        if (b == 0) {
            cout << "\nModulus by zero is not allowed.\n";
            return;
        }

        int result = a % b;

        cout << "\nProcess:\n\n";

        cout << "Dividend = " << a << "\n";
        cout << "Divisor  = " << b << "\n\n";

        cout << "Formula:\n";
        cout << "Remainder = Dividend % Divisor\n\n";

        cout << "Calculation:\n";
        cout << a << " % " << b << " = " << result << "\n";

        cout << "\nTherefore:\n";
        cout << "FINAL ANSWER: " << result << "\n";
    }


    // =====================================================
    // BINARY ADDITION
    // =====================================================
    void binaryAddition(string a, string b) {

        if (!isBinary(a) || !isBinary(b)) {
            cout << "\nInvalid Binary Number!\n";
            return;
        }

        int decimalA = binaryToDecimalValue(a);
        int decimalB = binaryToDecimalValue(b);

        int sum = decimalA + decimalB;

        cout << "\n----- BINARY ADDITION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First binary number  = " << a << "\n";
        cout << "Second binary number = " << b << "\n\n";

        cout << "Convert to Decimal:\n";
        cout << a << " = " << decimalA << "\n";
        cout << b << " = " << decimalB << "\n\n";

        cout << "Decimal calculation:\n";
        cout << decimalA << " + " << decimalB
             << " = " << sum << "\n\n";

        cout << "Convert " << sum << " back to Binary:\n";
        cout << sum << " = ";
        printBinary(sum);

        cout << "\n\nTherefore:\n";
        cout << a << " + " << b << " = ";
        printBinary(sum);

        cout << "\nFINAL ANSWER: ";
        printBinary(sum);
        cout << "\n";
    }


    // =====================================================
    // BINARY SUBTRACTION
    // =====================================================
    void binarySubtraction(string a, string b) {

        if (!isBinary(a) || !isBinary(b)) {
            cout << "\nInvalid Binary Number!\n";
            return;
        }

        int decimalA = binaryToDecimalValue(a);
        int decimalB = binaryToDecimalValue(b);

        if (decimalA < decimalB) {
            cout << "\nFor this simple toolkit, first number should be greater.\n";
            return;
        }

        int difference = decimalA - decimalB;

        cout << "\n----- BINARY SUBTRACTION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First binary number  = " << a << "\n";
        cout << "Second binary number = " << b << "\n\n";

        cout << "Convert to Decimal:\n";
        cout << a << " = " << decimalA << "\n";
        cout << b << " = " << decimalB << "\n\n";

        cout << "Decimal calculation:\n";
        cout << decimalA << " - " << decimalB
             << " = " << difference << "\n\n";

        cout << "Convert " << difference << " back to Binary:\n";
        cout << difference << " = ";
        printBinary(difference);

        cout << "\n\nTherefore:\n";
        cout << a << " - " << b << " = ";
        printBinary(difference);

        cout << "\nFINAL ANSWER: ";
        printBinary(difference);
        cout << "\n";
    }


    // =====================================================
    // BINARY MULTIPLICATION
    // =====================================================
    void binaryMultiplication(string a, string b) {

        if (!isBinary(a) || !isBinary(b)) {
            cout << "\nInvalid Binary Number!\n";
            return;
        }

        int decimalA = binaryToDecimalValue(a);
        int decimalB = binaryToDecimalValue(b);

        int result = decimalA * decimalB;

        cout << "\n----- BINARY MULTIPLICATION -----\n";

        cout << "\nProcess:\n\n";

        cout << "First binary number  = " << a << "\n";
        cout << "Second binary number = " << b << "\n\n";

        cout << "Convert to Decimal:\n";
        cout << a << " = " << decimalA << "\n";
        cout << b << " = " << decimalB << "\n\n";

        cout << "Decimal calculation:\n";
        cout << decimalA << " × " << decimalB
             << " = " << result << "\n\n";

        cout << "Convert " << result << " back to Binary:\n";
        cout << result << " = ";
        printBinary(result);

        cout << "\n\nTherefore:\n";
        cout << a << " × " << b << " = ";
        printBinary(result);

        cout << "\nFINAL ANSWER: ";
        printBinary(result);
        cout << "\n";
    }


    // =====================================================
    // BINARY DIVISION
    // =====================================================
    void binaryDivision(string a, string b) {

        if (!isBinary(a) || !isBinary(b)) {
            cout << "\nInvalid Binary Number!\n";
            return;
        }

        int decimalA = binaryToDecimalValue(a);
        int decimalB = binaryToDecimalValue(b);

        if (decimalB == 0) {
            cout << "\nDivision by zero is not allowed.\n";
            return;
        }

        int result = decimalA / decimalB;

        cout << "\n----- BINARY DIVISION -----\n";

        cout << "\nProcess:\n\n";

        cout << "Dividend = " << a << "\n";
        cout << "Divisor  = " << b << "\n\n";

        cout << "Convert to Decimal:\n";
        cout << a << " = " << decimalA << "\n";
        cout << b << " = " << decimalB << "\n\n";

        cout << "Decimal calculation:\n";
        cout << decimalA << " / " << decimalB
             << " = " << result << "\n\n";

        cout << "Convert " << result << " back to Binary:\n";
        cout << result << " = ";
        printBinary(result);

        cout << "\n\nTherefore:\n";
        cout << a << " / " << b << " = ";
        printBinary(result);

        cout << "\nFINAL ANSWER: ";
        printBinary(result);
        cout << "\n";
    }


    // =====================================================
    // NUMBER VALIDATION
    // =====================================================
    void validateNumber() {

        int choice;
        string number;

        cout << "\n--------------------------------------------\n";
        cout << "           NUMBER VALIDATION\n";
        cout << "--------------------------------------------\n";

        cout << "1. Binary\n";
        cout << "2. Octal\n";
        cout << "3. Hexadecimal\n";
        cout << "4. Back\n";

        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 4) {
            return;
        }

        cout << "Enter number: ";
        cin >> number;

        cout << "\nProcess:\n\n";

        if (choice == 1) {

            cout << "Checking every digit of " << number
                 << "...\n";

            if (isBinary(number))
                cout << "\nFINAL ANSWER: Valid Binary Number\n";
            else
                cout << "\nFINAL ANSWER: Invalid Binary Number\n";
        }

        else if (choice == 2) {

            cout << "Checking every digit of " << number
                 << "...\n";

            if (isOctal(number))
                cout << "\nFINAL ANSWER: Valid Octal Number\n";
            else
                cout << "\nFINAL ANSWER: Invalid Octal Number\n";
        }

        else if (choice == 3) {

            cout << "Checking every digit of " << number
                 << "...\n";

            if (isHexadecimal(number))
                cout << "\nFINAL ANSWER: Valid Hexadecimal Number\n";
            else
                cout << "\nFINAL ANSWER: Invalid Hexadecimal Number\n";
        }

        else {
            cout << "Invalid choice!\n";
        }
    }


    // =====================================================
    // CHECK BINARY
    // =====================================================
    bool isBinary(string number) {

        if (number.empty())
            return false;

        for (int i = 0; i < (int)number.length(); i++) {

            char c = number[i];

            if (c != '0' && c != '1')
                return false;
        }

        return true;
    }


    // =====================================================
    // CHECK OCTAL
    // =====================================================
    bool isOctal(string number) {

        if (number.empty())
            return false;

        for (int i = 0; i < (int)number.length(); i++) {

            char c = number[i];

            if (c < '0' || c > '7')
                return false;
        }

        return true;
    }


    // =====================================================
    // CHECK HEXADECIMAL
    // =====================================================
    bool isHexadecimal(string number) {

        if (number.empty())
            return false;

        for (int i = 0; i < (int)number.length(); i++) {

            char c = number[i];

            c = toupper(c);

            if (!((c >= '0' && c <= '9') ||
                  (c >= 'A' && c <= 'F'))) {

                return false;
            }
        }

        return true;
    }


private:

    // =====================================================
    // BINARY TO DECIMAL - INTERNAL FUNCTION
    // =====================================================
    int binaryToDecimalValue(string binary) {

        int decimal = 0;

        for (int i = 0; i < (int)binary.length(); i++) {

            char c = binary[i];

            decimal = decimal * 2 + (c - '0');
        }

        return decimal;
    }


    // =====================================================
    // DECIMAL TO BINARY - INTERNAL FUNCTION
    // =====================================================
    void printBinary(int number) {

        if (number == 0) {
            cout << "0";
            return;
        }

        int binary[32];
        int i = 0;

        while (number > 0) {

            binary[i] = number % 2;
            number = number / 2;
            i++;
        }

        for (int j = i - 1; j >= 0; j--) {
            cout << binary[j];
        }
    }
};


// =========================================================
// MAIN FUNCTION
// =========================================================

int main() {

    NumberSystem ns;

    int choice;

    do {

        cout << "\n\n";
        cout << "============================================\n";
        cout << "          NUMBER SYSTEM TOOLKIT\n";
        cout << "============================================\n";

        cout << "1. Number System Conversion\n";
        cout << "2. Decimal Arithmetic\n";
        cout << "3. Binary Arithmetic\n";
        cout << "4. Number Validation\n";
        cout << "5. Exit\n";

        cout << "============================================\n";

        cout << "Enter your choice: ";
        cin >> choice;


        // =================================================
        // OPTION 1 - NUMBER SYSTEM CONVERSION
        // =================================================

        if (choice == 1) {

            int conversionChoice;

            do {

                cout << "\n--------------------------------------------\n";
                cout << "        NUMBER SYSTEM CONVERSION\n";
                cout << "--------------------------------------------\n";

                cout << "1. Decimal to Binary\n";
                cout << "2. Decimal to Octal\n";
                cout << "3. Decimal to Hexadecimal\n";
                cout << "4. Binary to Decimal\n";
                cout << "5. Octal to Decimal\n";
                cout << "6. Hexadecimal to Decimal\n";
                cout << "7. Back\n";

                cout << "--------------------------------------------\n";

                cout << "Enter your choice: ";
                cin >> conversionChoice;


                // DECIMAL TO BINARY
                if (conversionChoice == 1) {

                    int decimal;

                    cout << "\nEnter decimal number: ";
                    cin >> decimal;

                    ns.decimalToBinary(decimal);
                }


                // DECIMAL TO OCTAL
                else if (conversionChoice == 2) {

                    int decimal;

                    cout << "\nEnter decimal number: ";
                    cin >> decimal;

                    ns.decimalToOctal(decimal);
                }


                // DECIMAL TO HEXADECIMAL
                else if (conversionChoice == 3) {

                    int decimal;

                    cout << "\nEnter decimal number: ";
                    cin >> decimal;

                    ns.decimalToHexadecimal(decimal);
                }


                // BINARY TO DECIMAL
                else if (conversionChoice == 4) {

                    string binary;

                    cout << "\nEnter binary number: ";
                    cin >> binary;

                    ns.binaryToDecimal(binary);
                }


                // OCTAL TO DECIMAL
                else if (conversionChoice == 5) {

                    string octal;

                    cout << "\nEnter octal number: ";
                    cin >> octal;

                    ns.octalToDecimal(octal);
                }


                // HEXADECIMAL TO DECIMAL
                else if (conversionChoice == 6) {

                    string hex;

                    cout << "\nEnter hexadecimal number: ";
                    cin >> hex;

                    ns.hexadecimalToDecimal(hex);
                }


                // BACK
                else if (conversionChoice == 7) {

                    cout << "\nReturning to main menu...\n";
                }


                else {

                    cout << "\nInvalid choice! Please try again.\n";
                }

            } while (conversionChoice != 7);
        }


        // =================================================
        // OPTION 2 - DECIMAL ARITHMETIC
        // =================================================

        else if (choice == 2) {

            int operation;

            do {

                cout << "\n--------------------------------------------\n";
                cout << "             DECIMAL ARITHMETIC\n";
                cout << "--------------------------------------------\n";

                cout << "1. Addition\n";
                cout << "2. Subtraction\n";
                cout << "3. Multiplication\n";
                cout << "4. Division\n";
                cout << "5. Modulus\n";
                cout << "6. Back\n";

                cout << "--------------------------------------------\n";

                cout << "Enter your choice: ";
                cin >> operation;


                if (operation >= 1 && operation <= 5) {

                    int a, b;

                    cout << "\nEnter first number: ";
                    cin >> a;

                    cout << "Enter second number: ";
                    cin >> b;


                    if (operation == 1) {
                        ns.decimalAddition(a, b);
                    }

                    else if (operation == 2) {
                        ns.decimalSubtraction(a, b);
                    }

                    else if (operation == 3) {
                        ns.decimalMultiplication(a, b);
                    }

                    else if (operation == 4) {
                        ns.decimalDivision(a, b);
                    }

                    else if (operation == 5) {
                        ns.decimalModulus(a, b);
                    }
                }


                else if (operation == 6) {

                    cout << "\nReturning to main menu...\n";
                }


                else {

                    cout << "\nInvalid choice! Please try again.\n";
                }

            } while (operation != 6);
        }


        // =================================================
        // OPTION 3 - BINARY ARITHMETIC
        // =================================================

        else if (choice == 3) {

            int operation;

            do {

                cout << "\n--------------------------------------------\n";
                cout << "             BINARY ARITHMETIC\n";
                cout << "--------------------------------------------\n";

                cout << "1. Binary Addition\n";
                cout << "2. Binary Subtraction\n";
                cout << "3. Binary Multiplication\n";
                cout << "4. Binary Division\n";
                cout << "5. Back\n";

                cout << "--------------------------------------------\n";

                cout << "Enter your choice: ";
                cin >> operation;


                if (operation >= 1 && operation <= 4) {

                    string a, b;

                    cout << "\nEnter first binary number: ";
                    cin >> a;

                    cout << "Enter second binary number: ";
                    cin >> b;


                    if (operation == 1) {
                        ns.binaryAddition(a, b);
                    }

                    else if (operation == 2) {
                        ns.binarySubtraction(a, b);
                    }

                    else if (operation == 3) {
                        ns.binaryMultiplication(a, b);
                    }

                    else if (operation == 4) {
                        ns.binaryDivision(a, b);
                    }
                }


                else if (operation == 5) {

                    cout << "\nReturning to main menu...\n";
                }


                else {

                    cout << "\nInvalid choice! Please try again.\n";
                }

            } while (operation != 5);
        }


        // =================================================
        // OPTION 4 - NUMBER VALIDATION
        // =================================================

        else if (choice == 4) {

            ns.validateNumber();
        }


        // =================================================
        // OPTION 5 - EXIT
        // =================================================

        else if (choice == 5) {

            cout << "\nThank you for using Number System Toolkit!\n";
        }


        // =================================================
        // INVALID MAIN MENU CHOICE
        // =================================================

        else {

            cout << "\nInvalid choice! Please try again.\n";
        }

    } while (choice != 5);


    return 0;
}
