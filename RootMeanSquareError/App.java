package RootMeanSquareError;

public class App{
    public static double RMSE_caculator(int [] y_main, int [] y_prediction){
        int SquaredError = 0;
        // calculating the squared error
        for (int i = 0; i < y_prediction.length; i++) {
            SquaredError += Math.pow(y_prediction[i] - y_main[i], 2);
        }
        // calculating mean squared error
        System.out.println("Squared error is " + SquaredError);
        return Math.sqrt(( 1.0 / y_main.length ) * SquaredError);
    }
    public static void main(String[] Args){
        int number = 20;
        int [] y_main = new int[number];
        int [] y_prediction = new int[number];
        double RMSE = 0;
        // initializing the variables randomly
        for(int i=0 ; i < y_main.length ; i++){
            y_main[i] = (int)(Math.random()*100);
            y_prediction[i] = (int)(Math.random()*100);
        }
        // printing the values
        System.out.println("y\ty_prediction");
        for (int i = 0; i < y_prediction.length; i++) {
            System.out.println(y_main[i]+"\t"+y_prediction[i]);
        }
        RMSE = RMSE_caculator(y_main, y_prediction);
        System.out.println("RMSE is " + RMSE);
    }
}