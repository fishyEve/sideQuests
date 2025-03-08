/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package areacircle;

import java.util.*;

/**
 *
 * @author evecollier
 */

public class AreaCircle {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        //Make a scanner
        
        Scanner in = new Scanner (System.in);
        // Make a variable for radius and set to 15
        
        
        // calculate the area of that circle (area = PI * radius * radius)
        
        //int radius = 15;
        int radius = in.nextInt();
        
        
        
        double PI = 3.14;
        
        double area = PI * radius * radius;
        
        System.out.println("Area is..." + area);
               
        
        
     
    }
    
}
