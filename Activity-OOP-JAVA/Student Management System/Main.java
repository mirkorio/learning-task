import java.io.IOException;
import java.util.Scanner;
import classes.Action;
import classes.Department;
import classes.Teacher;
import classes.Subject;
import classes.LearningMaterial;
import classes.AcademicTerm;

public class Main {
    public static Scanner console = new Scanner(System.in);
    public static Action actions = new Action();
    Scanner input = new Scanner(System.in);
    

    
    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static void entitiesMenu(int opt) throws IOException{
        int return_menu = 1;
        char opt2,  opt3, opt4;
        int password;
      
        while(return_menu == 1){
            switch (opt) {
                case 1:
                System.out.println("Enter Id: ");
                System.out.print(">>");
                id = console.nextInt();

                if(id == 1234){
                    clearScreen();
                    System.out.println("\n      Department     ");
                    menu2();

                    System.out.print(">> ");
                    opt2 = console.next().charAt(0);
                    opt2 = Character.toUpperCase(opt2);
                    
                    switch (opt2) {
                        case 'A':
                            clearScreen();
                            actions.viewDepartment();
                            break;
                        case 'B':
                            clearScreen();
                            actions.addDepartment();
                            break;
                        case 'C':
                        clearScreen();

                        System.out.println("Are you sure you want to delete all department?(Y/N)");
                        System.out.print(">> ");
                        opt4 = console.next().charAt(0);
                        opt4 = Character.toUpperCase(opt4);
    
                        if(opt4 == 'Y'){
                            actions.delAllDepartment();
                        }
                        else if(opt4 == 'N'){
                            break;
                        }
                        break;
                        case 'D':
                          mainMenu();
                          break;
                    }
                } else {
                  System.out.println("Please Enter Valid Id!");
                }
                    break;
                case 2:
                    System.out.println("Enter Id: ");
                    System.out.print(">>");
                    id = console.nextInt();

                    if(id == 1234){
                
                    clearScreen();
                    System.out.println("\n     Teacher     ");
                    menu2();

                    System.out.print(">> ");
                    opt2 = console.next().charAt(0);
                    opt2 = Character.toUpperCase(opt2);

                    switch (opt2) {
                        case 'A':
                            clearScreen();
                            actions.viewRecordTeacher();
                            break;
                        case 'B':
                            clearScreen();
                            actions.addRecordTeacher();
                            break;
                        case 'C':
                            clearScreen();

                            System.out.println("Are you sure you want to delete all records of Teacher?(Y/N)");
                            System.out.print(">> ");
                            opt4 = console.next().charAt(0);
                            opt4 = Character.toUpperCase(opt4);
        
                            if(opt4 == 'Y'){
                                actions.delAllTeacher();
                            }
                            else if(opt4 == 'N'){
                                break;
                            }
                            break;
                          case 'D':
                            mainMenu();
                            break;
                      }
                      } else {
                        System.out.println("Please Enter Valid Id!");
                      }
                    break;
                case 3:
                    System.out.println("Enter Id: ");
                    System.out.print(">>");
                    id = console.nextInt();

                    if(id == 1234){
                    clearScreen();
                    System.out.println("\n     Subject     ");
                    menu2();

                    System.out.print(">> ");
                    opt2 = console.next().charAt(0);
                    opt2 = Character.toUpperCase(opt2);

                    switch (opt2) {
                        case 'A':
                            clearScreen();
                            actions.viewSubject();
                            break;
                        case 'B':
                            clearScreen();
                            actions.addSubject();
                            break;
                        case 'C':
                            clearScreen();

                            System.out.println("Are you sure you want to delete all records of the subject?(Y/N)");
                            System.out.print(">> ");
                            opt4 = console.next().charAt(0);
                            opt4 = Character.toUpperCase(opt4);
        
                            if(opt4 == 'Y'){
                                actions.delAllSubject();
                            }
                            else if(opt4 == 'N'){
                                break;
                            }
                            break;
                          case 'D':
                            mainMenu();
                            break;
                      }
                      } else {
                        System.out.println("Please Enter Valid Id!");
                      }
                    break;
                case 4:
                    System.out.println("Enter Id: ");
                    System.out.print(">>");
                    id = console.nextInt();

                    if(id == 1234){
                    clearScreen();
                    System.out.println("\n     LearningMaterials     ");
                    menu2();
                    System.out.print(">> ");
                    opt2 = console.next().charAt(0);
                    opt2 = Character.toUpperCase(opt2);

                    switch (opt2) {
                        case 'A':
                            clearScreen();
                            actions.viewLearningMaterials();
                            break;
                        case 'B':
                            clearScreen();
                            actions.addLearningMaterials();
                            break;
                        case 'C':
                            clearScreen();

                            System.out.println("Are you sure you want to delete all records of the LearningMaterials?(Y/N)");
                            System.out.print(">> ");
                            opt4 = console.next().charAt(0);
                            opt4 = Character.toUpperCase(opt4);
        
                            if(opt4 == 'Y'){
                                actions.delAllLearningMaterials();
                            }
                            else if(opt4 == 'N'){
                                break;
                            }
                            break;
                          case 'D':
                            mainMenu();
                            break;
                        }
                        } else {
                        System.out.println("Please Enter Valid Id!");
                      }
                    break;
                case 5:
                    System.out.println("Enter Id: ");
                    System.out.print(">>");
                    id = console.nextInt();

                    if(id == 1234){
                     clearScreen();
                    System.out.println("\n      AcademicTerm     ");
                    menu2();

                    System.out.print(">> ");
                    opt2 = console.next().charAt(0);
                    opt2 = Character.toUpperCase(opt2);

                    switch (opt2) {
                        case 'A':
                            clearScreen();
                            actions.viewAcademicTerm();
                            break;
                        case 'B':
                            clearScreen();
                            actions.addAcademicTerm();
                            break;
                        case 'C':
                        clearScreen();

                        System.out.println("Are you sure you want to delete all records of AcademicTerm?(Y/N)");
                        System.out.print(">> ");
                        opt4 = console.next().charAt(0);
                        opt4 = Character.toUpperCase(opt4);
    
                        if(opt4 == 'Y'){
                            actions.delAllAcademicTerm();
                        }
                        else if(opt4 == 'N'){
                            break;
                        }
                        break;
                        case 'D':
                          mainMenu();
                          break;
                    }
                      } else {
                        System.out.println("Please Enter Valid Id!");
                      }
                    break;
                case 6:
                    System.out.println("Are you sure you want to exit?(Y/N)");
                    System.out.print(">> ");
                    opt3 = console.next().charAt(0);
                    opt3 = Character.toUpperCase(opt3);

                    if(opt3 == 'Y'){
                        System.out.println("Thank You for your time!");
                      System.out.println();
                      System.out.println("    Group 8(3 iN 1)    ");
                      System.out.println("     Bayos,Roberto     ");
                      System.out.println("  Tumaneng, Marc Christian ");
                      System.out.println("    Llaban, Jerome     ");
                        System.exit(0);
                    }
                    else if(opt3 == 'N'){
                        break;
                    }

                    else{
                        System.out.println("Invalid Input");
                        System.exit(0);
                    }
                    break;
                default:
                    System.out.println("Invalid Input");
                    break;
            }

            System.out.println("\nPress 1 to Continue and 0 to MAIN MENU");
            return_menu = console.nextInt();
        }
    }
    

    public static void menu2(){

        System.out.println("********************");
        System.out.println(" A. View Department      ");
        System.out.println(" B. Add New Department    ");
        System.out.println(" C. Delete All Department");
        System.out.println(" D. Back to Main Department ");
        System.out.println("********************");
    }

    public static void mainMenu() throws IOException {
      int opt;
        char exit = 'Y';

        while(exit == 'Y'){
        
        clearScreen();

        System.out.println("\n     WELCOME To CCCS DEPARTMENT      ");
        System.out.println("*******************************************************");
        System.out.println("              1. Department          ");
        System.out.println("              2. Teacher/s    ");
        System.out.println("              3. Subject      ");
        System.out.println("              4. LearningMaterials      ");
        System.out.println("              5. AcademicTerm     ");
        System.out.println("              6. Exit              ");
        System.out.println("*******************************************************");

        System.out.print(">> ");
        opt = console.nextInt();

        clearScreen();
        entitiesMenu(opt);
            
        System.out.println("\nReturn to MAIN MENU? (Y/N)");
        exit = console.next().charAt(0);

        exit = Character.toUpperCase(exit);
        }

    console.close();
    }

    public static void main(String args[]) throws IOException
    {
      mainMenu();
    }
}