package stack;

import static org.junit.Assert.*;


import org.junit.Test;

public class pushTest {

	@Test
	public void testPushString() {
		stack<String> myObj =  new stack<>();
		String output = myObj.push("{");
		assertEquals("{",output);
	}
	@Test(expected = IllegalArgumentException.class)
	public void testIllegalArgument() {
		stack<String> myObj2 =  new stack<>();
		String output = myObj2.push(null);
	}
}
