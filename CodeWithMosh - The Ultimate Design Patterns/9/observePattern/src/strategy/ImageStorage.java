package strategy;

public class ImageStorage {
//    private Compressor comprassor;
//    private Filter filter;

//    public ImageStorage(Compressor comprassor, Filter filter) {
//        this.comprassor = comprassor;
//        this.filter = filter;
//    }

    public void store(String filename,Compressor comprassor, Filter filter){

        comprassor.compress(filename);
        filter.apply(filename);


//        if(comprassor == "jpeg")
//            System.out.println("Compressing using JPEG");
//        else if(comprassor == "png")
//            System.out.println("Compressing using PNG");
//
//        if(filter == "b&w")
//            System.out.println("Applying B&W filter");
//        else if(filter == "high-contrast")
//            System.out.println("Applying high contrast filter");
    }


}
