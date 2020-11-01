package stack;


public class stack<T> {
	private stackItem firstItem;
	public int size;
	stack(){
		this.firstItem = null;
		this.size = 0;
	}
	public T push(T key) {
		// if null is pushed, throw error
		if (key == null) throw new IllegalArgumentException("Cannot provide null as argument");
		if (this.firstItem == null) {
			this.firstItem = new stackItem(key,null);
			this.size ++;
		}
		else {
			stackItem tmp = new stackItem(key,this.firstItem);
			this.firstItem = tmp;
			this.size ++;
		}
		return (T)this.firstItem.getKey();
	}
	public T top() {
		if (this.size == 0) throw new ArrayIndexOutOfBoundsException("Cannot get top of empty stack.");
		return (T)this.firstItem.getKey();
	}
	public T pop() {
		if (this.size == 0)  throw new ArrayIndexOutOfBoundsException("Cannot pop from empty stack.");
		stackItem tmp = this.firstItem;
		this.firstItem = this.firstItem.prevItem;
		this.size --;
		return (T)tmp.getKey();
	}
	public boolean empty() {
		return this.size == 0;	
	}
}
