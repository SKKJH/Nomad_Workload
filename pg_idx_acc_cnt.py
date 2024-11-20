import matplotlib.pyplot as plt

def plot_page_access_counts(input_file):
    output_image = "pg_idx_acc_cnt.png"
    """페이지 인덱스와 접근 횟수를 그래프로 그리기"""
    page_indices = []
    access_counts = []

    try:
        # 파일에서 데이터 읽기
        with open(input_file, "r") as file:
            for line in file:
                page, count = map(int, line.strip().split())
                page_indices.append(page)
                access_counts.append(count)
    except FileNotFoundError:
        print(f"Error: File not found at {input_file}. Please ensure the file exists.")
        return

    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.plot(page_indices, access_counts, marker='o', linestyle='-', linewidth=1)
    plt.title("Page Index vs Access Count")
    plt.xlabel("Page Index")
    plt.ylabel("Access Count")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_image)

if __name__ == "__main__":
    input_file = "page_access_counts.log"  # 데이터 파일 경로
    plot_page_access_counts(input_file)

