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

      // Ok so I kinda did a horrible soldering job (my first time so yeah)
      // This is now how it goes
      switch(i){
        case 7:
          Serial.write(1);
          break;
        case 6:
          Serial.write(2);
          break;
        case 10:
          Serial.write(3);
          break;
        case 9:
          Serial.write(4);
          break;
        case 5:
          Serial.write(5);
          break;
        case 3:
          Serial.write(6);
          break;
        case 2:
          Serial.write(7);
          break;
        case 11:
          Serial.write(8);
          break;
      }
    }
  }
  // Set a delay
  delay(200);
}
