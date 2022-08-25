import command.*;

import editor.*;
import observer.Chart;
import observer.DataSource;
import observer.SpreadSheet;

public class Main {
    public static void main(String[] args){
    var dataSource =new DataSource();
    var sheet1= new SpreadSheet();
    var sheet2= new SpreadSheet();
    var chart = new Chart();


    dataSource.addObserver(sheet1);
    dataSource.addObserver(sheet2);
    dataSource.addObserver(chart);
    dataSource.setValue(1);




    }
}
