import strategy.BlackAndWhiteFilter;
import strategy.ImageStorage;
import strategy.JpegCompressor;
import strategy.PngCompressor;
import template.TransferMoneyTask;

public class Main {
    public static void main(String[] args){

      var transferMoney = new TransferMoneyTask();
        transferMoney.execute();
    }
}
