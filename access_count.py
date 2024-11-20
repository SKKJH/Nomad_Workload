def count_page_accesses(sorted_file, output_file):
    """정렬된 페이지 인덱스 파일에서 페이지 접근 횟수를 계산"""
    with open(sorted_file, "r") as infile, open(output_file, "w") as outfile:
        current_page = None
        count = 0

        for line in infile:
            page = int(line.strip())
            if page == current_page:
                count += 1
            else:
                if current_page is not None:
                    outfile.write(f"{current_page} {count}\n")
                current_page = page
                count = 1

        # 마지막 페이지 기록
        if current_page is not None:
            outfile.write(f"{current_page} {count}\n")

if __name__ == "__main__":
    sorted_file = "page_index_sorted.log"
    output_file = "page_access_counts.log"
    count_page_accesses(sorted_file, output_file)
    print(f"Page access counts saved to {output_file}")

