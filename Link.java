public class Link {
    public Link next;
    public Object data;

    public Link(Object dataIn, Link nextIn){
        this.data = dataIn;
        this.next = nextIn;
    }

    public Link(Link nextIn){
        this.data = null;
        this.next = nextIn;
    }

    Object getData(){
        return data;
    }
    void setData(Object newData){
        data = newData;
    }

    Link getNext(){
        return next;
    }

    void setNext(Link newNext){
        next = newNext;
    }
}
