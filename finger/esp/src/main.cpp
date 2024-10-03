#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <ESP32Servo.h>

const char* ssid = "WIFISSID";
const char* password = "YOURPASSWORD";

AsyncWebServer server(80);
Servo servo1, servo2, servo3;
const int servoPin1 = 13;
const int servoPin2 = 12;
const int servoPin3 = 14;
int currentPosition1 = 0;
int currentPosition2 = 0;
int currentPosition3 = 0;

// Function prototype declaration
void handleServoRequest(AsyncWebServerRequest *request, Servo &servo, int &currentPosition, const String &servoId);


void setup() {
  Serial.begin(115200);
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);
  servo1.write(currentPosition1);
  servo2.write(currentPosition2);
  servo3.write(currentPosition3);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    Serial.print("Reveiving request");
    request->send(200, "text/plain", "ESP32 Multi-Servo Control");
  });

  server.on("/set1", HTTP_GET, [](AsyncWebServerRequest *request){
    handleServoRequest(request, servo1, currentPosition1, "1");
  });

  server.on("/set2", HTTP_GET, [](AsyncWebServerRequest *request){
    handleServoRequest(request, servo2, currentPosition2, "2");
  });

  server.on("/set3", HTTP_GET, [](AsyncWebServerRequest *request){
    handleServoRequest(request, servo3, currentPosition3, "3");
  });

  server.begin();
}

void handleServoRequest(AsyncWebServerRequest *request, Servo &servo, int &currentPosition, const String &servoId) {
  Serial.println("Received /set" + servoId + " request");
  if (request->hasParam("pos")) {
    String posParam = request->getParam("pos")->value();
    int pos = posParam.toInt();
    Serial.println("Position parameter: " + posParam);
    if (pos >= 0 && pos <= 180) {
      servo.write(pos);
      currentPosition = pos;
      Serial.println("Sending response: Servo" + servoId + " position set to " + String(pos));
      request->send(200, "text/plain", "Servo" + servoId + " position set to " + String(pos));
    } else {
      Serial.println("Invalid position");
      request->send(400, "text/plain", "Invalid position");
    }
  } else {
    Serial.println("Position not specified");
    request->send(400, "text/plain", "Position not specified");
  }
}

void loop() {
  // Nothing needed here
}