
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.print(" LED ON\n");

  delay(1000);

  digitalWrite(LED_BUILTIN, LOW);
  Serial.print(" LED OFF\n");

  delay(1000);
}
