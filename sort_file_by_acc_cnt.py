def sort_file_by_second_value(input_file, output_file):
    """두 번째 값이 큰 순서로 파일의 줄을 정렬하여 저장합니다."""
    data = []

    # 파일에서 데이터 읽기
    with open(input_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                first_value = int(parts[0])
                second_value = int(parts[1])
                data.append((first_value, second_value))

    # 두 번째 값을 기준으로 내림차순 정렬
    data.sort(key=lambda x: x[1], reverse=True)

    # 정렬된 데이터를 출력 파일에 저장
    with open(output_file, 'w') as f:
        for first_value, second_value in data:
            f.write(f"{first_value} {second_value}\n")

# 사용 예시
input_file = 'page_access_counts.log'
output_file = 'sorted_page_access_counts.log'
sort_file_by_second_value(input_file, output_file)

