# 251204

# N: 행 개수, M: 열 개수 입력
N, M = map(int, input().split())

# 보드를 리스트로 저장
board = [input().strip() for _ in range(N)]

# 정답 후보를 매우 크게 설정
answer = 987654321

# 체스판 패턴 정의 (W부터 시작 / B부터 시작)
pattern1 = ["WBWBWBWB", "BWBWBWBW"]  # W 시작
pattern2 = ["BWBWBWBW", "WBWBWBWB"]  # B 시작

# (i, j)는 8×8을 시작하는 왼쪽 위 칸
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):

        repaint1 = 0  # W 시작 패턴과 비교해 색칠해야 하는 칸 수
        repaint2 = 0  # B 시작 패턴과 비교해 색칠해야 하는 칸 수

        # 8×8 영역 비교
        for r in range(8):     # 행 0~7
            for c in range(8): # 열 0~7

                # 현재 실제 보드의 문자
                current = board[i + r][j + c]

                # 패턴1(W 시작)과 다르면 색칠해야 함
                if current != pattern1[r % 2][c]:
                    repaint1 += 1

                # 패턴2(B 시작)과 다르면 색칠해야 함
                if current != pattern2[r % 2][c]:
                    repaint2 += 1

        # 현재 8×8 영역에서 최소 색칠 개수를 전체 최소값과 비교
        answer = min(answer, repaint1, repaint2)

# 결과 출력
print(answer)
