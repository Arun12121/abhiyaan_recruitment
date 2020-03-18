//Assumed that the input is a valid expression, abd both the numbers and results willbe integers
#include <bits/stdc++.h>   

using namespace std; 

void showstack(stack <int> s) 
{ 
    while (!s.empty()) 
    { 
        cout << '\t' << s.top(); 
        s.pop(); 
    } 
    cout << '\n'; 
} 

int precedence(char op){ 
    if(op == '+'||op == '-') 
    return 1; 
    if(op == '*'||op == '/') 
    return 2; 
    return 0; 
} 
 
int operation(int a, int b, char op){ 
    switch(op){ 
        case '-': return a - b;
        case '+': return a + b;
        case '*': return a * b;
        case '/': return a / b;
    } 
} 

int evaluator(string s)
{
    stack <int> numbers;
    stack <char> ops;
    
    int i;
    for(i = 0; i < s.length(); i++)
    {
        if(s[i] == ' ')
            continue;
        else if(s[i] == '('){
            ops.push(s[i]);
        }
        else if(isdigit(s[i]))
        {
            int val = 0;
            while(i < s.length() && isdigit(s[i]))  //for multiple digits
            {
                val = 10*val + s[i] - '0';
                i++;
            }
            numbers.push(val);
        }
        else if(s[i] == ')') 
        { 
            while(!ops.empty() && ops.top() != '(') 
            { 
                int a = numbers.top(); 
                numbers.pop(); 
                  
                int b = numbers.top(); 
                numbers.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                numbers.push(operation(b, a, op)); 
            } 
            
            if(!ops.empty())    // pop opening brace
               ops.pop();
        }
        else
        { 
            while(!ops.empty() && precedence(ops.top()) >= precedence(s[i]))
            { 
                int a = numbers.top(); 
                numbers.pop(); 
                  
                int b = numbers.top(); 
                numbers.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                numbers.push(operation(b, a, op));
            }
            ops.push(s[i]);
        } 
    }
    return numbers.top(); 
}

int main()
{
    string s;
    getline(cin, s);
    s = "( " + s + " )";
    cout<<evaluator(s);
}


