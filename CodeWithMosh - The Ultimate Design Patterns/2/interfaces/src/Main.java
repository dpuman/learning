public class Main {

    public static void main(String[] args){
        TaxCalculator calculator = getCalculator();
        float value=calculator.calculateTax();

        System.out.println(calculator.calculateTax());

    }
    public static TaxCalculator getCalculator(){
        return new TaxCalculator2019();
    }
}
