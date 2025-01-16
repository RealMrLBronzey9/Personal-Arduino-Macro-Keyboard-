// Switch Pins
#define INIT_PIN 2
const int switchPins[10] = {2,3,4,5,6,7,8,9,10,11};
int switchPinLength = (sizeof(switchPins)/sizeof(int));
int iterateSwitchPins = switchPinLength + INIT_PIN;

// Switch Pin Status
int switchStatus;


void setup() {
  // put your setup code here, to run once:
  
  // Setup Serial Connection at 9600
  Serial.begin(9600);

  // Setup the switch pins as input
  for(int i = INIT_PIN; i < iterateSwitchPins; i++){
    pinMode(i, INPUT_PULLUP);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  bool isButtonPressed = false;

  // Check the status of all pins and write to the one on HIGH
  for(int i = INIT_PIN; i < iterateSwitchPins && !isButtonPressed; i++){
    switchStatus = digitalRead(i);

    if(switchStatus == LOW){
      isButtonPressed = true;
      Serial.write(i - 1);  // Write the specified switch number (pin 2 is switch 1..)
    }
  }

  delay(200);
}
