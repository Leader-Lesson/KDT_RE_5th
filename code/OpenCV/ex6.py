import cv2

src = cv2.imread('images/iu.jpg')
if src is None:
    print("파일을 찾을 수 없습니다.")
else:
    h, w, _ = src.shape

    # 1. 1/2 축소
    small_img = cv2.resize(src, (w // 2, h // 2)) 
    
    # 2. 좌우 반전
    flipped_img = cv2.flip(small_img, 1)

    # 3. 우하단 배치 (크기 불일치 방지)
    result = src.copy() 
    sh, sw, _ = flipped_img.shape # 실제 축소된 이미지의 크기 측정
    
    # 시작점(h//2)부터 이미지 높이(sh)만큼만 영역 지정
    result[h//2 : h//2 + sh, w//2 : w//2 + sw] = flipped_img

    cv2.imshow('Fixed Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()