package command;

import command.CustomerServices;
import command.fx.Command;

public class AddCustomerCommand implements Command {
    private CustomerServices services;

    public AddCustomerCommand(CustomerServices services) {
        this.services = services;
    }

    @Override
    public void execute() {
        services.addCustomer();
    }
}
