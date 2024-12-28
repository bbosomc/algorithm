# 전화번호목록
def solution(phone_book):
    # 1. 전화번호 목록 정렬
    phone_book.sort()

    # 2. 인접한 두 전화번호만 접두사 관계인지 검사 - 정렬했기 때문에 굳이 다 검사할 필요 없음
    for i in range(len(phone_book) - 1):
        # i번 번호가 i+1번 번호의 접두사인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False  # 접두사면 False

    return True  # 전부 확인 후 접두사가 없으면 True

phone_book = ["119", "97674223", "1195524421"]
print(solution(["119", "97674223", "1195524421"]))

# H-index(이해 잘 안가서 걍 공식 외움)
def solution(citations):
    arr = sorted(citations, reverse=True)
    h = 0
    # 6,5,3,1,0
    for i in range(len(arr)):
        if arr[i] < i+1:
            return i
    return len(arr)

print(solution([3,0,6,1,5]))