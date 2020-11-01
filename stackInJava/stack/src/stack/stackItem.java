package stack;

public class stackItem <T>{
	public stackItem prevItem;
	private T val;
	stackItem(T key,stackItem prevItem){
		this.val = key;
		this.prevItem = prevItem;
	}
	public T getKey() {
		return this.val;
	}
	public void setNextItem(stackItem myStackItem) {
		this.prevItem = myStackItem;
	}
	public void setKey(T key) {
		this.val = key;
	}
}
