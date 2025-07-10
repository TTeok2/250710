import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="MBTI 여행지 추천 🌍",
    page_icon="✈️",
    layout="wide"
)

# CSS 스타일 추가
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .destination-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .attraction-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .mbti-badge {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# MBTI별 여행지 데이터
MBTI_DESTINATIONS = {
    "INTJ": {
        "personality": "건축가형 🏛️",
        "description": "독창적이고 전략적인 사고를 가진 당신",
        "destinations": [
            {
                "name": "교토, 일본 🇯🇵",
                "reason": "고요한 사찰과 정원에서 깊은 사색을 즐기며, 일본의 전통 건축과 철학을 체험할 수 있습니다.",
                "attraction": "기요미즈데라",
                "attraction_reason": "세계문화유산으로 지정된 이 목조 사찰은 완벽한 건축 기법과 아름다운 경치로 INTJ의 완벽주의적 성향을 만족시킵니다."
            },
            {
                "name": "아이슬란드 🇮🇸",
                "reason": "신비로운 자연 현상과 독특한 지질학적 특징들이 호기심 많은 INTJ에게 완벽한 탐구 대상입니다.",
                "attraction": "오로라",
                "attraction_reason": "과학적 현상인 오로라를 직접 관찰하며 우주의 신비를 느낄 수 있어 지적 호기심을 충족시킵니다."
            },
            {
                "name": "프라하, 체코 🇨🇿",
                "reason": "중세 건축물과 역사적 유적지가 완벽하게 보존된 도시로, 체계적인 도시 계획을 감상할 수 있습니다.",
                "attraction": "프라하 성",
                "attraction_reason": "세계에서 가장 큰 고성 단지로, 천년의 역사와 건축학적 완성도가 전략적 사고를 가진 INTJ에게 영감을 줍니다."
            }
        ]
    },
    "INTP": {
        "personality": "논리학자형 🔬",
        "description": "논리적이고 분석적인 사고를 가진 당신",
        "destinations": [
            {
                "name": "제네바, 스위스 🇨🇭",
                "reason": "CERN과 같은 세계적인 연구기관이 위치해 있어 과학과 기술의 최첨단을 경험할 수 있습니다.",
                "attraction": "CERN",
                "attraction_reason": "세계 최대 입자물리학 연구소로, 우주의 근본 원리를 탐구하는 곳이어서 INTP의 지적 호기심을 극대화합니다."
            },
            {
                "name": "싱가포르 🇸🇬",
                "reason": "첨단 기술과 혁신적 도시 설계가 완벽하게 조화된 미래 도시의 모습을 볼 수 있습니다.",
                "attraction": "가든스 바이 더 베이",
                "attraction_reason": "첨단 기술로 만들어진 미래형 식물원으로, 자연과 기술의 완벽한 융합을 보여주는 혁신적 공간입니다."
            },
            {
                "name": "시애틀, 미국 🇺🇸",
                "reason": "기술 혁신의 중심지로, 마이크로소프트, 아마존 등 글로벌 기업들의 본사가 위치해 있습니다.",
                "attraction": "스페이스 니들",
                "attraction_reason": "미래지향적 건축물로, 기술과 디자인의 완벽한 결합을 보여주며 논리적 사고를 자극합니다."
            }
        ]
    },
    "ENTJ": {
        "personality": "통솔자형 👑",
        "description": "카리스마 있고 지도력이 뛰어난 당신",
        "destinations": [
            {
                "name": "뉴욕, 미국 🇺🇸",
                "reason": "세계 경제의 중심지로, 야심찬 ENTJ가 성공의 에너지를 느끼며 영감을 받을 수 있는 최적의 장소입니다.",
                "attraction": "월스트리트",
                "attraction_reason": "세계 금융의 중심지로, 리더십과 전략적 사고를 가진 ENTJ에게 성공의 동기부여를 제공합니다."
            },
            {
                "name": "두바이, UAE 🇦🇪",
                "reason": "불가능을 가능으로 만든 도시로, 비전을 현실로 만드는 리더십의 결과물을 직접 체험할 수 있습니다.",
                "attraction": "부르즈 할리파",
                "attraction_reason": "세계 최고층 건물로, 한계를 뛰어넘는 도전 정신과 리더십의 상징이자 ENTJ의 야망을 자극합니다."
            },
            {
                "name": "런던, 영국 🇬🇧",
                "reason": "역사적으로 세계를 이끌어온 대영제국의 중심지로, 전통과 현대적 리더십을 모두 경험할 수 있습니다.",
                "attraction": "런던 아이",
                "attraction_reason": "현대적 랜드마크로, 도시 전체를 한눈에 조망하며 거시적 관점과 전략적 사고를 기를 수 있습니다."
            }
        ]
    },
    "ENTP": {
        "personality": "변론가형 🎭",
        "description": "창의적이고 활동적인 당신",
        "destinations": [
            {
                "name": "바르셀로나, 스페인 🇪🇸",
                "reason": "가우디의 독창적인 건축물과 활기찬 문화가 창의적인 ENTP의 상상력을 자극합니다.",
                "attraction": "사그라다 파밀리아",
                "attraction_reason": "140년 넘게 건설 중인 독특한 건축물로, 끊임없는 도전과 혁신 정신이 ENTP의 창의성과 완벽하게 맞습니다."
            },
            {
                "name": "베를린, 독일 🇩🇪",
                "reason": "역사적 변화의 중심지로, 다양한 문화와 예술이 공존하는 창의적 에너지가 넘치는 도시입니다.",
                "attraction": "베를린 장벽",
                "attraction_reason": "역사적 변화의 상징으로, 기존 체제에 도전하고 새로운 가능성을 모색하는 ENTP의 정신과 일치합니다."
            },
            {
                "name": "암스테르담, 네덜란드 🇳🇱",
                "reason": "자유로운 분위기와 다양한 문화가 공존하는 도시로, 새로운 아이디어와 경험을 추구하는 ENTP에게 완벽합니다.",
                "attraction": "안네 프랑크 하우스",
                "attraction_reason": "역사적 의미가 깊은 곳으로, 인간의 창의성과 희망을 보여주는 공간이어서 ENTP의 인문학적 호기심을 자극합니다."
            }
        ]
    },
    "INFJ": {
        "personality": "옹호자형 🌙",
        "description": "이상주의적이고 헌신적인 당신",
        "destinations": [
            {
                "name": "부탄 🇧🇹",
                "reason": "행복지수가 높은 나라로, 물질보다 정신적 풍요를 추구하는 INFJ의 가치관과 완벽하게 일치합니다.",
                "attraction": "타이거 네스트 사원",
                "attraction_reason": "절벽 위에 자리한 신성한 사원으로, 영적 성장과 내적 평화를 추구하는 INFJ에게 깊은 영감을 줍니다."
            },
            {
                "name": "인도 리시케시 🇮🇳",
                "reason": "세계적인 요가와 명상의 중심지로, 영적 성장과 자아 발견을 추구하는 INFJ에게 이상적입니다.",
                "attraction": "갠지스 강",
                "attraction_reason": "힌두교의 성스러운 강으로, 정화와 영적 각성의 상징이며 INFJ의 깊은 내면세계와 공명합니다."
            },
            {
                "name": "산토리니, 그리스 🇬🇷",
                "reason": "아름다운 석양과 평온한 분위기가 내성적인 INFJ에게 깊은 사색과 영감을 제공합니다.",
                "attraction": "이아 마을",
                "attraction_reason": "세계에서 가장 아름다운 석양을 볼 수 있는 곳으로, 자연의 아름다움을 통해 내적 평화를 찾을 수 있습니다."
            }
        ]
    },
    "INFP": {
        "personality": "중재자형 🌸",
        "description": "이상적이고 예술적 감각이 뛰어난 당신",
        "destinations": [
            {
                "name": "발리, 인도네시아 🇮🇩",
                "reason": "자연과 문화가 조화롭게 어우러진 섬으로, 예술적 영감과 내적 평화를 동시에 찾을 수 있습니다.",
                "attraction": "우붓 라이스테라스",
                "attraction_reason": "아름다운 계단식 논밭으로, 자연과 인간의 조화로운 공존을 보여주며 INFP의 이상향을 실현한 공간입니다."
            },
            {
                "name": "파리, 프랑스 🇫🇷",
                "reason": "예술과 로맨스의 도시로, 창조적 영감과 아름다운 문화를 사랑하는 INFP에게 완벽한 여행지입니다.",
                "attraction": "몽마르트르",
                "attraction_reason": "예술가들의 성지로, 자유로운 창작 활동과 예술적 영감을 얻을 수 있는 INFP의 이상적인 공간입니다."
            },
            {
                "name": "뉴질랜드 남섬 🇳🇿",
                "reason": "때묻지 않은 자연과 평화로운 분위기가 내면의 조화를 추구하는 INFP에게 완벽한 힐링을 제공합니다.",
                "attraction": "밀포드 사운드",
                "attraction_reason": "세계에서 가장 아름다운 피오르드로, 자연의 숭고함과 평온함이 INFP의 감성을 깊이 울립니다."
            }
        ]
    },
    "ENFJ": {
        "personality": "주인공형 🌟",
        "description": "따뜻하고 카리스마 넘치는 당신",
        "destinations": [
            {
                "name": "코스타리카 🇨🇷",
                "reason": "생태관광의 선두주자로, 환경 보호와 지속가능한 발전을 추구하는 ENFJ의 이상을 실현한 나라입니다.",
                "attraction": "마누엘 안토니오 국립공원",
                "attraction_reason": "생물 다양성 보호의 모범 사례로, 자연과 인간의 공존을 추구하는 ENFJ의 가치관과 일치합니다."
            },
            {
                "name": "케냐 🇰🇪",
                "reason": "야생동물 보호와 지역 공동체 발전을 동시에 추구하는 곳으로, 사회적 기여를 중시하는 ENFJ에게 의미 있는 여행입니다.",
                "attraction": "마사이 마라",
                "attraction_reason": "동물의 대이동을 볼 수 있는 곳으로, 자연의 웅장함과 생명의 소중함을 느끼며 타인에 대한 관심을 더욱 키울 수 있습니다."
            },
            {
                "name": "캐나다 밴쿠버 🇨🇦",
                "reason": "다문화 사회의 모범 도시로, 다양성을 존중하고 포용하는 ENFJ의 성향과 완벽하게 맞습니다.",
                "attraction": "스탠리 파크",
                "attraction_reason": "도시와 자연이 조화롭게 공존하는 공간으로, 공동체의 행복을 추구하는 ENFJ의 이상을 보여줍니다."
            }
        ]
    },
    "ENFP": {
        "personality": "활동가형 🎪",
        "description": "열정적이고 사교적인 당신",
        "destinations": [
            {
                "name": "태국 🇹🇭",
                "reason": "다양한 문화와 활동이 가득한 나라로, 새로운 경험과 만남을 추구하는 ENFP에게 완벽한 모험의 장소입니다.",
                "attraction": "차트차크 주말시장",
                "attraction_reason": "세계에서 가장 큰 주말시장으로, 다양한 사람들과 문화를 경험하며 ENFP의 사교성과 호기심을 만족시킵니다."
            },
            {
                "name": "멕시코 🇲🇽",
                "reason": "열정적인 문화와 다채로운 축제가 있는 나라로, 에너지 넘치는 ENFP가 즐길 수 있는 무수한 경험을 제공합니다.",
                "attraction": "테오티와칸",
                "attraction_reason": "고대 문명의 신비로운 피라미드로, 역사와 문화에 대한 ENFP의 호기심을 자극하며 새로운 영감을 줍니다."
            },
            {
                "name": "브라질 리우데자네이루 🇧🇷",
                "reason": "세계적인 축제와 해변 문화가 어우러진 도시로, 자유롭고 활기찬 ENFP의 성격과 완벽하게 맞습니다.",
                "attraction": "코파카바나 해변",
                "attraction_reason": "세계에서 가장 유명한 해변 중 하나로, 음악과 축제, 다양한 사람들과의 만남이 ENFP의 에너지를 충전시킵니다."
            }
        ]
    },
    "ISTJ": {
        "personality": "물류전문가형 📋",
        "description": "책임감 강하고 실용적인 당신",
        "destinations": [
            {
                "name": "독일 🇩🇪",
                "reason": "체계적이고 질서정연한 문화와 정확한 시스템이 규칙을 중시하는 ISTJ의 성향과 완벽하게 일치합니다.",
                "attraction": "노이슈반슈타인 성",
                "attraction_reason": "디즈니 성의 모델이 된 완벽한 건축물로, 세밀한 설계와 전통적 아름다움이 ISTJ의 완벽주의를 만족시킵니다."
            },
            {
                "name": "일본 🇯🇵",
                "reason": "전통을 중시하고 질서정연한 문화가 안정성과 예측 가능성을 선호하는 ISTJ에게 편안함을 제공합니다.",
                "attraction": "후지산",
                "attraction_reason": "일본의 상징으로, 변하지 않는 아름다움과 신성함이 전통과 안정을 추구하는 ISTJ의 마음을 평온하게 합니다."
            },
            {
                "name": "스위스 🇨🇭",
                "reason": "정확성과 품질로 유명한 나라로, 세심함과 책임감을 중시하는 ISTJ의 가치관과 완벽하게 부합합니다.",
                "attraction": "융프라우요흐",
                "attraction_reason": "유럽의 지붕으로 불리는 곳으로, 정확한 산악철도 시스템과 웅장한 자연이 ISTJ의 실용성과 미적 감각을 동시에 만족시킵니다."
            }
        ]
    },
    "ISFJ": {
        "personality": "수호자형 🛡️",
        "description": "따뜻하고 배려심 많은 당신",
        "destinations": [
            {
                "name": "아일랜드 🇮🇪",
                "reason": "따뜻한 인심과 평화로운 자연이 어우러진 나라로, 조화로운 관계를 중시하는 ISFJ에게 완벽한 휴식을 제공합니다.",
                "attraction": "클리프 오브 모어",
                "attraction_reason": "아일랜드의 아름다운 해안 절벽으로, 자연의 평온함과 숭고함이 타인을 돌보느라 지친 ISFJ에게 깊은 위안을 줍니다."
            },
            {
                "name": "덴마크 🇩🇰",
                "reason": "사회복지가 발달하고 사람들이 서로 배려하는 문화가 공동체 정신을 중시하는 ISFJ의 이상향입니다.",
                "attraction": "니하운",
                "attraction_reason": "코펜하겐의 상징적인 컬러풀한 운하로, 평화롭고 아름다운 일상의 모습이 ISFJ의 따뜻한 마음을 편안하게 합니다."
            },
            {
                "name": "캐나다 🇨🇦",
                "reason": "친절하고 포용적인 문화로 유명한 나라로, 배려심 많은 ISFJ가 편안하게 여행할 수 있는 환경을 제공합니다.",
                "attraction": "나이아가라 폭포",
                "attraction_reason": "자연의 웅장함과 아름다움이 ISFJ의 마음을 치유하고, 생명의 소중함을 다시 한번 깨닫게 해줍니다."
            }
        ]
    },
    "ESTJ": {
        "personality": "경영자형 💼",
        "description": "체계적이고 효율적인 당신",
        "destinations": [
            {
                "name": "홍콩 🇭🇰",
                "reason": "동서양의 비즈니스 허브로, 효율적인 시스템과 국제적 감각을 갖춘 ESTJ에게 완벽한 비즈니스 여행지입니다.",
                "attraction": "빅토리아 피크",
                "attraction_reason": "홍콩의 전경을 한눈에 볼 수 있는 곳으로, 도시의 효율성과 발전상을 파악하며 ESTJ의 경영 마인드를 자극합니다."
            },
            {
                "name": "싱가포르 🇸🇬",
                "reason": "완벽한 도시 계획과 효율적인 시스템으로 유명한 나라로, 체계적인 ESTJ의 성향과 완벽하게 일치합니다.",
                "attraction": "마리나 베이 샌즈",
                "attraction_reason": "현대적 건축과 비즈니스의 상징으로, 효율성과 성공을 추구하는 ESTJ에게 영감과 동기부여를 제공합니다."
            },
            {
                "name": "스위스 취리히 🇨🇭",
                "reason": "세계적인 금융 중심지로, 정확성과 신뢰성을 바탕으로 한 비즈니스 문화가 ESTJ의 이상향입니다.",
                "attraction": "스위스 국립박물관",
                "attraction_reason": "스위스의 체계적인 역사와 문화를 보여주는 곳으로, 전통과 혁신의 균형을 추구하는 ESTJ의 가치관과 부합합니다."
            }
        ]
    },
    "ESFJ": {
        "personality": "집정관형 🤝",
        "description": "사교적이고 협력적인 당신",
        "destinations": [
            {
                "name": "이탈리아 🇮🇹",
                "reason": "따뜻한 인정과 가족 중심의 문화가 사람들과의 관계를 중시하는 ESFJ에게 완벽한 여행 경험을 제공합니다.",
                "attraction": "로마 콜로세움",
                "attraction_reason": "고대 로마의 역사와 문화를 체험할 수 있는 곳으로, 사람들과 함께 역사를 공유하며 소통하는 ESFJ의 성향을 만족시킵니다."
            },
            {
                "name": "그리스 🇬🇷",
                "reason": "신화와 역사가 살아있는 나라로, 사람들과의 이야기를 나누며 문화를 체험하는 것을 좋아하는 ESFJ에게 이상적입니다.",
                "attraction": "파르테논 신전",
                "attraction_reason": "고대 그리스 문명의 상징으로, 사람들과 함께 역사적 의미를 공유하며 깊은 유대감을 형성할 수 있는 공간입니다."
            },
            {
                "name": "터키 🇹🇷",
                "reason": "동서양이 만나는 독특한 문화와 따뜻한 환대로 유명한 나라로, 사교적인 ESFJ가 다양한 사람들과 교류할 수 있습니다.",
                "attraction": "카파도키아",
                "attraction_reason": "독특한 지형과 열기구 체험으로, 사람들과 함께 특별한 추억을 만들며 관계를 더욱 돈독하게 할 수 있는 곳입니다."
            }
        ]
    },
    "ISTP": {
        "personality": "장인형 🔧",
        "description": "실용적이고 독립적인 당신",
        "destinations": [
            {
                "name": "뉴질랜드 🇳🇿",
                "reason": "모험 스포츠의 천국으로, 실용적인 기술과 모험을 추구하는 ISTP에게 완벽한 액티비티를 제공합니다.",
                "attraction": "퀸스타운",
                "attraction_reason": "번지점프의 발원지로, 실용적 기술과 모험 정신을 동시에 만족시키는 ISTP의 이상적인 체험 공간입니다."
            },
            {
                "name": "노르웨이 🇳🇴",
                "reason": "피오르드와 오로라 등 자연 현상을 직접 체험할 수 있어, 실용적 지식과 자연을 사랑하는 ISTP에게 완벽합니다.",
                "attraction": "가이랑에르 피오르드",
                "attraction_reason": "자연이 만든 완벽한 지형으로, 자연의 원리와 메커니즘을 이해하고 싶어하는 ISTP의 탐구심을 자극합니다."
            },
            {
                "name": "일본 🇯🇵",
                "reason": "정밀한 기술과 장인정신이 살아있는 나라로, 실용적 기술을 추구하는 ISTP의 가치관과 완벽하게 일치합니다.",
                "attraction": "후지산",
                "attraction_reason": "일본의 상징으로, 등반을 통해 자신만의 방식으로 자연을 정복하고 내적 성장을 이룰 수 있는 곳입니다."
            }
        ]
    },
    "ISFP": {
        "personality": "모험가형 🎨",
        "description": "예술적이고 감성적인 당신",
        "destinations": [
            {
                "name": "모로코 🇲🇦",
                "reason": "다채로운 색감과 독특한 문화가 어우러진 나라로, 예술적 감각이 뛰어난 ISFP에게 무한한 영감을 제공합니다.",
                "attraction": "마라케시 구시가지",
                "attraction_reason": "전통적인 모로코 문화와 예술이 살아있는 곳으로, 수공예품과 독특한 건축물이 ISFP의 예술적 감성을 자극합니다."
            },
            {
                "name": "인도 🇮🇳",
                "reason": "다양한 색채와 문화가 공존하는 나라로, 감성적이고 예술적인 ISFP가 깊은 영감을 받을 수 있는 곳입니다.",
                "attraction": "타지마할",
                "attraction_reason": "사랑의 상징으로 지어진 완벽한 건축물로, 로맨틱하고 예술적인 ISFP의 감성을 깊이 움직이는 걸작입니다."
            },
            {
                "name": "페루 🇵🇪",
                "reason": "고대 문명과 신비로운 자연이 어우러진 나라로, 독특한 문화와 예술을 추구하는 ISFP에게 완벽한 여행지입니다.",
                "attraction": "마추픽추",
                "attraction_reason": "잉카 문명의 신비로운 유적으로, 고대 예술과 자연의 조화가 ISFP의 감성과 상상력을 극대화합니다."
            }
        ]
    },
    "ESTP": {
        "personality": "사업가형 🏃",
        "description": "활동적이고 즉흥적인 당신",
        "destinations": [
            {
                "name": "호주 🇦🇺",
                "reason": "다양한 익스트림 스포츠와 액티비티가 가능한 나라로, 모험을 추구하는 ESTP에게 완벽한 놀이터입니다.",
                "attraction": "그레이트 배리어 리프",
                "attraction_reason": "세계 최대 산호초 지대로, 스쿠버다이빙과 스노클링 등 스릴 넘치는 수중 활동을 즐길 수 있는 ESTP의 이상향입니다."
            },
            {
                "name": "남아프리카공화국 🇿🇦",
                "reason": "사파리와 익스트림 스포츠가 공존하는 나라로, 즉흥적이고 모험적인 ESTP에게 무한한 즐거움을 제공합니다.",
                "attraction": "케이프타운",
                "attraction_reason": "테이블 마운틴 등반과 상어 케이지 다이빙 등 스릴 넘치는 활동이 가능한 곳으로 ESTP의 모험심을 완전히 만족시킵니다."
            },
            {
                "name": "코스타리카 🇨🇷",
                "reason": "집라이닝, 래프팅 등 다양한 어드벤처 스포츠가 가능한 나라로, 액션을 추구하는 ESTP에게 완벽한 여행지입니다.",
                "attraction": "아레날 화산",
                "attraction_reason": "활화산 주변에서 다양한 액티비티를 즐길 수 있는 곳으로, 위험하지만 스릴 넘치는 경험을 원하는 ESTP에게 최적입니다."
            }
        ]
    },
    "ESFP": {
        "personality": "연예인형 🎉",
        "description": "사교적이고 즐거움을 추구하는 당신",
        "destinations": [
            {
                "name": "스페인 🇪🇸",
                "reason": "열정적인 플라멘코와 축제 문화가 있는 나라로, 즐거움과 표현을 사랑하는 ESFP에게 완벽한 무대입니다.",
                "attraction": "라 사그라다 파밀리아",
                "attraction_reason": "가우디의 독창적인 건축물로, 화려하고 독특한 디자인이 표현력 풍부한 ESFP의 감성을 자극합니다."
            },
            {
                "name": "브라질 🇧🇷",
                "reason": "삼바와 카니발의 나라로, 음악과 춤을 사랑하는 ESFP가 자유롭게 자신을 표현할 수 있는 최적의 장소입니다.",
                "attraction": "리우 카니발",
                "attraction_reason": "세계 최대 축제로, 음악과 춤, 화려한 의상으로 자신을 표현하는 ESFP에게 꿈같은 경험을 선사합니다."
            },
            {
                "name": "인도네시아 발리 🇮🇩",
                "reason": "아름다운 자연과 독특한 문화가 어우러진 섬으로, 사교적이고 즐거움을 추구하는 ESFP에게 완벽한 휴양지입니다.",
                "attraction": "울루와투 사원",
                "attraction_reason": "절벽 위의 아름다운 사원으로, 전통 케찰 댄스 공연을 보며 문화와 예술을 체험할 수 있는 ESFP의 이상적인 공간입니다."
            }
        ]
    }
}

def show_balloons():
    """풍선 효과를 보여주는 함수"""
    st.balloons()

def show_snow():
    """눈 효과를 보여주는 함수"""
    st.snow()

def main():
    # 메인 헤더
    st.markdown('<h1 class="main-header">✈️ MBTI 여행지 추천 🌍</h1>', unsafe_allow_html=True)
    
    # 소개 메시지
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem; color: #666;">
        당신의 MBTI 성격유형에 맞는 완벽한 여행지를 찾아보세요! 🎒✨
    </div>
    """, unsafe_allow_html=True)
    
    # MBTI 선택
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        mbti_types = list(MBTI_DESTINATIONS.keys())
        selected_mbti = st.selectbox(
            "🎯 당신의 MBTI를 선택하세요:",
            mbti_types,
            format_func=lambda x: f"{x} - {MBTI_DESTINATIONS[x]['personality']}"
        )
    
    if selected_mbti:
        # 선택된 MBTI 정보 표시
        mbti_info = MBTI_DESTINATIONS[selected_mbti]
        
        # MBTI 배지 표시
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <span class="mbti-badge">{selected_mbti} - {mbti_info['personality']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 성격 설명
        st.markdown(f"""
        <div style="text-align: center; font-size: 1.1rem; margin-bottom: 2rem; color: #555;">
            {mbti_info['description']}
        </div>
        """, unsafe_allow_html=True)
        
        # 추천 버튼
        if st.button("🎁 나만의 여행지 추천받기!", key="recommend_btn"):
            show_balloons()
            time.sleep(0.5)
            
            st.markdown("---")
            st.markdown("## 🌟 당신을 위한 특별한 여행지 추천")
            
            # 각 여행지를 카드 형태로 표시
            for i, destination in enumerate(mbti_info['destinations'], 1):
                st.markdown(f"""
                <div class="destination-card">
                    <h3>🏆 추천 {i}위: {destination['name']}</h3>
                    <p><strong>🎯 추천 이유:</strong> {destination['reason']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # 관광지 정보
                st.markdown(f"""
                <div class="attraction-card">
                    <h4>📍 꼭 가봐야 할 관광지: {destination['attraction']}</h4>
                    <p><strong>✨ 특별한 이유:</strong> {destination['attraction_reason']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
            
            # 마무리 메시지
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; font-size: 1.1rem; color: #2E86AB; margin: 2rem 0;">
                <strong>🎉 당신만의 특별한 여행을 떠나보세요! 🎉</strong><br>
                새로운 경험과 추억이 기다리고 있습니다! ✨
            </div>
            """, unsafe_allow_html=True)
            
            # 추가 효과
            if st.button("🎊 축하해요!", key="celebrate_btn"):
                show_snow()
                st.success("🌟 멋진 여행 되세요! 🌟")
    
    # 푸터
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #888; margin-top: 2rem;">
        💡 <strong>Tip:</strong> 다른 MBTI 유형도 궁금하다면 위에서 다시 선택해보세요!<br>
        🎪 즐거운 여행 계획 되세요! 🎪
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
