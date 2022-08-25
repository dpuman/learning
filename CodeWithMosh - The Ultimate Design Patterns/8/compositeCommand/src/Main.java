import command.*;
import command.fx.Button;

public class Main {
    public static void main(String[] args){

        var compositCommand = new CompositeCommand();

        compositCommand.add(new ResizeCommand());
        compositCommand.add(new BlackAndWhiteCommand());
        compositCommand.execute();
    }
}
