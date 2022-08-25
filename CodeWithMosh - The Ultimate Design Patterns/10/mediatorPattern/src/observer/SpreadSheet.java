package observer;

public class SpreadSheet implements Observer{
    private DataSource dataSource;

    public SpreadSheet(DataSource dataSource) {
        this.dataSource = dataSource;
    }


    @Override
    public void update() {
        System.out.println("Spread sheet got notified" + dataSource.getValue());
    }
}
