package stack;

import static org.junit.Assert.*;

import org.junit.Test;

public class testTop {
		@Test
		public void testTopWithMultiplePushes() {
			stack<String> myObj =  new stack<>();
			String output = myObj.push("(");
			output = myObj.push("{");
			String myTop = myObj.top();
			assertEquals("{",myTop);
		}
		@Test(expected = ArrayIndexOutOfBoundsException.class)
		public void testTopWithEmptyStack() {
			stack<String> myObj =  new stack<>();
			String myTop = myObj.top();
		}
}
