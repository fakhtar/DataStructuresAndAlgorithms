package stack;

import static org.junit.Assert.*;

import org.junit.Test;

public class testPop {
		@Test
		public void testPopWithMultiplePushes() {
			stack<String> myObj =  new stack<>();
			String output = myObj.push("(");
			output = myObj.push("{");
			String myPop = myObj.pop();
			assertEquals("{",myPop);
			myPop = myObj.pop();
			assertEquals("(",myPop);
		}
		@Test(expected = ArrayIndexOutOfBoundsException.class)
		public void testPopWithEmptyStack() {
			stack<String> myObj =  new stack<>();
			String myPop = myObj.top();
		}
}
