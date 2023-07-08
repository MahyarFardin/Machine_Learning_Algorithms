package Norm;

public class App{
    public static double NormCalculator(int [] vec, int power){
        // the algebra formula for calculating p norm of vector v = {v0, v1, ...}
        // is (|v0|^p + |v1|^p + ...)^1/p
        double sum = 0;
        for (int i : vec) {
            sum += Math.pow(Math.abs(i), power);
        }
        return Math.pow(sum, 1.0/power);
    }
    public static void main(String[] Args){
        int number = 100;
        int [] vec = new int[number];
        int power = 3; 
        double result = 0;

        // initializing the variables randomly
        for(int i=0 ; i < vec.length ; i++){
            // funny that we cannot generate negative numbers with this random generator :)
            vec[i] = (int)(Math.random()*10);
        }
        // printing the values
        for (int i = 0; i < vec.length; i++) {
            System.out.println(vec[i]);
        }
        // funny to see that if p > q => lp <= lq :)
        result = NormCalculator(vec, power);
        System.out.printf("L%d or ||V||%d is " + result, power, power);
    }
}