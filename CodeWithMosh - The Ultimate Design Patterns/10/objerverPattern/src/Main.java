import chainOfRersponsibility.*;


public class Main {
    public static void main(String[] args){

//        authenticator-> logger -> compressor

        var compressor = new Compressor(null);
        var logger = new Logger(compressor);
        var authentication = new Authenticator(logger);
        var server =new WebServer(authentication);
        server.handle(new HttpRequest("admin","1234"));





    }
}
