import matplotlib.pyplot as plt

def plot_page_index_over_time(input_file, output_image):
    """시간에 따른 페이지 인덱스를 점 그래프로 그리기 및 저장"""
    timestamps = []  # 시간 (순차적 인덱스)
    page_indices = []  # 페이지 인덱스 값

    try:
        # 파일에서 데이터 읽기
        with open(input_file, "r") as file:
            for timestamp, line in enumerate(file):
                page_index = int(line.strip())
                timestamps.append(timestamp)
                page_indices.append(page_index)
    except FileNotFoundError:
        print(f"Error: File not found at {input_file}. Please ensure the file exists.")
        return

    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.scatter(timestamps, page_indices, alpha=0.5, s=1, c='blue')  # 점 크기(s)와 투명도(alpha) 조정
    plt.title("Page Index Over Time")
    plt.xlabel("Time (Sequential Order)")
    plt.ylabel("Page Index")
    plt.grid(True)
    plt.tight_layout()

    # 그래프 저장
    plt.savefig(output_image)
    print(f"Graph saved as {output_image}")
    plt.show()

if __name__ == "__main__":
    input_file = "page_index.log"  # 데이터 파일 경로
    output_image = "temproal.png"  # 저장할 이미지 파일 경로
    plot_page_index_over_time(input_file, output_image)

