int m1a = 10; // Motor 1, pin 10 del Arduino va al pin 15 del L293B
int m1b = 9;  // Motor 1, pin 9 del Arduino va al pin 10 del L293B
int m2a = 12; // Motor 2, pin 12 del Arduino va al pin 2 del L293B
int m2b = 11; // Motor 2, pin 11 del Arduino va al pin 7 del L293B
char val;

void setup() {
  pinMode(m1a, OUTPUT); // Configura el pin digital 10 como salida
  pinMode(m1b, OUTPUT); // Configura el pin digital 9 como salida
  pinMode(m2a, OUTPUT); // Configura el pin digital 12 como salida
  pinMode(m2b, OUTPUT); // Configura el pin digital 11 como salida
  Serial.begin(9600);   // Inicia la comunicación serial a 9600 bps
}

void loop() {
  if (Serial.available() > 0) {[^1^][1]
    val = Serial.read(); // Lee el valor enviado a través de la conexión serial
    Serial.println(val); // Imprime el valor para depuración

    switch (val) {
      case 'F': // Hacia adelante
        digitalWrite(m1a, HIGH);
        digitalWrite(m1b, LOW);
        digitalWrite(m2a, HIGH);
        digitalWrite(m2b, LOW);
        break;
      case 'B': // Hacia atrás
        digitalWrite(m1a, LOW);
        digitalWrite(m1b, HIGH);
        digitalWrite(m2a, LOW);
        digitalWrite(m2b, HIGH);
        break;
      case 'L': // Izquierda
        digitalWrite(m1a, LOW);
        digitalWrite(m1b, LOW);
        digitalWrite(m2a, HIGH);
        digitalWrite(m2b, LOW);
        break;
      case 'R': // Derecha
        digitalWrite(m1a, HIGH);
        digitalWrite(m1b, LOW);
        digitalWrite(m2a, LOW);
        digitalWrite(m2b, LOW);
        break;
      case 'S': // Stop - Pare, Carrito detenido
        digitalWrite(m1a, LOW);
        digitalWrite(m1b, LOW);
        digitalWrite(m2a, LOW);
        digitalWrite(m2b, LOW);
        break;
    }
  }
}
