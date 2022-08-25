package observer;

public class SpreadSheet implements Observer{
    @Override
    public void update(int value) {
        System.out.println("Spread sheet got notified" + value);
    }
}
