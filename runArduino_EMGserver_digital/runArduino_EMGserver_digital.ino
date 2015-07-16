// variables for input pins and
int inPin = 7;
  
// variable to store the value 
int value = 0;

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

void setup() {
  // put your setup code here, to run once:
  // declaration of pin modes
  pinMode(inPin, INPUT);
  
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  
  // begin sending over serial port
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, LOW);
  
  // read the value on analog input
  value = digitalRead(inPin);

  // print out value over the serial port
//   Serial.println(10000); //prefix
   Serial.println(value);
//   Serial.println(10010); //end signal
   
  // wait for a bit to not overload the port
  delay(100);
  
  digitalWrite(led, HIGH);
  delay(100);
}
