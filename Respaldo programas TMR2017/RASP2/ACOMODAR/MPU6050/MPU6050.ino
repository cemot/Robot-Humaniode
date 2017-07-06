#include<Wire.h>
#include <Servo.h>

const int MPU=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,acx,acy,acz;
int posX,posY;
Servo sX;
Servo sY;
void setup(){
  Serial.begin(9600);
  
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);

  sX.attach(5);
  sY.attach(6); 
}
void loop(){
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  
  acx=AcX/100;
  acy=AcY/100;
  acz=AcZ/100;

  posX = map(acx, -160, 160, 0, 180);
  posY = map(acy, -160, 160, 0, 180);

  sX.write(posX);
  sY.write(posY);
  Serial.flush();
  Serial.println(String(acx)+","+String(acy)+","+String(acz));
  delay(200);
}
