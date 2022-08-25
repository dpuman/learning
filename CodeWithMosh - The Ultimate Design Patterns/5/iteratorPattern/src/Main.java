import iterator.BrowseHistory;
import iterator.Iterator;

public class Main {
    public static void main(String[] args){

        var history = new BrowseHistory();
        history.push("a");
        history.push("b");
        history.push("c");
        history.push("d");

        Iterator iterator =history.createIterator();
        while(iterator.hasNext()){
            var url =iterator.current();
            System.out.println(url);
            iterator.next();
        }

//        for (var i=0;i<history.getUrls().size();i++){
//            var url =history.getUrls().get(i);
//            System.out.println(url);
//        }
    }
}
