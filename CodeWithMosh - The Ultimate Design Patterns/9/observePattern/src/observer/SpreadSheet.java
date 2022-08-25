package observer;

public class SpreadSheet implements Observer{
    @Override
    public void update() {
        System.out.println("Spread sheet got notified");
    }
}
