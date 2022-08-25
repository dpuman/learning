package mediator;

import java.util.ArrayList;
import java.util.List;

public class UIControl {
    private List<Observer> observers =new ArrayList<>();

    public void  attatch(Observer observer){
        observers.add(observer);
    }

    protected void notifyObservers(){
        for (var observer:observers)
            observer.update();
    }

}
