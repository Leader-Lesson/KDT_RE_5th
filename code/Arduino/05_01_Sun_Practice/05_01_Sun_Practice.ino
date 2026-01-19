const int PANEL_PIN = A0; // 태양광 패널 입력
const int SW_PIN = 2;     // 판매 버튼 (INPUT_PULLUP)

// 가상 에너지 저장소
long energy = 0;

// 판매 단위(원하는 만큼 설정 가능)
const long SELL_UNIT = 100; // 100 단위 판매

// 충전 스케일 조정 (밝을수록 더 빨리 charging)
const int MAX_CHARGE_RATE = 50; // 전압이 5V일 때 +50씩 적립

void setup()
{
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);
}

void loop()
{

  // 1. 태양광 패널 전압 읽기 (0~5V)
  int raw = analogRead(PANEL_PIN);
  float voltage = (raw * 5.0) / 1023.0;

  // 2. 전압 기반 충전 공식
  // gain = (전압비율) × (최대충전량)
  int gain = (voltage / 5.0) * MAX_CHARGE_RATE;

  if (gain > 0)
  {
    energy += gain;
  }

  // 3. 버튼 눌림 감지
  bool prev = HIGH;
  bool curr = digitalRead(SW_PIN);

  if (prev == HIGH && curr == LOW)
  {
    Serial.println("=== 판매 요청 발생 ===");

    if (energy >= SELL_UNIT)
    {
      energy -= SELL_UNIT;
      Serial.print("판매 성공 | 판매량: ");
      Serial.print(SELL_UNIT);
      Serial.print(" | 남은 에너지: ");
      Serial.println(energy);
    }
    else
    {
      Serial.print("판매 실패 | 이유: 에너지가 부족합니다 | 현재 에너지: ");
      Serial.println(energy);
    }
  }
  prev = curr;

  // 4. 현재 상태 출력
  Serial.print("전압: ");
  Serial.print(voltage);
  Serial.print("V | 적립량: +");
  Serial.print(gain);
  Serial.print(" | 현재 에너지: ");
  Serial.println(energy);

  delay(500);
}