class Lesson {

   String text = "I'm a Simple Program";
   static String text2 = "I'm static text";

   static String getText(){
        return text2;
   }

   String getStaticText(){
        return text; 
   }

   public static void main(String[] args){
        String output = getText();
        System.out.println(output);
        Lesson progInstance = new Lesson();
        String retrievedText = progInstance.getText();
        String retrievedStaticText = 
                 progInstance.getStaticText(); 
        System.out.println(retrievedText);
        System.out.println(retrievedStaticText);
   }
}
