package state;

public class Canvas {
    private Tool currentTool;
//    private ToolType currentTool;
    public void mouseDown(){
        currentTool.mouseDown();
//        if (currentTool == ToolType.SELECTION){
//            System.out.println("Selection icon");
//        }else if (currentTool == ToolType.BRUSH){
//            System.out.println("Brush icon");
//        }else if (currentTool == ToolType.ERASER){
//            System.out.println("Eraser icon");
//        }

    }
    public void mouseUp(){
        currentTool.mouseUp();
//        if (currentTool == ToolType.SELECTION){
//            System.out.println("Draw dashed rectangle");
//        }else if (currentTool == ToolType.BRUSH){
//            System.out.println("Draw a line");
//        }else if (currentTool == ToolType.ERASER){
//            System.out.println("Eraser something");
//        }

    }

    public Tool getCuttentTool() {
        return currentTool;
    }

    public void setCuttentTool(Tool cuttentTool) {
        this.currentTool = cuttentTool;
    }
}
