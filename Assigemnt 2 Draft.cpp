d
#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

int evaluatePostfix(const string& expression, unordered_map<string, int>& variables) {
    stack<int> st;

    string token;
    for (char c : expression) {
        if (c == ' ') {
            if (!token.empty()) {
                if (isdigit(token[0])) {
                    st.push(stoi(token));
                } else {
                    st.push(variables[token]);
                }
                token.clear();
            }
        } else {
            token += c;
        }
    }

    return st.top();
}

int main() {
    char choice;
    do {
        string postfix;
        cout << "Enter a postfix expression with a $ at the end: ";
        getline(cin, postfix, '$');
        
        unordered_map<string, int> variables;
        string token;
        cout << "Enter the value of each variable (separated by space): ";
        getline(cin, token);
        size_t pos = 0;
        while ((pos = token.find(' ')) != string::npos) {
            string var = token.substr(0, pos);
            token.erase(0, pos + 1);
            int value;
            cout << "Enter the value of " << var << ": ";
            cin >> value;
            variables[var] = value;
        }
        if (!token.empty()) {
            int value;
            cout << "Enter the value of " << token << ": ";
            cin >> value;
            variables[token] = value;
        }

        cin.ignore(); // Consume newline character

        int result = evaluatePostfix(postfix, variables);
        cout << "Expression's value is " << result << endl;

        cout << "CONTINUE(y/n)? ";
        cin >> choice;
        cin.ignore(); // Consume newline character
    } while (choice == 'y' || choice == 'Y');

    return 0;
}
