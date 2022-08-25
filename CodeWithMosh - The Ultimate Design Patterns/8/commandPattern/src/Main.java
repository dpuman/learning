import command.CustomerServices;
import command.AddCustomerCommand;
import command.fx.Button;

public class Main {
    public static void main(String[] args){

     var services = new CustomerServices();
     var command =new AddCustomerCommand(services);
     var button =new Button(command);
     button.click();
    }
}
