public class Tema0 {

    // exercitiul 1

    // O variabila boolean este o data care poate memora doar valoarea 'Adevarat' sau 'Fals'
    public static void main(String[] args) {

        //exercitiul 3

        String nume;
        nume = "Ioana";
        int varsta;
        varsta = 23;
        /* variabila de tip float este asemanatoare cu variabila de tip double
        in schimb variabila double este tipica limbajului java , iar variabila float limbajalui phyton
         */
        double inaltime;
        inaltime = 161.5;
        boolean culoareParBlonda;
        culoareParBlonda = false;
        System.out.println( "Ma numesc "+ nume + " si am varsta de " + varsta + " ani , inaltimea mea este de " + inaltime + " m , iar parul meu are culoarea blonda " + culoareParBlonda );

        //exercitiul 5

        int i;
        for (i=1; i<20; i=i+3)
            System.out.println(i);
        /*segementul de cod java anterior ruleaza numerele mai mici decat 20 , incepand cu 1,
        aceste numere fiind din 3 in 3
         */

    }
}
