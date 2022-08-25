
import state.Canvas;
import state.SelectionTool;


public class Main {
    public static void main(String[] args){

        var canvas = new Canvas();
        canvas.setCuttentTool(new SelectionTool());
        canvas.mouseDown();
        canvas.mouseUp();
    }


}
