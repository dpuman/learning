public class Main {
    public static void main(String[] args){


        drawUIControl(new TextBox());
        drawUIControl(new CheckBox());
    }

    public static void drawUIControl(UIControls control){
        control.draw();
    }
}
