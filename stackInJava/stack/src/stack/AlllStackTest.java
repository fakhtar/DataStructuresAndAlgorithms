package stack;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;

@RunWith(Suite.class)
@SuiteClasses({ pushTest.class, testEmpty.class, testPop.class, testTop.class })
public class AlllStackTest {

}
