package command.fx;

public class Button {
    private String label;
    private Command command;

    public Button(Command commad) {
        this.command =commad;
    }

    public void click(){
    command.execute();
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
}
