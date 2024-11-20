import os
import heapq

CHUNK_SIZE = 1000000  # 한 번에 처리할 줄 수 (1백만 줄)
TEMP_FILE_PREFIX = "temp_chunk_"  # 임시 파일 이름 접두사

def sort_and_save_chunk(chunk, chunk_index):
    """부분 정렬 후 임시 파일에 저장"""
    chunk.sort()
    temp_file_name = f"{TEMP_FILE_PREFIX}{chunk_index}.txt"
    with open(temp_file_name, "w") as temp_file:
        temp_file.writelines(f"{num}\n" for num in chunk)
    return temp_file_name

def merge_sorted_chunks(output_file, temp_files):
    """정렬된 임시 파일 병합"""
    with open(output_file, "w") as output:
        # 각 파일의 첫 번째 값 로드
        min_heap = []
        file_pointers = []

        for temp_file in temp_files:
            f = open(temp_file, "r")
            file_pointers.append(f)
            first_line = f.readline()
            if first_line:
                heapq.heappush(min_heap, (int(first_line.strip()), len(file_pointers) - 1))

        # 병합 처리
        while min_heap:
            value, file_index = heapq.heappop(min_heap)
            output.write(f"{value}\n")
            next_line = file_pointers[file_index].readline()
            if next_line:
                heapq.heappush(min_heap, (int(next_line.strip()), file_index))

        # 임시 파일 닫기
        for f in file_pointers:
            f.close()

def external_sort(input_file, output_file):
    """외부 정렬 메인 함수"""
    temp_files = []
    chunk = []
    chunk_index = 0

    # 입력 파일 읽어서 부분 정렬 수행
    with open(input_file, "r") as f:
        for line in f:
            chunk.append(int(line.strip()))
            if len(chunk) == CHUNK_SIZE:
                temp_file_name = sort_and_save_chunk(chunk, chunk_index)
                temp_files.append(temp_file_name)
                chunk_index += 1
                chunk = []

        # 남은 데이터 처리
        if chunk:
            temp_file_name = sort_and_save_chunk(chunk, chunk_index)
            temp_files.append(temp_file_name)

    # 정렬된 임시 파일 병합
    merge_sorted_chunks(output_file, temp_files)

    # 임시 파일 삭제
    for temp_file in temp_files:
        os.remove(temp_file)

# 실행 예제
if __name__ == "__main__":
    input_file = "page_index.log"
    output_file = "page_index_sorted.log"
    external_sort(input_file, output_file)
    print(f"Sorting complete. Sorted file saved to {output_file}")

