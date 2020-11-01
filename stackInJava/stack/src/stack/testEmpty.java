package stack;

import static org.junit.Assert.*;

import org.junit.Test;

public class testEmpty {
		@Test
		public void testEmptyWithMultiplePush() {
			stack<String> myObj =  new stack<>();
			String output = myObj.push("(");
			output = myObj.push("{");
			boolean myEmpty = myObj.empty();
			assertEquals(false,myEmpty);
		}
		@Test
		public void testEmptyWithEmptyStack() {
			stack<String> myObj =  new stack<>();
			boolean myEmpty = myObj.empty();
			assertEquals(true,myEmpty);
		}
}
