// variables for input pins and
int analogInput[6];
  
// variable to store the value 
int value[6]; 

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

void setup() {
  // put your setup code here, to run once:
  // declaration of pin modes
  for(int i=0;i<6;i++)
  {
    analogInput[i] = i+1;
    value[i] = 0;     
    pinMode(analogInput[i], INPUT);    
  }
  
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  
  // begin sending over serial port
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, LOW);
  
  // read the value on analog input
  for(int i=0;i<6;i++)
  {
    value[i] = analogRead(analogInput[i]);
  }

  // print out value over the serial port
  for(int i=0;i<6;i++)
  {
    Serial.println(10000 + i + 1); //prefix
    Serial.println(value[i]);
    Serial.println(10010); //end signal
  }
  // wait for a bit to not overload the port
  delay(100);
  
  digitalWrite(led, HIGH);
  delay(100);
}
