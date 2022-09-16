/*
  DT-Production | Example IoT Rain Gauge Sensor untuk arduino
 ******************************
  PIN Map :
  RTC DS1307 SCL --> A5 Arduino
  RTC DS1307 SDA --> A4 Arduino
  RTC DS1307 VCC --> VCC 5v
  RTC DS1307 GND --> GND
 *****************************
  Rain Gauge Sensor PIN Map :
  Merah -------> VCC 5v
  Hitam -------> GND
  Putih ------> D2 Arduino
 ******************************
  diketahui bahwa 1 inchi = 2.54 cm
  diketahui bahwa 1 tip sensor ini = 2.6ml
  maka 0.053 inchi of rain didapat dari:
  panjang rain collector = 5.4 cm atau 2.126 inchi
  lebar rain collector = 3.6 cm atau 1.417 inchi
  luas=pxl -> 2.16 inchi x 1.417 inchi = 3.012 inchi persegi
  U.S. measures rain in inches so it would be 3.012 inchi kubik
  lalu dikonversi dari inchi kubik mjdi mL dan didapat bahwa 3.012 inchi kubik = 49.358 mL
  yg artinya 1 inchi of rain = 49.358 mL
  sehingga 1 tip sensor ini mewakili 2.6 mL/49.358 mL = 0.053 inchi of rain

  Terimakasih kepada : http://www.depoinovasi.com/ sebagai sumber refrensi dari Example ini.
*/

#include "RTClib.h"
#define RainPin 2
bool bucketPositionA = false;
const double bucketAmount = 0.053; // Hasil Perhitungan & Kalibrasi nilai per tip sensor

double dailyRain = 0.0;
double hourlyRain = 0.0;
double dailyRain_till_LastHour = 0.0;
bool first;
int delayData = 0;

RTC_Millis rtc;

unsigned long previousMillis = 0;
const long interval = 500; //ganti 500ms sesuai interval kebutuhan anda dalam menampilkan data per tip di serial monitor

void setup () {
  Serial.begin(9600);
  pinMode(RainPin, INPUT);
  Serial.println("Example Rain Gauge Sensor");
  rtc.begin(DateTime(__DATE__, __TIME__));
  delay(2000);
  Serial.println("Rain Gauge Ready !!");
  delay(2000);
}

void loop() {
  unsigned long currentMillis = millis();
  DateTime now = rtc.now();
  if ((bucketPositionA == false) && (digitalRead(RainPin) == LOW)) {
    bucketPositionA = true;
    dailyRain += bucketAmount;
  }
  if ((bucketPositionA == true) && (digitalRead(RainPin) == HIGH)) {
    bucketPositionA = false;
  }
  if (now.minute() != 0) first = true;

  if (now.minute() == 0 && first == true) {

    hourlyRain = dailyRain - dailyRain_till_LastHour;
    dailyRain_till_LastHour = dailyRain;

    // Menampilkan data per jam dan perhari di serial monitor
    Serial.println("=========== DATA CURAH HUJAN PER-JAM ============");
    Serial.print(now.hour());
    Serial.print(":");
    Serial.print(now.minute());
    Serial.print(":  Total Rain for the day = ");
    Serial.print(dailyRain, 3);
    Serial.print(" inches atau ");
    Serial.print(dailyRain * 2.54 * 10, 3);
    Serial.println(" mm");
    Serial.println();
    Serial.print("     :  Rain in last hour = ");
    Serial.print(hourlyRain, 3);
    Serial.print(" inches atau ");
    Serial.print(hourlyRain * 2.54 * 10, 3);
    Serial.println(" mm");
    Serial.println();
    first = false;
  }
  if (now.hour() == 0) {
    dailyRain = 0.0;
    dailyRain_till_LastHour = 0.0; // Jika jam pada RTC pukul 00:00 nilai pembacaan sensor menjadi 0 kembali
  }

/*
 * menampilkan nilai per tip curah hujan 
 * menggunakan Millis agar menghindari delay 
 * untuk pembacaan sensor
*/  
if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    Serial.println("=========== DATA CURAH HUJAN PER-TIP ============");
    Serial.print(now.hour());
    Serial.print(" : ");
    Serial.println(now.minute());
    Serial.println();
    Serial.print("mm/tip=");
    Serial.print(dailyRain * 2.54 * 10, 3);
    Serial.println(" mm");
    Serial.print("inch/tip=");
    Serial.print(dailyRain, 3);
    Serial.println(" inch");
   
  }
}
