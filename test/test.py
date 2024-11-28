import requests
import random

# Open Library API를 통해 책 검색하기
def search_books(query):
    # Open Library API를 이용해 책 검색
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    books = response.json()['docs']
    
    # 검색된 책 리스트에서 제목과 저자 출력
    book_list = []
    for book in books[:5]:  # 상위 5개의 책만 출력
        title = book.get('title', '알 수 없는 제목')
        author = book.get('author_name', ['알 수 없는 저자'])[0]
        book_list.append(f"제목: {title}, 저자: {author}")
    
    return book_list

# 챗봇 클래스
class StoryBot:
    def __init__(self):
        self.story_intro = "릴레이 소설에 오신 것을 환영해! 우리 이야기나 써볼까?"
        self.story_body = ""
        self.book_list = []
        self.current_theme = ""
        self.current_setting = ""
        self.current_characters = []
    
    def introduce_story(self):
        print(self.story_intro)
    
    def get_book_recommendation(self):
        # 책 추천
        print("오 떠오른다...!")
        self.book_list = search_books("소설")  # '소설'을 기준으로 책 검색
        for idx, book in enumerate(self.book_list, 1):
            print(f"{idx}. {book}")
    
    def select_book_for_story(self):
        # 사용자가 책을 선택하여 주제, 등장인물, 배경 등을 기반으로 스토리 생성
        book = random.choice(self.book_list)  # 예시로 랜덤 책 선택
        print(f"\n선택된 책: {book}")
        self.current_theme = "모험"  # 책의 주요 테마 설정 (예시)
        self.current_setting = "판타지 세계"  # 설정
        self.current_characters = ["영웅", "악당", "조력자"]  # 주요 등장인물 설정
    
    def generate_story(self):
        # 설정된 주제, 등장인물, 배경을 바탕으로 새로운 이야기 전개
        print("\n새로운 이야기를 생성하는 중...\n")
        story_elements = [
            f"주제: {self.current_theme}",
            f"설정: {self.current_setting}",
            f"등장인물: {', '.join(self.current_characters)}"
        ]
        self.story_body += "\n".join(story_elements) + "\n\n"
        
        # 무작위로 이야기 진행
        self.story_body += "이야기가 시작됩니다...\n"
        story_continuation = random.choice([
            "영웅은 고대의 악으로부터 왕국을 구하기 위한 퀘스트를 시작합니다.",
            "미스터리한 포털이 나타나고, 그곳은 미지의 세계로 이어집니다.",
            "악당은 평화로운 세계를 무너뜨리려고 음모를 꾸밉니다."
        ])
        self.story_body += story_continuation + "\n"
        
        print(self.story_body)

    def continue_story(self, user_input):
        # 사용자가 제공한 입력을 바탕으로 이야기를 계속 전개
        self.story_body += f"\n사용자 입력: {user_input}\n"
        self.story_body += "이야기가 전개됩니다...\n"
        self.story_body += f"{random.choice(['영웅이 싸운다', '악당이 습격한다', '반전이 일어난다'])}...\n"
        print(self.story_body)

# 챗봇 사용 예시
story_bot = StoryBot()

# 소설 시작 인사
story_bot.introduce_story()

# 책 추천
story_bot.get_book_recommendation()

# 책 선택 및 스토리 설정
story_bot.select_book_for_story()

# 이야기 생성
story_bot.generate_story()

# 사용자가 이야기 입력
while True:
    user_input = input("이야기의 다음 내용은 무엇인가요? (또는 'quit'을 입력하면 종료됩니다): ")
    if user_input.lower() == 'quit':
        print("소설을 함께 만들어 주셔서 감사합니다! 안녕히 가세요!")
        break
    story_bot.continue_story(user_input)
