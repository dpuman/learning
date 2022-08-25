import command.*;

import editor.*;

public class Main {
    public static void main(String[] args){
    var history =new History();
    var document =new HtmlDocument();
    document.setContent("Hello world");

    var boldCommand =new BoldCommand(document,history);
    boldCommand.execute();

    System.out.println(document.getContent());

    var undoCommand = new UndoCommand(history);
    undoCommand.execute();
    System.out.println(document.getContent());




    }
}
