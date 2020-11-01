package stack;

public class main {

	public static void main(String[] args) {
		String myString = "{{{}}}()(){}{}{}[][(]";
		System.out.println(isBalanced(myString));
	}
	
	public static boolean isBalanced(String stringToBeChecked) {
		// TODO Auto-generated method stub
		stack myStack = new stack();
		for (int i = 0; i < stringToBeChecked.length(); i++) {
			if (stringToBeChecked.charAt(i) == '(' || stringToBeChecked.charAt(i) == '{' || stringToBeChecked.charAt(i) == '[') {
				myStack.push(stringToBeChecked.charAt(i));
				continue;
			}
			char myTop;
			if (stringToBeChecked.charAt(i) == ')') {
				// get Top. If top is not ( then return false. if top gives error then return false
				// if get top gives an error then it is not balanced
				try {
					myTop = (char)myStack.pop();
				}
				catch (Exception e){
					return false;
				}
				if(myTop != '(') {
					return false;
				}
				continue;
			}
			if (stringToBeChecked.charAt(i) == '}') {
				// get Top. If top is not ( then return false. if top gives error then return false
				// if get top gives an error then it is not balanced
				try {
					myTop = (char)myStack.pop();
				}
				catch (Exception e){
					return false;
				}
				if(myTop != '{') {
					return false;
				}
				continue;
			}
			if (stringToBeChecked.charAt(i) == ']') {
				// get Top. If top is not ( then return false. if top gives error then return false
				// if get top gives an error then it is not balanced
				try {
					myTop = (char)myStack.pop();
				}
				catch (Exception e){
					return false;
				}
				if(myTop != '[') {
					return false;
				}
				continue;
			}
		}
		if (myStack.size != 0) {
			return false;
		}
		return true;
	}
}
