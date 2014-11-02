import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

/**
 * Created by bl02515 on 14-7-29.
 * <p/>
 * RPN表达式模拟
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * <p/>
 * Valid operators are +, -, *, /. Each operand may be an integer or another expression.
 * <p/>
 * Some examples:
 * ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 * ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 */
public class RPNEmulator {

    private static final HashSet<String> OPERATORS = new HashSet<String>(
            Arrays.asList("+", "-", "*", "/"));

    public int evalRPN(String[] tokens) {
        if (tokens == null || tokens.length == 0) {
            throw new IllegalArgumentException("the tokens can't be empty");
        }

        Stack<Integer> rpnStack = new Stack<Integer>();
        for (String token : tokens) {
            if (OPERATORS.contains(token)) {
                int right = rpnStack.pop();
                int left = rpnStack.pop();
                rpnStack.push(calc(left, right, token));
            }
            else {
                rpnStack.push(new Integer(token));
            }
        }
        return rpnStack.pop();
    }

    private Integer calc(int left, int right, String operator) {
        if (!OPERATORS.contains(operator)) {
            throw new IllegalArgumentException("the operator is invalid");
        }

        if (operator.equals("+")) {
            return left + right;
        }
        else if (operator.equals("-")) {
            return left - right;
        }
        else if (operator.equals("*")) {
            return left * right;
        }
        else if (operator.equals("/")) {
            return left / right;
        }

        throw new RuntimeException("it must be something I don't know yet!!!");
    }

    public static void main(String[] args) {
        RPNEmulator emulator = new RPNEmulator();
        int resultA = emulator.evalRPN(new String[] { "2", "1", "+", "3", "*" });
        assert (9 == resultA);
        int resultB = emulator.evalRPN(new String[] { "4", "13", "5", "/", "+" });
        assert (6 == resultB);
    }
}
