package chainOfRersponsibility;

public abstract class Handler {
    private Handler next;

    public Handler(Handler next) {
        this.next = next;
    }

    public void handler(HttpRequest request){
        if(doHandle(request))
            return;
        if(next!=null)
            next.handler(request);
    }

    public abstract boolean doHandle(HttpRequest request);
}
