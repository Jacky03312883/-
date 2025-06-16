
import cv2

# 載入訓練好的 Haar 級聯分類器
cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# 開啟攝影機
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 轉成灰階影像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測垃圾桶
    bins = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 標記偵測結果
    for (x, y, w, h) in bins:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Trash Bin', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('Trash Bin Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
