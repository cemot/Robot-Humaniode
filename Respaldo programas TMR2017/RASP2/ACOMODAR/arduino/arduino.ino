int led = 13;
int n=6;
void setup () {
   pinMode(led, OUTPUT); //LED 13 como salida
   pinMode(n,INPUT);
   Serial.begin(9600); //Inicializo el puerto serial a 9600 baudios
}

void loop () {
   Serial.println(digitalRead(n));
   if (Serial.available()) { //Si está disponible
      int c= Serial.read(); //Guardamos la lectura en una variable char
      if (c == 15) { //Si es una 'H', enciendo el LED
         digitalWrite(led, HIGH);
      } else if (c == 250) { //Si es una 'L', apago el LED
         digitalWrite(led, LOW);
      }
   }
   delay(500);
}
 
